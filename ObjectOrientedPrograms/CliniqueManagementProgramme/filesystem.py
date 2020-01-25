import json
from ManageDoctor import Doctor
from ManagePatient import Patient
from cliniquemanager import CliniqueManager


class FileSystem:
    def read_file(self):
        doctors = []
        patients = []
        with open("CliniqueManagementProgrammefile.json", "r") as readFile:
            data = json.load(readFile)

            for doctor in data['Doctors']:
                doctors.append(Doctor(doctor))

            for patient in data['Patients']:
                patients.append(Patient(patient))

            cliniquemanager_object = CliniqueManager(doctors, patients)

        return cliniquemanager_object

    def save_file(self, cliniquemanager_object):
        with open("CliniqueManagementProgrammefile.json", "w") as saveFile:
            json.dump(cliniquemanager_object.toDict(), saveFile, indent=2)
