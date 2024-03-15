from queue import Queue

patient_queue = Queue()
patient_choice = ''

print(f"Desk Manager - Patient Registration and Appointment System")
print("1. Register Patient")
print("2. Remove Patient after meeting the Doctor")
print("3. Display patient queue")
print("4. Exit")

while patient_choice != '4':
    patient_choice = input("Enter your choice (Just enter the option number): ")

    if patient_choice == '1':
        name = input("Enter your patient's name: ")
        patient_queue.put(name)
        print("Patient registered.")
    
    elif patient_choice == '2':
        if patient_queue.empty():
            print("No patients in the queue.")
        else:
            removed_patient = patient_queue.get()
            print(f"{removed_patient} has met the doctor and been removed from the queue.")

    elif patient_choice == '3':
        if patient_queue.empty():
            print("No patients in the queue.")
        else:
            print("Current patient queue:")
            for index, patient in enumerate(patient_queue.queue):
                print(f"{index+1}. {patient}")

    elif patient_choice == '4':
        print("Exiting program.")

    else:
        print("Invalid choice. Please enter a valid option.")
