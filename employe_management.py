import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department TEXT,
    salary REAL
)
""")
conn.commit()

def add_employee():
    name = input("Enter name: ")
    dept = input("Enter department: ")
    salary = float(input("Enter salary: "))
    cursor.execute("INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)", (name, dept, salary))
    conn.commit()
    print("Employee added!\n")

def view_employees():
    cursor.execute("SELECT * FROM employees")
    for row in cursor.fetchall():
        print(row)
    print()

def update_salary():
    emp_id = int(input("Enter employee ID to update: "))
    new_salary = float(input("Enter new salary: "))
    cursor.execute("UPDATE employees SET salary=? WHERE id=?", (new_salary, emp_id))
    conn.commit()
    print("Salary updated!\n")

def delete_employee():
    emp_id = int(input("Enter employee ID to delete: "))
    cursor.execute("DELETE FROM employees WHERE id=?", (emp_id,))
    conn.commit()
    print("Employee deleted!\n")

while True:
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Salary")
    print("4. Delete Employee")
    print("0. Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        update_salary()
    elif choice == "4":
        delete_employee()
    elif choice == "0":
        break
    else:
        print("Invalid choice!\n")

conn.close()
