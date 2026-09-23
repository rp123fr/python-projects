#to give attribute from one class to another we use inheritance
class Uni_person():
    def make_attendance(self):
        print("attendance marked")   

    def leave_application(self):
        print("sending leave application...")


class Teacher(Uni_person):  #this is called inheritance now the attributes in the class uni_person can be accessed by the class teacher
    def upload_test(self):
        print("test uploaded")

    def leave_application(self): #this is called method overriding to change a method inherited
        print("leave application submitted and waiting for approval...")

class Student(Uni_person): #we cannot inherit a single attribute from a class it all or nothing

    def come_school(self):
        print("going to school")

    def study(self):
        print("studying for test")

    def upload_answer(self):
        print("uploaded answer for the test")

    
class Clerk():
    def upload_data(self):
        print("data uploaded")

teacher1=Teacher()
teacher1.leave_application()