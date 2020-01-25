class Doctor:
    def __init__(self, D_dict={}):
        self.D_IDNO = D_dict['D_ID']
        self.D_Name = D_dict['D_Name']
        self.Specialization = D_dict['Specialization']
        self.Availability = D_dict['Availability']
        self.NoOfPatients = D_dict['Appoinment_available']

    def getDoctorName(self):
        return self.D_Name

    def getDoctorIdNumber(self):
        return self.D_IDNO

    def getDoctorSpecialization(self):
        return self.Specialization

    def getDoctorAvailbility(self):
        return self.Availability

    def getNoOfPatients(self):
        return self.NoOfPatients

    def to_dictionary(self):
        return{
            "D_Name": self.D_Name,
            "D_ID": self.D_IDNO,
            "Specialization": self.Specialization,
            "Availability": self.Availability,
            "Appoinment_available": self.NoOfPatients
        }
