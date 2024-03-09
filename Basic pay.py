HRA_PERCENTAGE = 0.10
TA_PERCENTAGE = 0.05
basic_pay = float(input("Enter the basic pay of the employee: "))
hra = HRA_PERCENTAGE * basic_pay
ta = TA_PERCENTAGE * basic_pay
salary = basic_pay + hra + ta
print("Salary of the employee: ${:.2f}".format(salary))
