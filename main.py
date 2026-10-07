# Patient Class
class Patient:
    def __init__(self, patient_id, name, age, gender, diagnosis):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis

    def display_info(self):
        print("\n******** Patient Information **********")
        print(f"ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Diagnosis: {self.diagnosis}")


# Hospital Class
class Hospital:
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print("Patient added successfully")

    def display_patients(self):
        print("\n************** All Patients **********")
        print(f"\n**** {self.hospital_name} ****")

        # Check if there are patients
        if len(self.patients) == 0:
            print("No patients found.")
        else:
            for patient in self.patients:
                patient.display_info()


# Patient Objects
patient1 = Patient(101, "Saidu", 23, "Male", "Poverty")
patient2 = Patient(102, "Abu Turay", 30, "Male", "Malaria")
patient3 = Patient(103, "Yabom Turay", 21, "Female", "Headache")

# Hospital Object
hospitall = Hospital("Donald Clinic")

# Add patients to the hospital using the add_patient method in the Hospital class
hospitall.add_patient(patient1)
hospitall.add_patient(patient2)
hospitall.add_patient(patient3)

# Display all patients
hospitall.display_patients()