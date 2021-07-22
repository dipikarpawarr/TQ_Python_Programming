class Student:

    # constructor gets invoked at the time of class instantiation
    def __init__(self, sid, sname, steacher):
        print("--- Constructor Invoked --- ")
        self.sid = sid
        self.sname = sname
        self.steacher = steacher
        print("--- Constructor END --- ")

    # instance method
    def studentDetails(self):
        print("\nStudent Details are :-")
        print("Student Id = ", self.sid)
        print("Student Name = ", self.sname)
        print("Teacher = ", self.steacher)

# Class Instantiation
studObject = Student(111,'Dipika','Kirti Jog')
studObject.studentDetails()