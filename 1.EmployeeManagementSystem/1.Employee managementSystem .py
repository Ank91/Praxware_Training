Company_Name = input("Enter Your Company Name : ")

Name = input("Enter Employee Name : ")
ID = input("Enter Employee Id : ")
Position = input("Enter Employee Position : ")
Mobile = int(input("Mobile Number : "))
Address = input("Enter Employee Address : ")
Email_id = input("Enter Employee  Email Id : ")
Salary = int(input(" Enter Employee Salary : "))

TA = (0.02 * Salary)     # travel allowance
DA = (0.05 * Salary)     # dearness allowance
HRA = (0.2 * Salary)     # house rent allowance
PF = (0.18 * Salary)      # provident fund
met = (Salary + TA+ DA+ HRA)
Total = ( met - PF )

print("\n\t\t*******************Salary Slip********************\n")
print("\t\tCompany Name   :" ,    Company_Name )
print("\t\tEmployee Name  :" ,     Name )
print("\t\tEmployee Id         :" ,      ID )
print("\t\tPosition                 :" ,      Position )
print("\t\tMobile                   :" ,      Mobile )
print("\t\tEmail Id                :" ,      Email_id)
print("\t\tAddress               :" ,      Address)
print("\t\t TA                         :" ,      TA)
print("\t\tDA                         :" ,       DA)
print("\t\tHRA                      :" ,       HRA)
print("\t\tPF                          :" ,        PF)
print("\t\tNet                        :" ,        met)
print("\t\tSalary                    :" ,        Salary)
print("\t\tTotal Salary          :" ,        Total)