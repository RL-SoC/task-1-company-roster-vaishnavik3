"""
This is where the actual working of the program will happen!
We'll be Querying stuff for testing whether your classes were defined correctly

Whenever something inappropriate happens (like a function returning false in people.py),
raise a Value Error.
"""
from people import Employee, Engineer, Salesman # import everything!

if __name__ == "__main__":  # Equivalent to int main() {} in C++.
    last_input = 99
    while last_input != 0:
        last_input = int(input("Please enter a query number:"))

        if last_input == 1:
            name = input("Name:")
            ID = int(input("ID:"))
            city = input("City:")
            branchcodes_input = input("Branch(es):")
            branchcodes = [int(code.strip()) for code in branchcodes_input.split(",")]
            salary = input("Salary: ")
            salary = int(salary) if salary else None
            engineer = Engineer(name, age, ID, city, branchcodes, salary=salary)
            engineer_roster.append(engineer)
            print("Engineer added successfully.")

        elif last_input == 2:
            name = input("Name:")
            age = int(input("Age:"))
            ID = int(input("ID:"))
            city = input("City:")
            branchcodes_input = input("Branch(es):")
            branchcodes = [int(code.strip()) for code in branchcodes_input.split(",")]
            position = input("Position (Rep, Manager, Head):")
            salary = input("Salary: ")
            salary = int(salary) if salary else None
            superior = input("Superior ID (optional): ")
            superior = int(superior) if superior else None
            salesman = Salesman(name, age, ID, city, branchcodes, position, salary, superior)
            sales_roster.append(salesman)
            print("Salesperson added successfully.")

        elif last_input == 3:
            ID = int(input("ID: "))
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break
            
            if not found_employee:
                print("No such employee")
            else:
                print(f"Name: {found_employee.name}")
                print(f"Age: {found_employee.age}")
                print(f"City of Work: {found_employee.city}")
                branch_names = [branchmap[code]["name"] for code in found_employee.branches]
                print(f"Branches: {', '.join(branch_names)}")
                print(f"Salary: {found_employee.salary}")

        elif last_input == 4:
            ID = int(input("ID: "))
            new_code = int(input("New Branch Code: "))
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break

            if not found_employee:
                raise ValueError("No such employee")

            if not found_employee.migrate_branch(new_code):
                raise ValueError("Branch migration failed")

            print("Branch migrated successfully.")

        elif last_input == 5:
            ID = int(input("Enter Employee ID to promote: "))
            position = input("Enter new position: ")
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break

            if not found_employee:
                raise ValueError("No such employee")

            if not found_employee.promote(position):
                raise ValueError("Promotion failed")

            print("Promotion successful.")

        elif last_input == 6:
            ID = int(input("Enter Employee ID to give increment: "))
            increment_amt = int(input("Enter increment amount: "))
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break

            if not found_employee:
                raise ValueError("No such employee")

            found_employee.increment(increment_amt)
            print("Increment successful.")

        elif last_input == 7:
            ID = int(input("Enter Employee ID to find superior: "))
            found_employee = None
            for employee in sales_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break

            if not found_employee:
                raise ValueError("No such employee")

            superior_id, superior_name = found_employee.find_superior()
            if superior_id is None:
                print("No superior found.")
            else:
                print(f"Superior ID: {superior_id}, Name: {superior_name}")

        elif last_input == 8:
            ID_E = int(input("Enter Employee ID to add superior: "))
            ID_S = int(input("Enter Employee ID of superior: "))
            found_employee = None
            for employee in sales_roster:
                if employee.ID == ID_E:
                    found_employee = employee
                    break

            if not found_employee:
                raise ValueError("No such employee")

            if not found_employee.add_superior(ID_S):
                raise ValueError("Adding superior failed")

            print("Superior added successfully.")

        else:
            raise ValueError("No such query number defined")

            


        






