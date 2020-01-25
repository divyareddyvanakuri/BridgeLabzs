class Patient:
    def __init__(self, p_dict={}):
        self.P_Name = p_dict['P_Name']
        self.P_SNO = p_dict['P_ID']
        self.MobileNumber = p_dict['MobileNumber']
        self.Age = p_dict['Age']

    def getPatientName(self):
        return self.P_Name

    def getPatientSerialNumber(self):
        return self.P_SNO

    def getPatientMobileNumber(self):
        return self.MobileNumber

    def getPatientAge(self):
        return self.Age

    def to_dictionary(self):
        return{
            "P_Name": self.P_Name,
            "P_ID": self.P_SNO,
            "MobileNumber": self.MobileNumber,
            "Age": self.Age
        }
