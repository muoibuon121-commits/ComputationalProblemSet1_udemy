import QuantLib as ql
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-darkgrid')
calc_date = ql.Date(12, 3, 2026)
ql.Settings.instance().evaluationDate = calc_date
calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond)
day_count = ql.ActualActual(ql.ActualActual.ISMA)

def setup_environment(base_rate=0.07):
    """
    Tạo đường cong lợi suất phẳng (Flat Forward Curve).
    Sử dụng SimpleQuote để dễ dàng 'shift' (dịch chuyển) lãi suất mà không cần tạo lại đường cong.
    """
    rate_quote = ql.SimpleQuote(base_rate)
    rate_handle = ql.QuoteHandle(rate_quote)
    yield_curve = ql.FlatForward(calc_date, rate_handle, day_count, ql.Compounded, ql.Semiannual)
    curve_handle = ql.YieldTermStructureHandle(yield_curve)
    
    return rate_quote, curve_handle

def create_bond(maturity_years, coupon_rate, curve_handle):
    """Hàm hỗ trợ tạo đối tượng Trái phiếu (Fixed Rate Bond)"""
    issue_date = calc_date
    maturity_date = calendar.advance(issue_date, ql.Period(maturity_years, ql.Years))
    
    # Lịch trả lãi (Schedule)
    schedule = ql.Schedule(issue_date, maturity_date, ql.Period(ql.Semiannual),
                           calendar, ql.Unadjusted, ql.Unadjusted,
                           ql.DateGeneration.Backward, False)
    
    face_value = 100.0
    settlement_days = 0
    bond = ql.FixedRateBond(settlement_days, face_value, schedule, [coupon_rate], day_count)
    
    # Gắn Engine định giá
    engine = ql.DiscountingBondEngine(curve_handle)
    bond.setPricingEngine(engine)
    
    return bond


# PHẦN (a): YIELD SENSITIVITY 
print("--- Part (a): Basic Yield Sensitivity ---")
rate_quote, curve_handle = setup_environment(0.07) # Base rate 7%
bond_5y_6c = create_bond(maturity_years=5, coupon_rate=0.06, curve_handle=curve_handle)

rates_to_test = np.linspace(0.05, 0.09, 50) # Chạy từ 5% đến 9%
prices_a = []

for r in rates_to_test:
    rate_quote.setValue(r)  # Shift method: Cập nhật lãi suất trực tiếp
    prices_a.append(bond_5y_6c.NPV())

# Trả rate về lại 7%
rate_quote.setValue(0.07)
print(f"Base Price (7% Yield): {bond_5y_6c.NPV():.4f}")

# PHẦN (b): EFFECT OF MATURITY (ẢNH HƯỞNG CỦA KỲ HẠN)
maturities = [5, 6, 8, 10, 15, 20] # Đã thêm 5y làm cơ sở so sánh
prices_b = {m: [] for m in maturities}

for m in maturities:
    temp_bond = create_bond(maturity_years=m, coupon_rate=0.06, curve_handle=curve_handle)
    for r in rates_to_test:
        rate_quote.setValue(r)
        prices_b[m].append(temp_bond.NPV())

# PHẦN (c): EFFECT OF COUPON (ẢNH HƯỞNG CỦA COUPON)
coupons = [0.06, 0.08, 0.10, 0.15, 0.20, 0.30] # Thêm 6% làm cơ sở
prices_c = {c: [] for c in coupons}

for c in coupons:
    temp_bond = create_bond(maturity_years=5, coupon_rate=c, curve_handle=curve_handle)
    for r in rates_to_test:
        rate_quote.setValue(r)
        prices_c[c].append(temp_bond.NPV())

fig, axes = plt.subplots(1, 2, figsize=(16, 6))
for m in maturities:
    axes[0].plot(rates_to_test * 100, prices_b[m], label=f'{m} Years')
axes[0].set_title("Part (b): Effect of Maturity on Yield Sensitivity\n(Coupon = 6%)", fontsize=14, fontweight='bold')
axes[0].set_xlabel("Yield to Maturity (%)")
axes[0].set_ylabel("Bond Price")
axes[0].axvline(x=7, color='grey', linestyle='--', alpha=0.5) # Đường base rate
axes[0].legend()

# Đồ thị (c) - Coupon
# Để so sánh độ nhạy chuẩn xác, ta chuyển giá về dạng % thay đổi so với giá gốc tại Yield = 7%
axes[1].set_title("Part (c): Effect of Coupon on Yield Sensitivity\n(Maturity = 5 Years, Normalized)", fontsize=14, fontweight='bold')
for c in coupons:
    # Tính giá base tại rate = 7%
    rate_quote.setValue(0.07)
    base_price = prices_c[c][rates_to_test.tolist().index(min(rates_to_test, key=lambda x:abs(x-0.07)))]
    normalized_prices = [(p / base_price) * 100 for p in prices_c[c]]
    
    axes[1].plot(rates_to_test * 100, normalized_prices, label=f'Coupon {c*100:.0f}%')

axes[1].set_xlabel("Yield to Maturity (%)")
axes[1].set_ylabel("Normalized Bond Price (Base = 100 at 7% Yield)")
axes[1].axvline(x=7, color='grey', linestyle='--', alpha=0.5)
axes[1].legend()

plt.tight_layout()
plt.show()
