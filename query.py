import psycopg2
from psycopg2 import sql

def fetch_data(query, params=None):
    cursor.execute(query, params)
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    print("\n" + "-" * 60)
    print(f"{' | '.join(columns)}")
    print("-" * 60)
    for row in rows:
        print(" | ".join(str(col).ljust(15) for col in row))
    print("-" * 60)

conn = psycopg2.connect(
    dbname="clinic_db",
    user="user",
    password="password",
    host="db",
    port="5432"
)
cursor = conn.cursor()

queries = [
    ("Всі дані з таблиці Patients", """
    SELECT*
    FROM Patients;
    """),
    ("Всі дані з таблиці Doctors", """
    SELECT*
    FROM Doctors;
    """),
    ("Всі дані з таблиці Stays", """
    SELECT*
    FROM Stays;
    """),    
    ("Пацієнти, народжені після 1998 року:", """
    SELECT last_name, first_name, middle_name
    FROM Patients
    WHERE birth_year > 1998
    ORDER BY last_name;
    """),

    ("Кількість пацієнтів за категорією:", """
    SELECT category, COUNT(*) AS patient_count
    FROM Patients
    GROUP BY category;
    """),

    ("Сума лікування та сума з пільгою для кожного пацієнта:", """
    SELECT p.card_number, 
           (s.days_in_hospital * s.daily_cost) AS total_cost, 
           ((s.days_in_hospital * s.daily_cost) * (1 - s.discount / 100)) AS cost_with_discount
    FROM Patients p
    JOIN Stays s ON p.card_number = s.card_number;
    """),

    ("Звернення до лікаря заданої спеціалізації (лор):", """
    SELECT p.last_name, p.first_name, p.middle_name, d.specialization
    FROM Patients p
    JOIN Stays s ON p.card_number = s.card_number
    JOIN Doctors d ON s.doctor_id = d.doctor_id
    WHERE d.specialization = 'лор';
    """),

    ("Кількість звернень пацієнтів до кожного лікаря:", """
    SELECT d.last_name, d.first_name, COUNT(*) AS visit_count
    FROM Doctors d
    JOIN Stays s ON d.doctor_id = s.doctor_id
    GROUP BY d.last_name, d.first_name;
    """),

    ("Кількість пацієнтів кожної категорії, що лікувалися у лікарів різних спеціалізацій:", """
    SELECT p.category, d.specialization, COUNT(*) AS patient_count
    FROM Patients p
    JOIN Stays s ON p.card_number = s.card_number
    JOIN Doctors d ON s.doctor_id = d.doctor_id
    GROUP BY p.category, d.specialization;
    """)
]

for description, query in queries:
    print(f"\n{description}")
    fetch_data(query)

cursor.close()
conn.close()
