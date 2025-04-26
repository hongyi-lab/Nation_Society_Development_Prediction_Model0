# StateDynamics-MVP
> *Layered Life-Cycle × Tension Function × Narrative Bandwidth × Elite Payoff × Capital Velocity × Cross-Friction*

## 1. Why：
Existing political instability predictions rely solely on single-layer, static models. 
This project pioneers a six-variable coupled equation framework, delivering a computationally viable semi-automated governance engine.
现有政治不稳定预测只做 **单层+静态**。本项目首创六变量耦合方程，提供
可演算的 **半自动治理引擎**。

## 2. Core Equations (Preview)
1. **Multi-Layer Life-Cycle**  
   $$ Life(t)=\sum_L w_L·Stage_L(t-τ_L) $$
2. **Tension Function**  
   $$ T=αΔW+βΔC+γΔS $$  
   $$ T_{crit}=T·(1-ηE) $$
3. **Narrative Bandwidth**  
   $$ S_{eff}=S_{local}+B(t)·S_{import} $$
4. **External Shock Convolution**  
   $$ \mathcal{F}(t)=\sum A_k e^{-λ_k(t-t_k)} $$
5. **Capital vs. Skill Scissors**  
   $$ Π_{ind}=σSkill-μ_k+ρ\dot M -ψTax $$
6. **Collapse Condition**  
   $$ R_{eff}<R_{min}\ ∨\ S_{eff}<S_{min} $$

*（For detailed formula version, seen in the whitepaper - /docs/whitepaper_draft.pdf)*

## 3. Roadmap
- [ ] toy dataset (US / FIN / ETH)  
- [ ] `risk_score()` Python function  
- [ ] Jupyter demo & quick back-test  
- [ ] arXiv v0.3 (4-page working paper)

## 4. License
MIT — fork 自由，署名必留。（ free to fork, but attribution is required ) 

*Time-stamped 2025-04-26.*
