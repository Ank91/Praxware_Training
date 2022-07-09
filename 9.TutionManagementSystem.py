# Tuition  Management  system


ID_Of_Maths_Trainer = "01"
ID_Of_Python_Trainer = "02"
Salary_ForMathsTrainer = 10000
Salary_ForPythonTrainer = 20000

TA = (0.1 * Salary_ForMathsTrainer or  Salary_ForPythonTrainer)     # travel allowance
DA = (0.07 * Salary_ForMathsTrainer or  Salary_ForPythonTrainer)     # dearness allowance
HRA = (0.2 * Salary_ForMathsTrainer or  Salary_ForPythonTrainer)     # house rent allowance
PF = (0.18 * Salary_ForMathsTrainer or  Salary_ForPythonTrainer)      # provident fund
met1 = (Salary_ForMathsTrainer + TA+ DA+ HRA  )
met2 = (Salary_ForPythonTrainer +TA +DA +HRA)
Total1 = ( met1 - PF )
Total2 = (met2 - PF)
Incentive_For_MathsTrainer = 5000
Incentive_For_PythonTrainer = 10000





while True :
    Maths_TrainerName = input("Enter  Maths Trainer Name  : ").upper()
    print(F'This is {Maths_TrainerName} id : 01\n')
    if   Maths_TrainerName == Maths_TrainerName or  Maths_TrainerName == ID_Of_Maths_Trainer :
        Taken_LecturesMaths = int(input("       Enter Number Of Taken Lectures By " f" {Maths_TrainerName} : "))
        Student_Teach_Maths = int(input("       Enter How Many Students Teach By " f" {Maths_TrainerName} : "))
        if Taken_LecturesMaths >= 12 :
            Salary = Total1 + Incentive_For_MathsTrainer
            print("")
            print("|", "*"*10, "Maths Trainer Details", "*"*10, " |")
            print("")
            print("\t\tMaths Trainer Name                        :" ,    Maths_TrainerName )
            print("\t\tID                                                         :" ,      ID_Of_Maths_Trainer)
            print("\t\tTotal Taken Lacture In a Month     :" ,     Taken_LecturesMaths)
            print("\t\tStudent Teach In a Month               :" ,      Student_Teach_Maths )
            print("")
            print("|", "*"*10, "Maths Trainer Salary Details","*"*10, "|")
            print("")
            print("\t\t TA                         :" ,      TA)
            print("\t\tDA                         :" ,       DA)
            print("\t\tHRA                      :" ,       HRA)
            print("\t\tPF                          :" ,        PF)
            print("\t\tSalary                    :" ,        Salary_ForMathsTrainer)
            print("\t\tIncentive              :",         Incentive_For_MathsTrainer)
            print("\t\tNet                        :" ,        met1)
            print("\t\tTotal Salary          :" ,        Salary)
            print(" ="*30)
        elif  Taken_LecturesMaths <  12 :
            Salary = Total1 - 2000
            print("")
            print("|", "*" * 10, "Maths Trainer Details", "*" * 10, " |")
            print("")
            print("\t\tMaths Trainer Name                        :", Maths_TrainerName)
            print("\t\tID                                                         :", ID_Of_Maths_Trainer)
            print("\t\tTotal Taken Lacture In a Month     :", Taken_LecturesMaths)
            print("\t\tStudent Teach In a Month               :", Student_Teach_Maths)
            print("")
            print("|", "*" * 10, "Maths Trainer Salary Details", "*" * 10, "|")
            print("")
            print("\t\t TA                         :", TA)
            print("\t\tDA                         :", DA)
            print("\t\tHRA                      :", HRA)
            print("\t\tPF                          :", PF)
            print("\t\tSalary                    :", Salary_ForMathsTrainer)
            print("\t\tNet                        :", met1)
            print("\t\tCut In Salary        :", -2000)
            print("\t\tTotal Salary          :", Salary)
            print(" =" * 30)
    else:
            print("Enter The Correct Number ! ! ")
            break


#Python Trainer

    Python_Trainer_Name = input("Enter Python Trainer Name  : ").upper()
    print(F'This is {Python_Trainer_Name} id : 02\n')
    if     Python_Trainer_Name  == Python_Trainer_Name or  Python_Trainer_Name == ID_Of_Python_Trainer:
            Taken_Lectures_Python = int(input("       Enter Number Of Taken Lactures By " f" {Python_Trainer_Name} : "))
            Student_Teach_Python   = int(input("       Enter How Many Students Teach By " f" {Python_Trainer_Name} : "))
    if     Taken_Lectures_Python >= 16:
            Salary = Total2 + Incentive_For_PythonTrainer
            print("")
            print("|", "*"*10, "Python Trainer Details", "*"*10, " |")
            print("")
            print("\t\tPython Trainer Name                       :" ,     Python_Trainer_Name )
            print("\t\tID                                                          :" ,     ID_Of_Python_Trainer)
            print("\t\tTotal Taken Lecture In a Month      :" ,     Taken_Lectures_Python)
            print("\t\tStudent Teach In a Month                :" ,      Student_Teach_Python)
            print("")
            print("|", "*"*10, "Python Trainer Salary Details","*"*10, "|")
            print("\t\t TA                         :" ,      TA)
            print("\t\tDA                         :" ,       DA)
            print("\t\tHRA                      :" ,       HRA)
            print("\t\tPF                          :" ,        PF)
            print("\t\tSalary                    :" ,        Salary_ForPythonTrainer)
            print("\t\tIncentive              :" ,        Incentive_For_PythonTrainer)
            print("\t\tNet                        :" ,        met2)
            print("\t\tTotal Salary          :" ,        Salary)
    elif Taken_Lectures_Python < 16:
        Salary = Total2 - 2000
        print("")
        print("|", "*" * 10, "Python Trainer Details", "*" * 10, " |")
        print("")
        print("\t\tPythonTrainer Name                        :", Python_Trainer_Name)
        print("\t\tID                                                         :", ID_Of_Python_Trainer)
        print("\t\tTotal Taken Lecture In a Month     :", Taken_Lectures_Python)
        print("\t\tStudent Teach In a Month               :", Student_Teach_Python)
        print("")
        print("|", "*" * 10, "Python Trainer Salary Details", "*" * 10, "|")
        print("")
        print("\t\t TA                         :", TA)
        print("\t\tDA                         :", DA)
        print("\t\tHRA                      :", HRA)
        print("\t\tPF                          :", PF)
        print("\t\tSalary                    :", Salary_ForPythonTrainer)
        print("\t\tNet                        :", met2)
        print("\t\tCut In Salary        :", -2000)
        print("\t\tTotal Salary          :", Salary)
        print(" =" * 30)
    else:
        print("Enter The Correct Number ! ! ")
        break

