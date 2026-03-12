# ComputationalProblemSet1_udemy
## Featured Coursework: Fixed Income & Computational Finance

**Computational Problem Set 1: Bond Pricing, Yield Sensitivity & Bootstrapping**
*(Status: In Progress | Tech Stack: Python, QuantLib, SciPy)*

---

### Problem 1: Interest Rates and Bond Prices
Explore the relationship between interest rates and bond prices. 

**Setup:** Create a coupon bond with a 5-year maturity, paying a 6% coupon semiannually. Create a flat yield curve with a 7% rate level.
* **(a) Yield Sensitivity:** Price the bond with a flat yield curve with rate levels varying between 5% and 9%. Use the shift method of the curve object to perturb the rate level from the 7% base level.
* **(b) Maturity Effect:** While keeping the same coupons, create new bond objects with maturities of 6, 8, 10, 15, and 20 years. For each bond, carry out the same exercise as in (a). *Objective: Conclude about the yield sensitivity of bond prices and how maturity affects it.*
* **(c) Coupon Effect:** Starting from the bond in (a), leaving maturity constant, try coupon rates of 8%, 10%, 15%, 20%, and 30%. *Objective: Characterize the coupon effect on the yield sensitivity of bonds.*

---

### Problem 2: Yield-to-Maturity (YTM) Dynamics
Explore the behavior of the yield-to-maturity using numerical root-finding methods.

**Setup:** Create a reasonable coupon bond (e.g., 6% coupon, 5-year maturity).
* **Analysis:** Use the YTM method of the bond object to find the yield-to-maturity if the bond were trading at par. Compare the result to the specified coupon rate.
* **Perturbation:** Perturb the price and observe how the yield-to-maturity responds. Try both premium and discount bonds. 
*(Note: Computing the YTM involves root finding, introducing manageable numerical errors).*

---

### Problem 3: Bootstrapping the Yield Curve
Explore the relationship between the implied yield curve and the market/contractual characteristics of the bonds.

**Setup:** Use the `curve_factory` function to bootstrap the bonds from problem set #1 and confirm earlier constructions.
* **Experiment 1 (Parallel Shift):** Increase and decrease all bond prices together in increments of 5% of the face value.
* **Experiment 2 (Curve Steepening/Flattening):** Perturb only the long-maturity bond prices, leaving the short-maturity bonds fixed. Repeat by holding the long bonds constant and perturbing the short ones.
* **Experiment 3 (Coupon Adjustment):** Adjust the coupons of the bonds in a similar investigation.
* **Objective:** In all experiments, observe and characterize the impact on the bootstrapped yield curve.

---

<div align="center">
  <img src="[LINK_ẢNH_PIXEL_ART_CỦA_BẠN]" width="350" alt="Quant/AI Developer Pixel Art" />
  
  <h1>Hi there, I'm [Tên của bạn]! 👋</h1>
  <p><b>Aspiring Quantitative Researcher | Financial Volatility Analyst</b></p>
  <p><i>Building robust models, exploring financial markets, and pushing the boundaries of AI.</i></p>
</div>

---

## 🛠 Project Tech Stack & Environment

Dự án này được xây dựng và mô phỏng hoàn toàn dựa trên các công cụ chuyên sâu về Quantitative Finance và Data Science dưới đây:

<p>
  <b>💻 Core Language & Environment:</b><br>
  <img align="middle" src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python" />
  <img align="middle" src="https://img.shields.io/badge/Jupyter-F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white" alt="Jupyter Notebook" />
</p>

<p>
  <b>📈 Quantitative & Financial Modeling:</b><br>
  <img align="middle" src="https://img.shields.io/badge/QuantLib-F37021?style=for-the-badge" alt="QuantLib" />
</p>

<p>
  <b>📊 Data Manipulation & Visualization:</b><br>
  <img align="middle" src="https://img.shields.io/badge/NumPy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
  <img align="middle" src="https://img.shields.io/badge/Pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img align="middle" src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge" alt="Matplotlib" />
</p>

---

## Featured Coursework & Research

**Currently focusing on Fixed Income valuation and building robust financial models using Python and QuantLib.**

### 📉 Computational Problem Set 1: Bond Pricing & Yield Dynamics
*(Status: In Progress | Tech Stack: Python, QuantLib, NumPy, Matplotlib)*

* **Problem 1 (Yield Sensitivity & Maturity):** Explored the fundamental relationship between interest rates and bond prices by constructing a flat yield curve and pricing 5-year coupon bonds. Investigated the effects of varying maturities (6 to 20 years) and coupon rates (8% to 30%) on yield sensitivity using `QuantLib` shift methods.
* **Problem 2 (Yield-to-Maturity):** Implemented numerical root-finding algorithms to investigate YTM behavior for bonds trading at par, premium, and discount. 
* **Problem 3 (Bootstrapping):** Utilized `curve_factory` functions to bootstrap yield curves. Conducted scenario analysis (parallel shifts, curve steepening/flattening) to observe the implied yield curve's reaction to market perturbations.

---

