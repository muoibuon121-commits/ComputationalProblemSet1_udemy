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

##  Tech Stack & Environment


<p>
  <b> Programming Languages:</b> 
  <img align="middle" src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python" /><img align="middle" src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white" alt="C++" /><img align="middle" src="https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white" alt="R" /><img align="middle" src="https://img.shields.io/badge/Ruby-CC342D?style=for-the-badge&logo=ruby&logoColor=white" alt="Ruby" /><img align="middle" src="https://img.shields.io/badge/Swift-FA7343?style=for-the-badge&logo=swift&logoColor=white" alt="Swift" /><img align="middle" src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="SQL" />
</p>

<p>
  <b> Data Science & Machine Learning:</b> 
  <img align="middle" src="

## Author 
Github: Muối 
