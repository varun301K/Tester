import random
elij = []
def student():
    student_name = input("Enter student name: ")
    grades = float(input("Enter grades of previous year:"))
    income = int(input("Enter family income: "))
    pone_num = int(input("Enter phone number: "))
    if grades >= 5.0:
        if income <= 20000:
            print("The student is eligible ")
            a = random.randint(1,5)
            Student_id = student_name[ :3]+str(a)+"GOV"+str(pone_num)[-3:]
            print("Student ID for the supplies is ", Student_id)
            elij.append(Student_id)
        else:
            print("The student is not eligible")
    else:
        print("The student does not have the required grades")

def main():
    while True:
        student()
        count = input("Do you want to add another student? (yes/no): ")
        if count.lower == "yes":
            # print("The students eligible for the supplies are: ", elij)
            continue
        else:
            break
    print("The students eligible for the supplies are: ", elij)
    student()

if __name__ == "__main__":
    main()