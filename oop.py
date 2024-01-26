class HR():
    def __init__(self, data) -> None:
        self.__hr_data = data
        self.hr_name = data["name"]

    def salaryCount(self, totalteacher):
        return totalteacher*10000
    
    def feesCount(self, totalstudent):
        return totalstudent*5000
    
    def total_revenew(self, a, b):
        return self.salaryCount(a) - self.feesCount(b)
    
    def record(self,personType, info_No):
        self.record_list = [[], [], []]

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
                self.record_list[1].append(info)
            elif personType == "Student":
                global Student_ID
                Student_ID+=1
                info["ID"] = Student_ID
                self.record_list[0].append(info)
            else:
                global HR_ID
                HR_ID+=1
                info["ID"] = HR_ID
                self.record_list[2].append(info)
        
        return self.record_list
    
    def countTotal(self):
        self.totalstudent = len(self.record_list[0])
        self.totalteacher = len(self.record_list[1])
        self. totalhr = len(self.record_list[2])

        return 




class Teacher():
    
    def __init__(self, data) -> None:
        self.__teacher_data = data
        self.teacher_name = data["name"]
        self.teacher_contact_info = data["contact_info"]
        self.teacher_subjects = data["subjects"]

class Student():
    
    def __init__(self, data) -> None:
        self.student_data = data

class School(HR, Teacher, Student):
    
    def __init__(self):
        rules = """
        1. Respect all teachers and staff members.
        2. Follow the dress code at all times.
        3. No bullying or harassment will be tolerated.
        4. Cell phones must be turned off during class.
        5. Attend all classes regularly and be on time.
        6. No cheating or plagiarism is allowed.
        7. Keep the school premises clean and tidy.
        8. Use appropriate language and behavior.
        9. No unauthorized use of school property.
        10. Follow safety guidelines in labs and workshops.
        """
        print(rules)



    