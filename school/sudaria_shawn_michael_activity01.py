#Shawn Michael A. Sudaria BSIT - 1B
def GrossSalary(hours_rendered):
    rate = 500
    gross_salary = rate * hours_rendered
    return gross_salary

def SalaryDeductions(loan, health_insurance, tax, gross_salary):
    deductions = loan + health_insurance + tax * gross_salary
    return deductions

def NetSalary(gross_salary, deductions):
    net_salary = gross_salary - deductions
    return net_salary

name = input("Enter your name: ")
hours = float(input("Enter hours rendered: "))
loan = float(input("Enter loan: "))
health_Insurance = float(input("Enter health insurance: "))

tax_rate = 0.12
gross_salary = GrossSalary(hours)
tax = gross_salary * tax_rate

deducs = SalaryDeductions(loan, health_Insurance, tax, gross_salary)
net_salary = NetSalary(gross_salary, deducs)

print("Payslip for", name)
print("Gross Salary:", gross_salary)
print("Deductions:", deducts)
print("Net Salary:", net_salary)
