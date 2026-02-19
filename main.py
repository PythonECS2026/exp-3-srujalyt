# AIM: Write a Python program to calculate the gross salary of an employee.
# Coder:Srujal
# Date:18/02/2026

print("Salary Calculator")
Basic_Salary = float(input("Enter the Basic Salary(BA) : "))

print("Salary Details:")
DA = 0.70 * Basic_Salary
TA = 0.30 * Basic_Salary
HRA = 0.10 * Basic_Salary
gross_salary = Basic_Salary + DA + TA + HRA
print(f"Basic Salary:  {Basic_Salary}\t")
print(f"DA(70%):       {DA}\t")
print(f"TA(30%):       {TA}\t")
print(f"HRA(10%):      {HRA}\t")
print(f"GROSS SALARY:  {gross_salary}")

