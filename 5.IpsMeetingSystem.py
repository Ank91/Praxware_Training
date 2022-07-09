from time import  sleep

print("\nBook Your Time Slot For IPS Office Meeting in Time Between 1pm to 2pm :\n")

Total_Person = int(input("Enter How many meeting we have Today :-"))
print("\nEnter Your Details\n".center(30))

Meeting_person = []
PersonDetails = []
Purpose = []
Code = []

for x in range(1, Total_Person+1):
    person = input(f"Enter The name of {x} : ")
    Details = input(f" Enter The State and City with Pincode of {person} :")
    Purpose1 = input(f" Enter The Purpose of {person} :")
    print(f" {person} id is : {x}"),
    Meeting_person.append(person)
    PersonDetails.append(Details)
    Purpose.append(Purpose1)
    Code.append(x)
print("Persons's Name = "f" {Meeting_person}")
print("State,City and Pincode = "f"{PersonDetails}")
print("Purpose's = "f"{Purpose}")
print("Id = "f"{Code}")

print("\n Enter Id Between :-"f" 1 To {Total_Person}\n")




class Ips:
    def select_person(self):
      for i in range(0,Total_Person):
        officer = int(input("Enter Id select a Person For meeting :"))
        if officer == 1:
            print("\nSelected person is :",   Meeting_person[0])
            print("Details Of the person :",   PersonDetails[0])
            print("Purpose               :",   Purpose[0])
            Time = int(input("Enter Time limit For Meeting "))
            sleep(Time)
            feedback = input(" Enter the feedback of Meeting | :")
            print(feedback)
        elif officer == 2:
            print("\nSelected person is :", Meeting_person[1])
            print("Details Of the person :", PersonDetails[1])
            print("Purpose               :", Purpose[1])
            Time = int(input("Enter Time limit For Meeting "))
            sleep(Time)
            feedback = input(" Enter the feedback of Meeting | :")
            print(feedback)
        elif officer == 3:
            print("\nSelected person is :", Meeting_person[2])
            print("Details Of the person :", PersonDetails[2])
            print("Purpose               :", Purpose[2])
            Time = int(input("Enter Time limit For Meeting "))
            sleep(Time)
            feedback = input(" Enter the feedback of Meeting | :")
            print(feedback)
        elif officer == 4:
            print("\nSelected person is :", Meeting_person[3])
            print("Details Of the person :", PersonDetails[3])
            print("Purpose               :", Purpose[3])
            Time = int(input("Enter Time limit For Meeting "))
            sleep(Time)
            feedback = input(" Enter the feedback of Meeting | :")
            print(feedback)
        elif officer == 5:
            print("\nSelected person is :", Meeting_person[4])
            print("Details Of the person :", PersonDetails[4])
            print("Purpose               :", Purpose[4])
            time = int(input("Enter Time limit For Meeting "))
            sleep(Time)
            feedback = input(" Enter the feedback of Meeting | :")
            print(feedback)
        else :
            print(" Enter The Id In between 1 to 5")



    def meeting_details(self):
         alldetails = open("AllDetails.txt", "w")
         alldetails.write("\n Today's Meeting Details ||\n")
         alldetails.write("\n Total Taken Meetings       : "f"{Total_Person}\n")
         alldetails.write("\n  ID                  : "f"{Code}\n")
         alldetails.write("\n Name                 : "f"{Meeting_person}\n")
         alldetails.write("\n Details              :"f" {PersonDetails}\n")
         alldetails.write("\n Regarding Discussion : "f"{Purpose}\n")




obj = Ips()
obj.select_person()
obj.meeting_details()

























