
def record(personType, info_No):
    info_list = []

    for i in range(info_No):
        info = {}
        print(f"Please add {personType}  info")
        info["name"] = input("Enter  name : ")
        info["age"] = int(input("Enter age : "))
        if personType == "Student":
            info["father_name"] = input("Enter father_name : ")
            info["class"] = int(input("Enter class : "))
            info["subjects"] = list(map(str, input("Enter the subjects : ").split()))
        if personType == "Teacher" or personType == "HR":
            info["dept"] = personType
            info["salary"] = int(input("Enter salary : "))
        if personType == "Teacher":
            info["classes"] = list(map(str, input("Enter classes : ").split()))
            info["subjects"] = list(map(str, input("Enter the subjects : ").split()))

        info_list.append(info)
        print()
    return info_list

info_No = int(input("How many  info you want to record? : "))
personType = input("Enter the person type : ")
record_list = record(personType, info_No)


print(record_list)