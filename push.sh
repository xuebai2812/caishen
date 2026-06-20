#!/usr/bin/env bash
# 一键把「裁神」skill 推到 GitHub —— 全程终端完成，无需打开网页。
# 用法：  bash push.sh
# 可选环境变量：
#   GH_TOKEN   有 repo 权限的 GitHub Personal Access Token（没装 gh 时需要）
#   PRIVATE    true=私有仓库(默认) / false=公开仓库
set -e

USER="xuebai2812"
EMAIL="xuebai1228@gmail.com"
REPO="caishen"
PRIVATE="${PRIVATE:-true}"

cd "$(dirname "$0")"
echo "==> 工作目录: $(pwd)"

# 0. 清掉之前可能残留的半成品 .git，重新初始化
rm -rf .git
git init -b main -q
git config user.name "$USER"
git config user.email "$EMAIL"
git add -A
git commit -q -m "裁神：中国大陆裁员谈判与维权 Claude Skill 首次提交"
echo "==> 本地已提交：$(git log --oneline -1)"

# 1. 优先使用 gh CLI（若已安装并登录，最省事）
if command -v gh >/dev/null 2>&1; then
  echo "==> 检测到 gh CLI，使用 gh 建库并推送"
  VIS="--private"; [ "$PRIVATE" = "false" ] && VIS="--public"
  # 若仓库已存在，gh repo create 会报错，则退回到直接 push
  if gh repo create "$USER/$REPO" $VIS --source=. --remote=origin --push 2>/dev/null; then
    echo "✅ 完成（gh）：https://github.com/$USER/$REPO"
    exit 0
  fi
  echo "==> 仓库可能已存在，改为直接推送"
  git remote remove origin 2>/dev/null || true
  git remote add origin "https://github.com/$USER/$REPO.git"
  git push -u origin main
  echo "✅ 完成：https://github.com/$USER/$REPO"
  exit 0
fi

# 2. 没有 gh —— 用 GitHub API + Token 建库，再用 token 推送
if [ -z "$GH_TOKEN" ]; then
  read -rsp "粘贴你的 GitHub Personal Access Token（有 repo 权限，输入不回显）: " GH_TOKEN
  echo
fi

echo "==> 通过 GitHub API 创建仓库（已存在则跳过）"
PRIV_JSON=$([ "$PRIVATE" = "false" ] && echo false || echo true)
code=$(curl -s -o /tmp/gh_create.json -w "%{http_code}" \
  -H "Authorization: token $GH_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  https://api.github.com/user/repos \
  -d "{\"name\":\"$REPO\",\"private\":$PRIV_JSON,\"description\":\"裁神 · 中国大陆裁员谈判与维权 Claude Skill\"}")
if [ "$code" = "201" ]; then
  echo "    仓库已创建"
elif grep -q "already exists" /tmp/gh_create.json 2>/dev/null; then
  echo "    仓库已存在，复用"
else
  echo "    创建返回 HTTP $code："; cat /tmp/gh_create.json; echo
fi

echo "==> 推送"
git remote remove origin 2>/dev/null || true
git remote add origin "https://$USER:$GH_TOKEN@github.com/$USER/$REPO.git"
git push -u origin main
# 推送后把 token 从 remote URL 抹掉，避免明文残留
git remote set-url origin "https://github.com/$USER/$REPO.git"
echo "✅ 完成：https://github.com/$USER/$REPO"
