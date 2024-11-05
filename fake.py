import psycopg2
from datetime import date, timedelta

conn = psycopg2.connect(
    dbname="clinic_db",
    user="user",
    password="password",
    host="db",
    port="5432"
)
cursor = conn.cursor()

# Заповнення таблиці 'Patients'
patients_data = [
    (1, "Іванов", "Іван", "Іванович", "вул. Козацька, 1", "+380123456789", 2000, "дитяча"),
    (2, "Петренко", "Петро", "Петрович", "вул. Садова, 2", "+380987654321", 1995, "доросла"),
    (3, "Сидоренко", "Сидір", "Сидорович", "вул. Гетьманська, 3", "+380555123456", 2010, "дитяча"),
    (4, "Коваленко", "Костянтин", "Костянтинович", "вул. Центральна, 4", "+380332456789", 1988, "доросла"),
    (5, "Шевченко", "Тарас", "Григорович", "вул. Патріотична, 5", "+380777456123", 1992, "доросла"),
    (6, "Мельник", "Марія", "Олексіївна", "вул. Осіння, 6", "+380123789456", 2005, "дитяча"),
    (7, "Тимошенко", "Ольга", "Василівна", "вул. Вишнева, 7", "+380444456789", 1997, "доросла"),
    (8, "Грищенко", "Анна", "Сергіївна", "вул. Шевченка, 8", "+380654789123", 2001, "дитяча"),
    (9, "Кучер", "Олександр", "Анатолійович", "вул. Зелена, 9", "+380321456789", 1990, "доросла"),
]
cursor.executemany("INSERT INTO Patients (card_number, last_name, first_name, middle_name, address, phone, birth_year, category) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", patients_data)

# Заповнення таблиці 'Doctors'
doctors_data = [
    (1, "Кравченко", "Олег", "Іванович", "лор", 10),
    (2, "Мельник", "Наталія", "Сергіївна", "терапевт", 8),
    (3, "Шевченко", "Ірина", "Володимирівна", "хірург", 15),
    (4, "Бондаренко", "Сергій", "Олександрович", "терапевт", 12)
]
cursor.executemany("INSERT INTO Doctors (doctor_id, last_name, first_name, middle_name, specialization, experience_years) VALUES (%s, %s, %s, %s, %s, %s);", doctors_data)

# Дані прибуттів у стаціонар (17 записів)
stays_data = [
    (1, 1, date.today(), 5, 100, 10, 1),  # Пацієнт 1
    (2, 2, date.today(), 7, 150, 5, 2),   # Пацієнт 2
    (3, 3, date.today(), 3, 120, 0, 3),   # Пацієнт 3
    (4, 4, date.today(), 14, 200, 15, 1),  # Пацієнт 4
    (5, 5, date.today(), 10, 180, 0, 2),   # Пацієнт 5
    (6, 6, date.today(), 2, 90, 0, 3),     # Пацієнт 6
    (7, 7, date.today(), 4, 130, 5, 1),     # Пацієнт 7
    (8, 8, date.today(), 6, 160, 10, 2),    # Пацієнт 8
    (9, 9, date.today(), 1, 80, 0, 3),      # Пацієнт 9
    (10, 1, date.today() - timedelta(days=2), 8, 110, 0, 1),  # Пацієнт 1
    (11, 2, date.today() - timedelta(days=1), 9, 140, 0, 2),  # Пацієнт 2
    (12, 3, date.today() - timedelta(days=3), 3, 120, 0, 3),  # Пацієнт 3
    (13, 4, date.today() - timedelta(days=5), 15, 250, 5, 1),  # Пацієнт 4
    (14, 5, date.today() - timedelta(days=7), 7, 160, 0, 2),  # Пацієнт 5
    (15, 6, date.today() - timedelta(days=6), 10, 90, 0, 3),  # Пацієнт 6
    (16, 7, date.today() - timedelta(days=4), 4, 150, 5, 1),  # Пацієнт 7
    (17, 8, date.today() - timedelta(days=8), 12, 180, 10, 2)  # Пацієнт 8
]
cursor.executemany("INSERT INTO Stays (stay_id, card_number, admission_date, days_in_hospital, daily_cost, discount, doctor_id) VALUES (%s, %s, %s, %s, %s, %s, %s);", stays_data)

conn.commit()
cursor.close()
conn.close()
