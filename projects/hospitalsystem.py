class Patient():
    def __init__(self,patient_id,name,bill=0):
        self.p_id=patient_id
        self.p_name=name
        self.__bill=bill
    def add_charge(self,amount):
        self.__bill+=amount 
        return self.__bill
    def make_payment(self,amount):
        self.__bill-=amount
        return self.__bill
    def get_bill(self):
        print(f"your bill is: {self.__bill}")      

class Doctor():
    def __init__(self,doctor_id,name,speciality):
        self.d_id=doctor_id
        self.d_name=name
        self.d_speciality=speciality
    def diagnose(self,patient):
        pass 

class Surgeon(Doctor):
    def diagnose(self, patient):
       print("recommend surgery")
       patient.add_charge(500000)
               

class Physician(Doctor):
    def diagnose(self, patient):
        print("prescribes medication")
        patient.add_charge(500)

class Hospital():
    def __init__(self):
        self.patients = []
        self.doctors = []

    def register_patient(self, patient):
        self.patients.append(patient)

    def register_doctor(self, doctor):
        self.doctors.append(doctor)

    def find_patient(self,patient_id):
        for p in self.patients:
            if p.p_id==patient_id:
             return p
        return None

    def find_doctor(self,doctor_id):
        for d in self.doctors:
            if d.d_id==doctor_id:
             return d
        return None

    def book_appointment(self, patient_id, doctor_id):
     patient = self.find_patient(patient_id)
     doctor = self.find_doctor(doctor_id)

     if patient is None or doctor is None:
        print("Patient or Doctor not found.")
        return

     doctor.diagnose(patient)



hospital = Hospital()

p1 = Patient(1, "Ravi")
doc1 = Surgeon(101, "Dr. Mehta", "Cardiology")

hospital.register_patient(p1)
hospital.register_doctor(doc1)

hospital.book_appointment(1, 101)
p1.get_bill()     










