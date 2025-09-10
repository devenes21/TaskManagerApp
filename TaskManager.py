import json
from datetime import datetime

path = "/home/sotiris/Desktop/Python/TaskManagerApp/tasks.json"


#ΧΡΕΙΑΖΕΣΑΙ ΠΑΝΤΟΥ ΤΟ load_tasks ΚΑΙ save_tasks

def load_tasks():
    try:
        with open(path, "r", encoding="utf-8") as jsonfile:             # Ανοίγουμε το αρχείο JSON για ανάγνωση
            content = jsonfile.read().strip()                           # Διαβάζουμε το περιεχόμενο του αρχείου και αφαιρούμε κενά
            if not content:                                             # Αν το αρχείο είναι άδειο
                return []                                               # Επιστρέφουμε μια κενή λίστα
            return json.loads(content)                                  # Φορτώνουμε τις εργασίες από το αρχείο JSON
    except (FileNotFoundError, json.JSONDecodeError):                   # Αν το αρχείο δεν υπάρχει ή είναι χαλασμένο
        return []                                                       

def save_tasks(tasks):                                                  # Αποθηκεύουμε τις εργασίες στο αρχείο JSON
    with open(path, "w", encoding="utf-8") as jsonfile:                 # Ανοίγουμε το αρχείο JSON για εγγραφή
        json.dump(tasks, jsonfile, ensure_ascii=False, indent=4)        # Αποθηκεύουμε τις εργασίες στο αρχείο JSON


def add_task():

    title = input("Εισάγετε τον τίτλο της εργασίας: ")
    description = input("Εισάγετε την περιγραφή της εργασίας: ")
    # Validate deadline format
    while True:
        deadline = input("Εισάγετε την προθεσμία της εργασίας (dd/mm/yyyy): ")
        try:
            datetime.strptime(deadline, "%d/%m/%Y")
            break
        except ValueError:
            print("Λάθος μορφή ημερομηνίας. Παρακαλώ εισάγετε σε μορφή dd/mm/yyyy.")
    # Validate completed input
    while True:
        completed = input("Έχει ολοκληρωθεί? (ναι/όχι): ").lower()
        if completed in ['ναι', 'όχι']:
            break
        else:
            print("Παρακαλώ εισάγετε 'ναι' ή 'όχι'.")

    tasks = load_tasks()                                            # Φορτώνουμε τις υπάρχουσες εργασίες
    new_task = { 
        "title": title,
        "description": description,
        "deadline": deadline,
        "completed": completed
    }
    tasks.append(new_task)                                          # Προσθέτουμε τη νέα εργασία στη λίστα
    save_tasks(tasks)                                               # Αποθηκεύουμε τις εργασίες πίσω στο αρχείο JSON

    print("Η εργασία προστέθηκε επιτυχώς!")



def remove_task():
    print("Ποια εργασία θέλετε να αφαιρέσετε;")
    flag = True
    while flag:
        answer = input("Εισάγετε το όνομα της εργασίας: ")
        tasks = load_tasks()
        for i, task in enumerate(tasks):
            if task.get("title") == answer:
                tasks.pop(i)  # Αφαιρούμε την εργασία από τη λίστα
                save_tasks(tasks)
                print("Η εργασία αφαιρέθηκε επιτυχώς!")
                flag = False
                again = input("Θέλετε να αφαιρέσετε άλλη εργασία; (ναι/όχι): ").lower()
                if again == 'ναι':
                    flag = True
                break
        else:
            print("Δεν βρέθηκε εργασία με αυτόν τον τίτλο.")




def complete_task():
    print("Ποια εργασία θέλετε να σημειώσετε ως ολοκληρωμένη;")
    flag = True
    while flag:
        answer = input("Εισάγετε το όνομα της εργασίας: ")
        tasks = load_tasks()
        for task in tasks:
            if task.get("title") == answer:
                task["completed"] = "ναι"  # Σημειώνουμε την εργασία ως ολοκληρωμένη
                save_tasks(tasks)
                print("Η εργασία σημειώθηκε ως ολοκληρωμένη!")
                flag = False
                again = input("Θέλετε να σημειώσετε άλλη εργασία ως ολοκληρωμένη; (ναι/όχι): ")
                if again == 'ναι':
                    flag = True
                break
        else:
            print("Δεν βρέθηκε εργασία με αυτόν τον τίτλο.")


def show_tasks():
    tasks = load_tasks()  # φορτώνουμε όλες τις εργασίες
    flag1 = True
    while flag1:
        if tasks == []:
            print("Δεν υπάρχουν εργασίες.")
            flag1 = False
            return

    today = date.today()
    for i, task in enumerate(tasks, start=1):
        deadline_date = datetime.strptime(task['deadline'], "%d/%m/%Y").date() # Μετατροπή της προθεσμίας σε αντικείμενο date
        overdue = deadline_date < today and task['completed'] == 'όχι'


    print("\n--- Λίστα Εργασιών ---")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. Τίτλος: {task['title']}")
        print(f"   Περιγραφή: {task['description']}")
        print(f"   Προθεσμία: {task['deadline']}")
        print(f"   Ολοκληρωμένο: {task['completed']}")
        if overdue:
            print("   Προσοχή: Η προθεσμία έχει περάσει και η εργασία δεν έχει ολοκληρωθεί!")
        print("----------------------")


def search():
    tasks = load_tasks()
    search_term = input("Εισάγετε τον τίτλο της εργασίας: ")
    for i, task in enumerate(tasks, start=1):
        if search_term.lower() in task['title'].lower():
            print(f"{i}. Τίτλος: {task['title']}")
            print(f"   Περιγραφή: {task['description']}")
            print(f"   Προθεσμία: {task['deadline']}")
            print(f"   Ολοκληρωμένο: {task['completed']}")
            if overdue:
                print("   Προσοχή: Η προθεσμία έχει περάσει και η εργασία δεν έχει ολοκληρωθεί!")
            print("----------------------")
            break


#Menu
flag = True
while flag:
    print("Καλώς ήρθατε στο Task Manager!")
    print("1. Προσθήκη εργασίας")
    print("2. Αφαίρεση εργασίας")
    print("3. Προβολή όλων των εργασιών")
    print("4. Σημείωση εργασίας ως ολοκληρωμένη")
    print("5. Αναζήτηση εργασίας")
    print("6. Έξοδος")
    choice = int(input("Επιλέξτε μια επιλογή: "))

    if choice == 1:
        add_task()
    elif choice == 2:
        remove_task()
    elif choice == 3:
        show_tasks()  #terminal show
    elif choice == 4:
        complete_task()
    elif choice == 5:
        search()
    elif choice == 6:
        print("Έξοδος από το πρόγραμμα.")
        flag = False