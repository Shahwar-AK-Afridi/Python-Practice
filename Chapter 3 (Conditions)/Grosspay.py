hrs = input("Enter Hours:")
rate = input("Enter the rate:")
h = float(hrs)
r = float(rate)

if h <= 40:
    grosspay = h*r
    print("Grosspay:", grosspay)
elif h > 40:
    pay_below_40 = 40*r
    remain = h - 40
    r = r*1.5
    pay_above_40 = remain*r
    sum = pay_above_40 + pay_below_40
    print(sum)
else:
    print("invalid input")
