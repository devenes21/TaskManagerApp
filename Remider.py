import json
from datetime import datetime, timedelta
import schedule
import time
import smtplib
from email.message import EmailMessage\


path = "/home/sotiris/Desktop/Python/TaskManagerApp/tasks.json"

email_address = "sotirisdev7@gmail.com"
email_password = "emailsender21"  # Use an app password for better security
to_email = "sotirisdevenes@yahoo.com"

def load_tasks():
    try:
        with open(path, "r", encoding="utf-8") as jsonfile:             # Ανοίγουμε το αρχείο JSON για ανάγνωση
            content = jsonfile.read().strip()                           # Διαβάζουμε το περιεχόμενο του αρχείου και αφαιρούμε κενά
            if not content:                                             # Αν το αρχείο είναι άδειο
                return []                                               # Επιστρέφουμε μια κενή λίστα
            return json.loads(content)                                  # Φορτώνουμε τις εργασίες από το αρχείο JSON
    except (FileNotFoundError, json.JSONDecodeError):                   # Αν το αρχείο δεν υπάρχει ή είναι χαλασμένο
        return []

def send_email(subject, body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = to_email
    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
        print("Email sent successfully.")

def check_deadlines():
    tasks = load_tasks()
    now = datetime.now()
    for task in tasks:
        if task['completed'].lower() == 'όχι':                                                                      #Eλέγχουμε μόνο τις μη ολοκληρωμένες εργασίες
            try:
                deadline_date = datetime.strptime(task['deadline'], "%d/%m/%Y").date()                              # Μετατρέπουμε την προθεσμία σε αντικείμενο datetime
                if deadline_date - datetime.now().date()  <= timedelta(days=3):                                     # Έλεγχος αν η προθεσμία είναι σε 3 μέρες
                    subject = f"Υπενθύμιση: Εργασία '{task['title']}' με προθεσμία {task['deadline']}"
                    body = f"Η εργασία '{task['title']}' έχει προθεσμία στις {task['deadline']}.\n\nΠεριγραφή: {task['description']}"
                    send_email(subject, body)
            except ValueError:
                print(f"Invalid date format for task '{task['title']}': {task['deadline']}")


schedule.every().day.at("time").do(check_deadlines)
while True:
    schedule.run_pending()
    time.sleep(1)




#if __name__ == "__main__":
#    check_deadlines()
    