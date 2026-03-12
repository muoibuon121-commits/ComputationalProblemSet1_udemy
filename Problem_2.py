import QuantLib as ql
import numpy as np
import matplotlib.pyplot as plt

# Sử dụng lại môi trường từ Bài 1
calc_date = ql.Date(12, 3, 2026)
ql.Settings.instance().evaluationDate = calc_date
calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond)
day_count = ql.ActualActual(ql.ActualActual.ISMA)
# SETUP: Tạo trái phiếu 5 năm, Coupon 6%
maturity_years = 5
coupon_rate = 0.06
face_value = 100.0

issue_date = calc_date
maturity_date = calendar.advance(issue_date, ql.Period(maturity_years, ql.Years))
schedule = ql.Schedule(issue_date, maturity_date, ql.Period(ql.Semiannual),
                       calendar, ql.Unadjusted, ql.Unadjusted,
                       ql.DateGeneration.Backward, False)

bond = ql.FixedRateBond(0, face_value, schedule, [coupon_rate], day_count)

# ==========================================
# PHẦN 1: TÍNH YTM KHI GIAO DỊCH TẠI PAR (TRẢ BẰNG MỆNH GIÁ)
# ==========================================
print("--- Part 1: YTM at Par ---")
par_price = 100.0
# Sử dụng hàm bondYield của QuantLib (chứa thuật toán root-finding)
ytm_at_par = bond.bondYield(par_price, day_count, ql.Compounded, ql.Semiannual)

print(f"Bond Price: {par_price}")
print(f"Specified Coupon Rate: {coupon_rate * 100:.2f}%")
print(f"Calculated YTM: {ytm_at_par * 100:.2f}%")
print("-> Observation: When a bond trades at par, its YTM exactly equals its coupon rate.\n")
# PHẦN 2: PERTURBATION VÀ SAI SỐ TÌM NGHIỆM
print("--- Part 2: Price Perturbations & Root-Finding Errors ---")
# Tạo mảng giá từ Premium (110) xuống Discount (90)
test_prices = [110.0, 105.0, par_price, 95.0, 90.0]
print(f"{'Target Price':<15} | {'Calculated YTM':<15} | {'Recalculated Price':<20} | {'Numerical Error':<20}")
print("-" * 75)
ytm_list = []
for p in test_prices:
    # 1. Tìm YTM từ Giá (Root-finding)
    implied_ytm = bond.bondYield(p, day_count, ql.Compounded, ql.Semiannual)
    ytm_list.append(implied_ytm)  
    # 2. Tính ngược lại Giá từ YTM vừa tìm được để kiểm tra sai số
    # Sử dụng hàm cleanPrice để định giá ngược lại
    recalc_price = bond.cleanPrice(implied_ytm, day_count, ql.Compounded, ql.Semiannual) 
    # 3. Tính sai số (Error)
    error = abs(p - recalc_price)
    status = "Premium" if p > 100 else ("Par" if p == 100 else "Discount")
    print(f"{p:<6} ({status:<8}) | {implied_ytm*100:>7.4f}%      | {recalc_price:>18.14f} | {error:>18.2e}")

# VẼ BIỂU ĐỒ (PRICE - YTM RELATIONSHIP)
prices_plot = np.linspace(80, 120, 100)
ytms_plot = [bond.bondYield(p, day_count, ql.Compounded, ql.Semiannual) * 100 for p in prices_plot]

plt.figure(figsize=(10, 6))
plt.plot(ytms_plot, prices_plot, color='darkred', linewidth=2)
plt.axhline(y=100, color='grey', linestyle='--', alpha=0.7)
plt.axvline(x=6.0, color='grey', linestyle='--', alpha=0.7)

plt.scatter([ytm_at_par*100], [par_price], color='black', zorder=5, label='Par Bond (Price=100, YTM=6%)')

plt.title("Yield-to-Maturity vs. Bond Price (Convexity)", fontsize=14, fontweight='bold')
plt.xlabel("Yield to Maturity (%)")
plt.ylabel("Bond Price")
plt.legend()
plt.tight_layout()
plt.show()
