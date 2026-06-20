#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
中国大陆经济补偿金 / 赔偿金计算器（N / N+1 / 2N）
依据《劳动合同法》第 47、87 条。

用法：
  交互式：  python compensation_calculator.py
  传参式：  python compensation_calculator.py --years 8 --months 4 \
            --avg-wage 30000 --last-wage 30000 --cap-base 35000

参数说明：
  --years      工作整年数（如 8 年 4 个月填 8）
  --months     不满一年的剩余月数（如 8 年 4 个月填 4）
  --avg-wage   解除前 12 个月平均应发工资（税前，含奖金/津贴/提成）
  --last-wage  上一个月工资（代通知金按此算，不受 3 倍封顶限制）；默认等于 avg-wage
  --cap-base   当地社平工资 × 3 的封顶基数（须查当年官方值）；不传则不封顶

注意：cap-base 每年由各地人社局更新，务必查当年最新值，勿用旧数。
"""
import argparse
import sys


def service_factor(years: int, months: int) -> float:
    """工龄折算为补偿月数倍数。满6个月不满1年按1年，不满6个月按0.5。"""
    factor = float(years)
    if months >= 6:
        factor += 1.0
    elif months > 0:
        factor += 0.5
    return factor


def calc(years, months, avg_wage, last_wage=None, cap_base=None):
    last_wage = avg_wage if last_wage is None else last_wage
    factor = service_factor(years, months)

    capped = False
    base = avg_wage
    capped_factor = factor
    if cap_base is not None and avg_wage > cap_base:
        capped = True
        base = cap_base
        capped_factor = min(factor, 12.0)  # 触发封顶时年限最多 12 年

    n = base * capped_factor
    n_plus_1 = n + last_wage           # 代通知金不受 3 倍封顶限制
    two_n = n * 2

    return {
        "service_factor": factor,
        "applied_factor": capped_factor,
        "capped": capped,
        "base_used": base,
        "N": round(n, 2),
        "N_plus_1": round(n_plus_1, 2),
        "2N": round(two_n, 2),
    }


def fmt(x):
    return f"{x:,.2f}"


def report(r, avg_wage, cap_base):
    lines = []
    lines.append("=" * 48)
    lines.append("           经济补偿 / 赔偿金 测算结果")
    lines.append("=" * 48)
    lines.append(f"工龄折算月数：{r['service_factor']:.1f} 个月")
    if r["capped"]:
        lines.append(f"⚠ 触发 3 倍封顶：月工资 {fmt(avg_wage)} > 封顶基数 {fmt(cap_base)}")
        lines.append(f"  → 基数按 {fmt(r['base_used'])} 计，年限封顶 {r['applied_factor']:.1f} 个月（最多12）")
    else:
        lines.append("未触发 3 倍封顶：按实际工资计，年限不封顶")
    lines.append("-" * 48)
    lines.append(f"N（经济补偿）   ：{fmt(r['N'])} 元")
    lines.append(f"N+1（含代通知金）：{fmt(r['N_plus_1'])} 元")
    lines.append(f"2N（违法解除赔偿）：{fmt(r['2N'])} 元")
    lines.append("=" * 48)
    lines.append("说明：N=合法解除/协商解除（单位提出）的法律底线；")
    lines.append("     2N=公司违法解除时可主张，是谈判与仲裁的核心杠杆。")
    lines.append("本结果为基于一般规则的估算，不构成法律意见。")
    return "\n".join(lines)


def interactive():
    print("中国大陆经济补偿金计算器（回车确认每一项）\n")
    years = int(input("工作整年数（如 8 年 4 个月填 8）: ") or 0)
    months = int(input("剩余月数（如 8 年 4 个月填 4，没有填 0）: ") or 0)
    avg_wage = float(input("解除前 12 个月平均应发工资（税前/元）: ") or 0)
    last_in = input(f"上一个月工资（默认 {avg_wage:.0f}）: ").strip()
    last_wage = float(last_in) if last_in else avg_wage
    cap_in = input("当地社平×3 封顶基数（不清楚就留空，须查当年值）: ").strip()
    cap_base = float(cap_in) if cap_in else None
    r = calc(years, months, avg_wage, last_wage, cap_base)
    print("\n" + report(r, avg_wage, cap_base))


def main():
    p = argparse.ArgumentParser(description="经济补偿金/赔偿金计算器")
    p.add_argument("--years", type=int)
    p.add_argument("--months", type=int, default=0)
    p.add_argument("--avg-wage", type=float)
    p.add_argument("--last-wage", type=float, default=None)
    p.add_argument("--cap-base", type=float, default=None)
    args = p.parse_args()

    if args.years is None or args.avg_wage is None:
        if len(sys.argv) > 1:
            p.error("非交互模式需至少提供 --years 和 --avg-wage")
        interactive()
    else:
        r = calc(args.years, args.months, args.avg_wage, args.last_wage, args.cap_base)
        print(report(r, args.avg_wage, args.cap_base))


if __name__ == "__main__":
    main()
