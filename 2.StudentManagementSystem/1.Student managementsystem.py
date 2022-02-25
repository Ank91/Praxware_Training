College_Name = input("Enter Your College Name : ")

Student_Name = input("Enter Student Name : ")
Sem = int(input("Enter Student Sem : "))
RollNumber = int(input("Enter Student Roll number : "))
EnrollmentNo = int(input("Enter Student Enrollment Number : "))

subject1 = 45
subject2 = 45
subject3 = 10
Total = (subject1+subject2+subject3)
percentage = (Total/3)


print("\n\t\t*******************Marksheet********************\n")
print("\t\tCollege Name           :" ,        College_Name)
print("\t\tStudent Name          :" ,         Student_Name)
print("\t\tSem                            :" ,         Sem)
print("\t\tRollnumber              :" ,         RollNumber)
print("\t\tEnrollmentNumber :" ,         EnrollmentNo)

print("\n\t\t **********Subjects**********Marks***********\n")

print("\t\t                 Subject1   :" ,        subject1)
print("\t\t                 Subject2   :" ,        subject2)
print("\t\t                 Subject3   :" ,        subject3)
print("")
print("\t\tTotal                          :" ,         Total)
print("\t\tPercentage                :" ,         percentage)
