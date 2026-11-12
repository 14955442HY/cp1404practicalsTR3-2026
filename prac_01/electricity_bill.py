# print("Electricity bill estimator")
#
# price_per_kwh = float(input("Enter cents per kWh: "))
# daily_use = float(input("Enter daily use in kWh: "))
# number_of_days = int(input("Enter number of billing days: "))
#
# estimated_bill = price_per_kwh * daily_use * number_of_days / 100
#
# print(f"Estimated bill: ${estimated_bill:.2f}")


TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")

tariff = input("Which tariff? 11 or 31: ")
daily_use = float(input("Enter daily use in kWh: "))
number_of_days = int(input("Enter number of billing days: "))

if tariff == "11":
    price_per_kwh = TARIFF_11
else:
    price_per_kwh = TARIFF_31

estimated_bill = price_per_kwh * daily_use * number_of_days

print(f"Estimated bill: ${estimated_bill:.2f}")