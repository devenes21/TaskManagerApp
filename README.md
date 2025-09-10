1. TaskManager.py

Προσθήκη εργασίας

Αφαίρεση εργασίας

Προβολή όλων των εργασιών

Σημείωση εργασίας ως ολοκληρωμένη

Αναζήτηση εργασίας

Το αρχείο χρησιμοποιεί JSON για αποθήκευση των εργασιών (tasks.json).

Παράδειγμα εκτέλεσης:
   python3 TaskManager.py


   
2. Reminder.py

Έλεγχος ημερομηνιών λήξης εργασιών

Στέλνει email 3 μέρες πριν την προθεσμία για μη ολοκληρωμένες εργασίες

Απαιτήσεις: pip install schedule
Παράδειγμα εκτέλεσης: python3 reminder.py

Βάλε σωστά τα emails: email_address, email_password (app password για Gmail), to_email.
Ρύθμισε την ώρα υπενθύμισης στη γραμμή: schedule.every().day.at("HH:MM").do(check_deadlines)
Tο πρόγραμμα τρέχει συνεχώς σε loop για να ελέγχει καθημερινά.
