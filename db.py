import psycopg2

# Підключення до PostgreSQL
conn = psycopg2.connect(
    dbname="clinic_db",
    user="user",
    password="password",
    host="db",
    port="5432"
)

cursor = conn.cursor()

# Створення таблиць
cursor.execute("""
CREATE TABLE IF NOT EXISTS Patients (
    card_number SERIAL PRIMARY KEY,
    last_name VARCHAR(100) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    middle_name VARCHAR(100),
    address VARCHAR(255),
    phone VARCHAR(15) CHECK (phone ~ '^\\+?\\d{1,15}$'),
    birth_year INTEGER CHECK (birth_year > 1900),
    category VARCHAR(10) CHECK (category IN ('дитяча', 'доросла'))
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Doctors (
    doctor_id SERIAL PRIMARY KEY,
    last_name VARCHAR(100) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    middle_name VARCHAR(100),
    specialization VARCHAR(20) CHECK (specialization IN ('лор', 'терапевт', 'хірург')),
    experience_years INTEGER CHECK (experience_years >= 0)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Stays (
    stay_id SERIAL PRIMARY KEY,
    card_number INTEGER REFERENCES Patients(card_number) ON DELETE CASCADE,
    admission_date DATE NOT NULL,
    days_in_hospital INTEGER CHECK (days_in_hospital > 0),
    daily_cost DECIMAL(10, 2) CHECK (daily_cost > 0),
    discount DECIMAL(5, 2) CHECK (discount >= 0 AND discount <= 100),
    doctor_id INTEGER REFERENCES Doctors(doctor_id) ON DELETE CASCADE
);
""")

conn.commit()
cursor.close()
conn.close()
