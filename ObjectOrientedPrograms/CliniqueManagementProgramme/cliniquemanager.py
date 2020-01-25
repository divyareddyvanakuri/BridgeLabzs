from ManagePatient import Patient
from ManageDoctor import Doctor


def read_patient():
    return{
        "P_Name": input("enter patient name:"),
        "P_ID": input("enter patient S.NO:"),
        "MobileNumber": input("enter patient phonenumber:"),
        "Age": input("enter patient")
    }


def read_doctor():
    return {
        "D_ID": input("enter doctor ID number:"),
        "D_Name": input("enter doctor name:"),
        "Specialization": input("enter doctor specialization:"),
        "Availability": input("enter doctor availability:"),
        "Appoinment_available": input("enter no of patients:")
    }


class CliniqueManager:
    def __init__(self, D_collection=[], P_collection=[]):
        self.D_collection = D_collection
        self.P_collection = P_collection

    def addDoctor(self, doctor=""):
        doctor = Doctor(read_doctor())
        self.D_collection.append(doctor)

    def deleteDoctor(self, index):
        del self.D_collection[index]

    def showDoctors(self):
        for doctor in self.D_collection:
            print(doctor.to_dictionary())

    def addPatient(self, patient):
        patient = Patient(read_patient())
        self.P_collection.append(patient)

    def deletePatient(self,index):
        del self.P_collection[index]

    def showPatients(self):
        for patient in self.P_collection:
            print(patient.to_dictionary())

    def toDict(self):
        doctor_list = []
        for doctor_obj in self.D_collection:
            doctor_list.append(doctor_obj.to_dictionary())
        patient_list = []
        for patient_obj in self.P_collection:
            patient_list.append(patient_obj.to_dictionary())
        return {"Patients": patient_list, "Doctors": doctor_list}
