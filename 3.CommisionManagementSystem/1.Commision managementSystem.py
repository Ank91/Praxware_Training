SalesMan_Name = input(" Enter Salesman Name  : ")
ID = input(" Enter Salesman Id : ")

"Shop Name  = PraxWare technologies"
"Joining Date = 12-12-2020"
"Current Date = 10-01-2022"
"Salary = 10,000"
Item1 = "Laptop"
Item2 = "Mouse"


Item1 = int(input(" Enter Total Quantity Of Sell Laptop :"))
Item2 = int(input(" Enter Total Quantity Of Sell Mouse :"))

Item1Commission = (Item1*5/100)
Item2Commission = (Item2*5/100)
Total_Commission = (Item1Commission+Item2Commission)

Total_Salary = (10000+Item1Commission+Item2Commission)

print("\n\t\t************Salesman Details***********\n")
print("\t\tSalesman Name                :" ,       SalesMan_Name)
print("\t\tShop Name                       :" ,       "PraxWare Technology")
print("\t\tID                                       :" ,         ID)
print("\t\tJoining Date                      :" ,         "12-12-2020")
print("\t\tCurrent Date                     :" ,         "10-01-2022")

print("\n\t\t**************Sales Report***************\n")
print("\t\tSalary                                   :" ,              "10,000")
print("\t\tLaptop Commission         :" ,               Item1Commission)
print("\t\tMouse Commission          :" ,               Item2Commission)
print("\t\tTotal Commission             :" ,               Total_Commission )
print("\t\tTotal Salary                        :" ,                Total_Salary)



