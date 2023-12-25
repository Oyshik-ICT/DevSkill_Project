
def record(personType, info_No, record_list):

    for i in range(info_No):
        print(personType, i+1)
        info = {}
        while True:
            key = input("Enter key(Enter 0 if you want to terminate) : ")
            if key == '0':
                break
            elif key == 'Salary' or key == 'Age' or key == 'Class':
                value = int(input(f"Enter {personType} {key} : "))
            elif key == 'Classes':
                value = list(map(int, input(f"Enter {personType} {key} : ").split()))
            elif key == 'Subjects':
                value = list(map(str, input(f"Enter {personType} {key} : ").split()))
            else:
                value = input(f"Enter {personType} {key} : ")
            info[key] = value

        if personType == "Teacher":
            global Teacher_ID
            Teacher_ID+=1
            info["ID"] = Teacher_ID
            record_list[0].append(info)
        elif personType == "Student":
            global Student_ID
            Student_ID+=1
            info["ID"] = Student_ID
            record_list[1].append(info)
        else:
            global HR_ID
            HR_ID+=1
            info["ID"] = HR_ID
            record_list[2].append(info)
        
        print()



record_list = [[], [], []]
Student_ID, Teacher_ID, HR_ID = 0, 0, 0
while True:
    personType = input("Enter the person type(Enter 0 if you want to terminate) : ")
    if personType == '0':
        break
    info_No = int(input("How many  info you want to record? : "))
    record(personType, info_No, record_list)


print(record_list)