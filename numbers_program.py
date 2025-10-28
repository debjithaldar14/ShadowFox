
# 2. NUMBERS

def format_example(num, fmt):
    result = format(num, fmt)
    print("Formatted result:", result)

format_example(145, 'o')

r = 84
pi = 3.14
area = pi * (r ** 2)
water_per_sqm = 1.4
total_water = int(area * water_per_sqm)
print("Area of pond:", area)
print("Total water (liters):", total_water)

distance = 490
time_minutes = 7
time_seconds = time_minutes * 60
speed = int(distance / time_seconds)
print("Speed (m/s):", speed)
