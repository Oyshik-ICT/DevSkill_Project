from abc import ABC, abstractclassmethod

class Rules(ABC):

    @abstractclassmethod
    def individualRules(self):
        pass

class School:
        def __init__(self):
            self.record_list = [[], [], []]

        def __record(self,personType, info_No):

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
    
        def total_info(self):
            while True:
                personType = input("Enter the person type(Enter 0 if you want to terminate) : ")
                if personType == '0':
                    break
                info_no = int(input("Enter total number : "))
                self.__record(personType, info_no)
            return len(self.record_list[0]), len(self.record_list[1]), len(self.record_list[2])

class HR(School, Rules):
    def __init__(self):
        super().__init__()
        self.totalStudent, self.totalTeacher, self.totalHR = self.total_info()

    def individualRules(self):
        self.rules = "HR Rules"

    def TeacherSalaryCount(self):
        return self.totalTeacher*10000
    
    def HRSalaryCount(self):
        return self.totalHR*8000
    
    def StudentSalaryCount(self):
        return self.totalStudent*3000
    
    def __total_revenew(self):
        return self.StudentSalaryCount() - (self.TeacherSalaryCount() + self.HRSalaryCount())
    
class Teacher(Rules):
    def __init__(self):
        pass

    def individualRules(self):
        self.rules = "Teachers Rules"

class Student(Rules):
    def __init__(self):
        pass

    def individualRules(self):
        self.rules = "Students Rules"
        

Student_ID, Teacher_ID, HR_ID = 0, 0, 0
hrObj = HR()
