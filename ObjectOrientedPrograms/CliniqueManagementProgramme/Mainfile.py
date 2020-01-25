from cliniquemanager import CliniqueManager
from filesystem import FileSystem
while True:
    filesystem_object = FileSystem()
    cliniqueManager_object = CliniqueManager()
    print("________CliniqueManagement Main-Menu_______")
    print(" 1.Manage Doctors"), print(" 2.Manage patients"), print(
        " 3.Take Appointment"), print(" 4.Quit")
    manager = int(input("enter option:"))
    if manager == 1:
        cliniqueManager_object = filesystem_object.read_file()
        cliniqueManager_object.deleteDoctor(1)
        filesystem_object.save_file(cliniqueManager_object)
        print("___Sub-Menu___"), print(" 1.AddDoctor"), print(
            " 2.updateDoctot"), print(" 3.Delect Doctor")
        print(" 4.serachDoctor"), print(" 5.PrintDoctors")
    elif manager == 2:
        print("___Sub-Menu___"), print(" 1.AddPatient"), print(
            " 2.updatePatient"), print(" 3.Delect patient")
        print(" 4.serachpatient"), print(" 5.Printpatients")

    elif manager == 3:
        print("Take appointment")
    elif manager == 4:
        break
    else:
        print("wrong choice")
