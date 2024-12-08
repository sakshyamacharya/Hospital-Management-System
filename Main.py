
from Admin import Admin
from Doctor import Doctor
from Patient import Patient
def main():
    """
    the main function to be ran when the program runs
    """
   
    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC')]
    discharged_patients = []
    admin.write_patientRecords(patients)
    patients_list=admin.read_patientRecords()
      
    while True:
        if admin.login():
            running = True
            break
        else:
            print('Incorrect username or password.')

    while running:
        
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin detais')
        print(' 6- Get Management Report')
        print(' 7- Quit')

     
        op = input('Option: ')

        if op == '1':
          admin.doctor_management(doctors)
          

        elif op == '2':
         

            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()

                if op == 'yes' or op == 'y':
                   
                    admin.discharge(patients,discharged_patients)

                elif op == 'no' or op == 'n':
                    break

               
                else:
                    print('Please answer by yes or no.')
        
        elif op == '3':
          
            
            admin.view_discharge(discharged_patients)

        elif op == '4':
         
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
          
            admin.update_details()

        elif op == '6':
            
            admin.get_management_report(doctors,patients)
        
        elif op=='7':
            quit()

        else:
          
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()