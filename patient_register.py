import queue

def register_patient(patient_queue):
    name = input("Enter patient's name: ")
    patient_queue.put(name)
    print(f"Patient {name} registered")

def remove_patient(patient_queue):
    if patient_queue.empty():
        print("No patients in the queue")
    else:
        name = patient_queue.get()
        print(f"Patient {name} has met the doctor and is removed from the queue")

def display_patient_queue(patient_queue):
    if patient_queue.empty():
        print("No patients in the queue")
    else:
        print("Current patient queue:")
        for i, name in enumerate(list(patient_queue.queue), 1):
            print(f"{i}. {name}")

def main():
    patient_queue = queue.Queue()
    
    while True:
        print("\nDesk Manager System Menu:")
        print("1. Register Patient")
        print("2. Remove Patient after Meeting Doctor")
        print("3. Display Patient Queue")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            register_patient(patient_queue)
        elif choice == '2':
            remove_patient(patient_queue)
        elif choice == '3':
            display_patient_queue(patient_queue)
        elif choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
