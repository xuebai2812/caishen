#!/usr/bin/env bash
# 一键同步：把当前改动提交并推送到 GitHub。
# 用法：
#   bash sync.sh                 # 用默认提交信息
#   bash sync.sh "你的提交说明"   # 自定义提交信息
# 前提：已配好钥匙串免密（git config --global credential.helper osxkeychain）或 gh 登录。
set -e
cd "$(dirname "$0")"

MSG="${1:-更新裁神 skill 内容}"

if [ -z "$(git status --porcelain)" ]; then
  echo "没有需要提交的改动。"
  exit 0
fi

git add -A
git commit -m "$MSG"
git push
echo "✅ 已推送：https://github.com/xuebai2812/caishen"
