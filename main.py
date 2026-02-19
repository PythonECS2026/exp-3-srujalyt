# AIM: Write a Python program to calculate the gross salary of an employee.
# Coder:Srujal
# Date:18/02/2026
basic_salary = float(input("Enter the Basic Salary (BS): "))
da = 0.70 * basic_salary
ta = 0.30 * basic_salary
hra = 0.10 * basic_salary
gross_salary = basic_salary + da + ta + hra
print(f"Basic Salary:    {basic_salary}\t")
print(f"Dearness (DA):   {da}\t")
print(f"Travel (TA):     {ta}\t")
print(f"House Rent(HRA): {hra}\t")

print(f"GROSS SALARY:    {gross_salary}")

