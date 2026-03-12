import QuantLib as ql
import numpy as np
import matplotlib.pyplot as plt
# 0. THIẾT LẬP MÔI TRƯỜNG 
calc_date = ql.Date(12, 3, 2026)
ql.Settings.instance().evaluationDate = calc_date
calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond)
day_count = ql.ActualActual(ql.ActualActual.ISMA)

# Các kỳ hạn từ Bài 1
maturities = [5, 6, 8, 10, 15, 20]
base_coupon = 0.06
base_prices = [100.0] * len(maturities) # Giá Par = 100

def curve_factory(maturities, coupons, prices):
    """
    Hàm Bootstrapping: Xây dựng đường cong lợi suất (Yield Curve) 
    từ danh sách kỳ hạn, coupons và giá trái phiếu.
    """
    helpers = []
    # Đảm bảo coupons là một list có cùng độ dài với maturities
    if isinstance(coupons, float):
        coupons = [coupons] * len(maturities)
        
    for m, c, p in zip(maturities, coupons, prices):
        maturity_date = calendar.advance(calc_date, ql.Period(m, ql.Years))
        schedule = ql.Schedule(calc_date, maturity_date, ql.Period(ql.Semiannual),
                               calendar, ql.Unadjusted, ql.Unadjusted,
                               ql.DateGeneration.Backward, False)
        
        # Quote giá trái phiếu
        price_handle = ql.QuoteHandle(ql.SimpleQuote(p))
        
        # Tạo BondHelper để QuantLib tự động giải hệ phương trình tìm Zero Rate
        helper = ql.FixedRateBondHelper(price_handle, 0, 100.0, schedule, [c], day_count, ql.Unadjusted)
        helpers.append(helper)
    
    # Xây dựng đường cong nội suy Log-Linear
    yield_curve = ql.PiecewiseLogLinearDiscount(calc_date, helpers, day_count)
    yield_curve.enableExtrapolation()
    return yield_curve

def get_curve_points(curve, max_years=20):
    """Hàm hỗ trợ lấy các điểm trên đường cong để vẽ đồ thị"""
    plot_years = np.linspace(1, max_years, 50)
    rates = []
    for y in plot_years:
        # Cộng số ngày vào ngày hiện tại
        d = calc_date + int(y * 365.25) 
        # Lấy Zero Rate tại ngày đó
        rate = curve.zeroRate(d, day_count, ql.Compounded, ql.Semiannual).rate()
        rates.append(rate * 100)
    return plot_years, rates

# THÍ NGHIỆM 1: PARALLEL SHIFT (DỊCH CHUYỂN SONG SONG)
curve_base = curve_factory(maturities, base_coupon, base_prices)
curve_up5 = curve_factory(maturities, base_coupon, [p + 5.0 for p in base_prices])
curve_down5 = curve_factory(maturities, base_coupon, [p - 5.0 for p in base_prices])
# THÍ NGHIỆM 2: STEEPENING & FLATTENING (ĐỘ DỐC ĐƯỜNG CONG)
# Steepening: Trái phiếu ngắn hạn giá giữ nguyên (100), trái phiếu dài hạn rớt giá (90) -> Lợi suất dài hạn tăng
steep_prices = [100.0, 100.0, 95.0, 90.0, 85.0, 80.0]
curve_steep = curve_factory(maturities, base_coupon, steep_prices)

# Flattening/Inverted: Trái phiếu ngắn hạn rớt giá (85), trái phiếu dài hạn giữ nguyên (100)
flat_prices = [85.0, 90.0, 95.0, 100.0, 100.0, 100.0]
curve_flat = curve_factory(maturities, base_coupon, flat_prices)
# THÍ NGHIỆM 3: COUPON ADJUSTMENT (THAY ĐỔI LÃI SUẤT CUỐNG PHIẾU)
# Cùng mức giá Par (100), nhưng Coupon các năm cuối cao hơn
steep_coupons = [0.06, 0.06, 0.07, 0.08, 0.09, 0.10]
curve_coupon_adj = curve_factory(maturities, steep_coupons, base_prices)

# VẼ BIỂU ĐỒ (VISUALIZATION)
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Đồ thị 1: Parallel Shift
x, y_base = get_curve_points(curve_base)
_, y_up5 = get_curve_points(curve_up5)
_, y_down5 = get_curve_points(curve_down5)

axes[0].plot(x, y_base, label='Base (Prices=100)', color='black', linewidth=2)
axes[0].plot(x, y_up5, label='Prices +5% (105)', color='green', linestyle='--')
axes[0].plot(x, y_down5, label='Prices -5% (95)', color='red', linestyle='--')
axes[0].set_title("Exp 1: Parallel Shift (Price Impact)", fontweight='bold')
axes[0].set_ylabel("Zero Yield (%)")
axes[0].legend()

# Đồ thị 2: Steepening & Flattening
_, y_steep = get_curve_points(curve_steep)
_, y_flat = get_curve_points(curve_flat)

axes[1].plot(x, y_base, label='Base Curve', color='black', linewidth=2)
axes[1].plot(x, y_steep, label='Steepening (Long Bonds drop in price)', color='purple', linestyle='-.')
axes[1].plot(x, y_flat, label='Flattening/Inverted (Short Bonds drop)', color='orange', linestyle='-.')
axes[1].set_title("Exp 2: Curve Steepening vs Flattening", fontweight='bold')
axes[1].legend()

# Đồ thị 3: Coupon Adjustment
_, y_coup = get_curve_points(curve_coupon_adj)

axes[2].plot(x, y_base, label='Base (Coupons=6%)', color='black', linewidth=2)
axes[2].plot(x, y_coup, label='Higher Coupons for Long Bonds', color='blue', linestyle=':')
axes[2].set_title("Exp 3: Implied Yield with Increasing Coupons", fontweight='bold')
axes[2].legend()

for ax in axes:
    ax.set_xlabel("Maturity (Years)")
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
