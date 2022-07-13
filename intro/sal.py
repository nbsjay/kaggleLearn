# calculate the weekly pay based on work hours, pay per hour, and tax rate


def get_pay(num_hours, hour_pay, taxrate):
    
    pay_pretax = num_hours * hour_pay
    
    # After-tax pay, based on user unputed tax
    pay_aftertax = pay_pretax * (1 - taxrate)
    return pay_aftertax


# Calculate pay based on working hours
x = int(input("how many hours do you work in a week?   "))
y = int(input("How much are you paid per hour?  "))
z = float(input("enter the current tax rate in decimal?  "))

print(f"Your salary after tax is {get_pay(x, y, z)}")
