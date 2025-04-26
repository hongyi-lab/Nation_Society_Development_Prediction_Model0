# core.py — StateDynamics MVP prototype

import math
from typing import List, Tuple

def risk_score(
    delta_W: float,
    delta_C: float,
    delta_S: float,
    B: float,
    S_local: float,
    S_import: float,
    eta_E: float,
    rho_Mdot: float,
    sigma_skill: float,
    mu_k: float,
    psi_tax: float,
    shocks: List[Tuple[float, float, float]],  # list of (A_k, λ_k, t_k)
    t_now: float
) -> dict:
    """
    Prototype function for calculating risk indicators:计算风险指标的雏形函数：
      - T_adj: Adjusted tension调整后张力
      - S_eff: effective narrative resources实效叙事资源
      - shock: external shock convolution外部冲击卷积
      - collapse: whether below threshold (placeholder logic)是否低于阈值（占位逻辑）
      - individual: example of an individual opportunity function个人机会函数示例
    """
    # 1. Liquidity function & scarcity function张力函数 & 精英校正
    T = delta_W + delta_C + delta_S
    T_adj = T * (1.0 - eta_E)

    # 2. Effective narrative resources叙事带宽合成
    S_eff = S_local + B * S_import

    # 3. External shock convolution function (τ)外部冲击卷积 ℱ(t)
    F = 0.0
    for A_k, lam_k, t_k in shocks:
        dt = max(0.0, t_now - t_k)
        F += A_k * math.exp(-lam_k * dt)

    # 4. Available opportunity multiplier (when <=1, no further opportunities are available)可崩溃条件（占位，只做示例）
    R_eff = 1.0  # In the future, it can be replaced by a material resources function. 未来可由物质资源函数替代
    collapse = (R_eff < 1.0) or (S_eff < 1.0)

    # 5. Example of an individual composite signal model个人机会函数剪刀差
    individual = sigma_skill - mu_k + rho_Mdot - psi_tax

    return {
        "T_adj": T_adj,
        "S_eff": S_eff,
        "shock": F,
        "collapse": collapse,
        "individual": individual
    }


if __name__ == "__main__":
    # === Toy example: 3 simple testing data ===
    sample_shocks = [
        (1.0, 0.1, 1990.0),
        (0.5, 0.2, 1995.0),
    ]
    # First Test, function operation testing:
    res = risk_score(
        delta_W=0.3, delta_C=0.2, delta_S=0.1,
        B=0.5, S_local=0.4, S_import=0.6,
        eta_E=0.1, rho_Mdot=0.05, sigma_skill=0.2,
        mu_k=0.05, psi_tax=0.02,
        shocks=sample_shocks,
        t_now=2000.0
    )
    print("Risk score demo:", res)
