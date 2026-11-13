#Student Management System
STUDENT=[]
#Dictionary 1st
Department={
    "BCA":{"subject1":"Python",
           "subject2":"Java",
           "subject3":"C++"
           },
    "BBA":{
           "subject1":"Business Management",
           "subject2":"Marketing",
           "subject3":"Finance"
           }    
}
#Dictionary 2nd
Marks={
    "BCA":{
        "subject1":{"Max_Marks":100},
        "subject2":{"Max_Marks":100},
        "subject3":{"Max_Marks":100}
        },
    "BBA":{
        "subject1":{"Max_Marks":100},
        "subject2":{"Max_Marks":100},
        "subject3":{"Max_Marks":100}
        }
    }

#1.Add student with all detail
def add_Student():
    while True:
        name=input("Enter Student Name:")
        if name=="":
            print("Name cannot be empty")
        elif name.isdigit():
            print("Name cannot be a number")
        else:
            break
    while True:
        Branch=input("Enter Student Branch:").upper()
        if Branch not in Department:
            print("Invaild Branch")
        else:
            subjects=Department[Branch]
            max_marks = Marks[Branch]
            student_marks = {}
            print("Subjects:")
            for subject in subjects:
                print(subject,":",subjects[subject])
                while True:
                    obtained_marks = input("Enter obtained marks: ")

                    if not obtained_marks.isdigit():
                        print("Marks must be a number")
                    elif int(obtained_marks) > max_marks[subject]["Max_Marks"]:
                        print("Marks cannot be greater than maximum marks")
                    else:
                        obtained_marks = int(obtained_marks)
                        break

                student_marks[subject] = obtained_marks
            break   
    Semester=input("Enter Student Semester:")
    print(f"Branch: {Branch}, Semester: {Semester}")
    while True:
        Roll_No=input("Enter Student Roll No:")
        if not Roll_No.isdigit():
            print("Roll No cannot be a string")
        elif int(Roll_No)<=0:
            print("Roll No. cannot be zero")

        else:
            Roll_No=int(Roll_No)
            duplicate=False
            for student in STUDENT:
                if student["Roll_No"]==Roll_No:
                    duplicate=True
                    break
            if duplicate:
                print("This Roll No. is alredy Exist.Enter a different Roll No.")
            else:
                break
    dictionary1={
       "name":name,
       "Branch":Branch,
       "Semester":Semester,
       "Roll_No":Roll_No,
       "Marks":student_marks
       }
    STUDENT.append(dictionary1)
    return 

#2.View student with all detail
def view_Student():
    print("===This is your Student:===")
    if len(STUDENT)==0:
        print("Student list is empty")
    else:
        for s in STUDENT:
            print(f"Name: {s['name']},\nBranch: {s['Branch']},\nSemester: {s['Semester']},\nRoll No: {s['Roll_No']},\nMarks: {s['Marks']}")
 #3.Search student with all detail
def search_Student():
    while True:
        search_Roll=input("Enter Roll No to search: ")
        if not search_Roll.isdigit():
            print("Roll No must be a number. Please enter again.")
            continue
        elif int(search_Roll)<=0:
            print("Roll No cannot be zero or negative. Please enter again.")
            continue
        else:
            search_Roll=int(search_Roll)

        found=False

        for searc in range(len(STUDENT)):

            if STUDENT[searc]["Roll_No"]==search_Roll:

                print(
                    f"Name: {STUDENT[searc]['name']},\n"
                    f"Branch: {STUDENT[searc]['Branch']},\n"
                    f"Semester: {STUDENT[searc]['Semester']},\n"
                    f"Roll No: {STUDENT[searc]['Roll_No']},\n"
                    f"Marks: {STUDENT[searc]['Marks']}"
                )

                found=True
                break
        if found:
            break
        else:
            print("Student not found.")

            again=input(
                "Do you want to search again? (yes/no): "
            ).lower()

            if again=="yes":
                continue
            else:
                break
#4.Update student with all detail
def update_Student():
    while True:
        search_Roll=input("Enter Roll No to update: ")

        if not search_Roll.isdigit():
            print("Roll No must be a number. Please enter again.")
            continue

        elif int(search_Roll)<=0:
            print("Roll No cannot be zero or negative. Please enter again.")
            continue

        else:
            search_Roll=int(search_Roll)
            break

    found=False
    for u in range(len(STUDENT)):

        if STUDENT[u]["Roll_No"]==search_Roll:

            found=True

            print("Student found. Enter new details:")

            choices=input(
                "1.Name 2.Branch 3.Semester 4.Roll No 5.Marks\n"
                "Enter choice: "
            )

# NAME 
            if choices=="1":
                while True:
                    new_name=input("Enter new name: ")
                    if new_name=="":
                        print("Name cannot be empty")
                    elif new_name.isdigit():
                        print("Name cannot be a number")
                    else:
                        STUDENT[u]["name"]=new_name
                        print("Name updated Successfully")
                        break
# BRANCH 
            elif choices=="2":
                while True:
                    new_branch=input("Enter new branch: ").upper()
                    if new_branch in Department:
                        STUDENT[u]["Branch"]=new_branch
                        print("Branch updated Successfully")
                        break
                    else:
                        print("Invalid Branch")
#SEMESTER 
            elif choices=="3":
                while True:
                    new_sem=input("Enter new Semester: ")
                    if not new_sem.isdigit():
                        print("Semester must be a number")

                    elif int(new_sem)<=0:
                        print("Semester cannot be zero or negative")
                    else:
                        STUDENT[u]["Semester"]=new_sem
                        print("Semester Updated Successfully")
                        break
#  ROLL NO 
            elif choices=="4":
                while True:
                    new_roll=input("Enter new Roll No: ")
                    if not new_roll.isdigit():
                        print(
                            "Roll No must be a number. "
                            "Please enter again."
                        )
                        continue
                    elif int(new_roll)<=0:
                        print(
                            "Roll No cannot be zero or negative. "
                            "Please enter again."
                        )
                        continue
                    new_roll=int(new_roll)
                    duplicate=False
                    for student in STUDENT:
                        if student["Roll_No"]==new_roll:
                            duplicate=True
                            break
                    if duplicate:
                        print(
                            "This Roll No already exists. "
                            "Please enter a different Roll No."
                        )
                    else:
                        STUDENT[u]["Roll_No"]=new_roll
                        print("Roll No updated Successfully")
                        break
#  MARKS 
            elif choices=="5":
                while True:
                    subject=input("Enter subject: ").lower()
                    if subject not in STUDENT[u]["Marks"]:
                        print(
                            "Subject not found. "
                            "Please enter a valid subject."
                        )
                    else:
                        while True:
                            new_marks=input("Enter new marks: ")
                            if not new_marks.isdigit():
                                print("Marks must be a number")
                            elif int(new_marks)>100:
                                print(
                                    "Marks cannot be greater than "
                                    "maximum marks"
                                )
                            else:
                                STUDENT[u]["Marks"][subject]=int(new_marks)
                                print(
                                    "Marks updated Successfully"
                                )
                                break
                        break
            else:
                print("Invalid choice.")
            break
    if found==False:
        print("Student not found.")

        again=input(
            "Do you want to try again? (yes/no): "
        ).lower()
        if again=="yes":
            update_Student()
#5.Delete student with all detail
def delete_Student():
    while True:
        search_Roll=input("Enter Roll No to delete: ")
        if not search_Roll.isdigit():
            print(
                "Roll No must be a number. "
                "Please enter again."
            )
            continue
        elif int(search_Roll)<=0:
            print(
                "Roll No cannot be zero or negative. "
                "Please enter again."
            )
            continue
        else:

            search_Roll=int(search_Roll)
        found=False
        for d in range(len(STUDENT)):
            if STUDENT[d]["Roll_No"]==search_Roll:
                del STUDENT[d]
                found=True
                print("Student deleted successfully")
                break
        if found:
            break
        else:
            print("Student not found.")
            again=input(
                "Do you want to try again? (yes/no): "
            ).lower()
            if again=="yes":
                continue
            else:
                break
#6.Calculate Result
def cal_Student():
    while True:
        search_Roll=input(
            "Enter Roll No to calculate result: "
        )
        if not search_Roll.isdigit():
            print(
                "Roll No must be a number. "
                "Please enter again."
            )
            continue
        elif int(search_Roll)<=0:
            print(
                "Roll No cannot be zero or negative. "
                "Please enter again."
            )
            continue
        else:
            search_Roll=int(search_Roll)
        found=False
        for c in range(len(STUDENT)):
            if STUDENT[c]["Roll_No"]==search_Roll:
                found=True
                branch=STUDENT[c]["Branch"]
                total_obtained=0
                total_max=0
                print("\n===== RESULT =====")
                print(
                    "Name:",
                    STUDENT[c]["name"]
                )
                print(
                    "Roll No:",
                    STUDENT[c]["Roll_No"]
                )
                print(
                    "Branch:",
                    branch
                )
                print(
                    "Semester:",
                    STUDENT[c]["Semester"]
                )
                for subject in STUDENT[c]["Marks"]:
                    obtained=STUDENT[c]["Marks"][subject]
                    maximum=Marks[branch][subject]["Max_Marks"]
                    print(
                        subject,
                        ":",
                        obtained,
                        "/",
                        maximum
                    )
                    total_obtained=total_obtained+obtained
                    total_max=total_max+maximum
                percentage=(
                    total_obtained/total_max
                )*100
                print(
                    "Total Marks:",
                    total_obtained,
                    "/",
                    total_max
                )
                print(
                    "Percentage:",
                    percentage,
                    "%"
                )
                break
        if found:
            break
        else:
            print("Student not found.")
            again=input(
                "Do you want to try again? (yes/no): "
            ).lower()
            if again=="yes":
                continue
            else:
                break
#7.Top Student
def top_Student():
    while True:
        print("\n===== TOP STUDENT =====")
        print("1. Branch-wise Top 3")
        print("2. College-wise Top 3")

        choice=input("Enter choice: ")

# BRANCH-WISE 

        if choice=="1":
# Enter valid Branch
            while True:
                Branch=input("Enter Branch: ").upper()

                if Branch not in Department:
                    print("Invalid Branch. Please enter again.")

                else:
                    break
 # Enter existing Semester for this Branch
            while True:
                Semester=input("Enter Semester: ")
                if not Semester.isdigit():
                    print("Semester must be a number. Please enter again.")
                    continue
                elif int(Semester)<=0:
                    print("Semester cannot be zero or negative. Please enter again.")
                    continue

                semester_exists=False

                for student in STUDENT:
                    if student["Branch"]==Branch and student["Semester"]==Semester:
                        semester_exists=True
                        break

                if semester_exists:
                    break

                else:
                    print("This Semester does not exist for this Branch.")
                    print("Please enter again.")

  #  COLLEGE-WISE 
        elif choice=="2":
# Enter existing Semester
            while True:
                Semester=input("Enter Semester: ")
                if not Semester.isdigit():
                    print("Semester must be a number. Please enter again.")
                    continue
                elif int(Semester)<=0:
                    print("Semester cannot be zero or negative. Please enter again.")
                    continue

                semester_exists=False
                for student in STUDENT:
                    if student["Semester"]==Semester:
                        semester_exists=True
                        break

                if semester_exists:
                    break

                else:
                    print("This Semester does not exist.")
                    print("Please enter again.")
# WRONG CHOICE 
        else:
            print("Invalid choice. Please enter 1 or 2.")
            continue
# SELECT STUDENTS 
        selected_students=[]
        for student in STUDENT:
            if choice=="1":
                if student["Branch"]==Branch and student["Semester"]==Semester:
                    selected_students.append(student)

            elif choice=="2":

                if student["Semester"]==Semester:
                    selected_students.append(student)
# NO STUDENT CHECK 
        if len(selected_students)==0:
            print("No student found.")

            again=input("Do you want to try again? (yes/no): ").lower()

            if again=="yes":
                continue
            else:
                return
#  CALCULATE PERCENTAGE 
        student_percentage=[]
        for student in selected_students:
            branch=student["Branch"]
            total_obtained=0
            total_max=0

            for subject in student["Marks"]:
                obtained=student["Marks"][subject]
                maximum=Marks[branch][subject]["Max_Marks"]
                total_obtained=total_obtained+obtained
                total_max=total_max+maximum
            percentage=(total_obtained/total_max)*100

            student_percentage.append({
                "name":student["name"],
                "Roll_No":student["Roll_No"],
                "Branch":student["Branch"],
                "Semester":student["Semester"],
                "Percentage":percentage
            })
#  GET DIFFERENT PERCENTAGES 
        percentages=[]
        for student in student_percentage:
            if student["Percentage"] not in percentages:
                percentages.append(student["Percentage"])
# Highest percentage first
        percentages.sort(reverse=True)
# DISPLAY TOP 3
        print("\n===== TOP 3 STUDENTS =====")
        position=1
        for percentage in percentages:
            if position>3:
                break
            for student in student_percentage:
                if student["Percentage"]==percentage:
                    print(
                        position,
                        "Position:",
                        "Name:",student["name"],
                        "| Roll No:",student["Roll_No"],
                        "| Branch:",student["Branch"],
                        "| Semester:",student["Semester"],
                        "| Percentage:",student["Percentage"],
                        "%"
                    )
            position=position+1
        break
while True:
    print("1.Add Student")
    print("2.View Student")
    print("3.Search Student")
    print("4.Update Student")
    print("5.Delete Student")
    print("6.Calculate Result")
    print("7.Top Student")
    print("8.Exit")
    choice=int(input("Enter your choice: "))    
    if choice==1:
        add_Student()
    elif choice==2:
        view_Student()
    elif choice==3:
        search_Student()
    elif choice==4:
        update_Student()
    elif choice==5:
        delete_Student()
    elif choice==6:
        cal_Student()
    elif choice==7:
        top_Student()
    elif choice==8:
        break   
    else:
        print("Invalid choice, please try again.")