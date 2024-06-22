"""
We'll try to understand classes in python. 
Check the resources on google classroom to ensure you have gone through everything expected.

"""
###### THESE LISTS HAVE ALREADY BEEN DEFINED FOR YOU ###############
engineer_roster = [] # A list of all instantiated engineer objects
sales_roster = [] # List of all instantiated sales objects
branchmap = {  # A dictionary of dictionaries -> Maps branchcodes to cities and branch names
    0:  { "city": "NYC", "name": "Hudson Yards"},
    1:  { "city": "NYC" , "name": "Silicon Alley"},
    2:  { "city": "Mumbai", "name": "BKC"},
    3:  { "city": "Tokyo", "name": "Shibuya"},
    4:  { "city": "Mumbai", "name": "Goregaon"},
    5:  { "city": "Mumbai", "name": "Fort"}
}
####################################################################

class Employee:
    name : str 
    age : int
    ID : int
    city : int
    branches : list[int] # This is a list of branches (as branch codes) to which the employee may report
    salary : int 

    def __init__(self, name, age, ID, city,\
                 branchcodes, salary = None):
        self.name = name
        self.age = age 
        self.ID = ID
        self.city = city
        self.branches = branchcodes
        if salary is not None: self.salary = salary
        else: self.salary = 10_000 
    
    def change_city(self, new_city:str) -> bool:
        # Change the city 
        if self.city != new_city:
            self.city = new_city
            # Return true if city change, successful, return false if city same as old city
            return true
        return false
        
        pass

    def migrate_branch(self, new_code:int) -> bool:
        # Should work only on those employees who have a single 
        # branch to report to. Fail for others.
        if len(self.branches) != 1:
            return false

        current_branch_code = self.branches[0]
        current_city = self.branchmap[current_branch_code]["city"]
        new_city = self.branchmap[new_code]["city"]

        # Change old branch to new if it is in the same city, else return false.
        if current_city == new_city:
            self.branches[0] = new_code
            return True
        else:
            return False
    
        pass

    def increment(self, increment_amt: int) -> None:
        # Increment salary by amount specified.
        self.salary += increment_amt
        pass





class Engineer(Employee):
    position : str # Position in organization Hierarchy

    def __init__(self, name, age, ID, city,\
                 branchcodes, position= "Junior", salary = None):
        # Call the parent's constructor
        super().__init__(name, age, ID, city, branchcodes, salary)
        
        # Check if position is one of "Junior", "Senior", "Team Lead", or "Director"
        # Only then set the position. 
        if position in ["Junior", "Senior", "Team Lead", "Director"]:
            self.position = position
        else:
            self.position = "Junior" 
        

    
    def increment(self, amt:int) -> None:
        # While other functions are the same for and engineer,
        # and increment to an engineer's salary should add a 10% bonus on to "amt"
        bonus = amt * 0.10
        total_increment = amt + bonus
        self.salary += total_increment

        pass
        
    def promote(self, position:str) -> bool:
        # Return false for a demotion or an invalid promotion
        # Promotion can only be to a higher position and
        # it should call the increment function with 30% of the present salary
        # as "amt". Thereafter return True.
        if position not in ["Senior", "Team Lead", "Director"]:
            return False
        
        if position == "Senior" and self.position in ["Team Lead", "Director"]:
            return False
        
        if position == "Team Lead" and self.position == "Director":
            return False
        
        # Promotion to a higher position
        current_salary = self.salary
        amt = current_salary * 0.30  # 30% of present salary as amt
        
        # Call the increment function with amt
        self.increment(amt)
        
        # Update position
        self.position = position
        
        return True
        pass



class Salesman(Employee):
    """ 
    This class is to be entirely designed by you.

    Add increment (this time only a 5% bonus) and a promotion function
    This time the positions are: Rep -> Manager -> Head.

    Add an argument in init which tracks who is the superior
    that the employee reports to. This argument should be the ID of the superior
    It should be None for a "Head" and so, the argument should be optional in init.
    """
    
    # An extra member variable!
    superior : int # EMPLOYEE ID of the superior this guy reports to
    position : str # Position in organization Hierarchy

    def __init__(self, name, age, ID, city,\
                 branchcodes, position= "Rep", salary = None, superior = None):
        # Call the parent's constructor
        super().__init__(name, age, ID, city, branchcodes, salary)
        
        # Check if position is one of "Rep", "Manager" or "Head"
        # Only then set the position. 
        if position in ["Rep", "Manager", "Head"]:
            self.position = position
        else:
            self.position = "Rep"

        if position != "Head":
            self.superior = superior
        else:
            self.superior = None
    

    # def increment 
    def increment(self, amt:int) -> None:
        # Add increment (this time only a 5% bonus)
        bonus = amt * 0.05
        total_increment = amt + bonus
        self.salary += total_increment

        pass

    
     # def promote 
    def promote(self, position:str) -> bool:
        # Return false for a demotion or an invalid promotion
        # Promotion can only be to a higher position and
        # it should call the increment function with 30% of the present salary
        # as "amt". Thereafter return True.
        if position not in ["Manager", "Head"]:
            return False
        
        if position == "Manager" and self.position in ["Head"]:
            return False
        
        # Promotion to a higher position
        current_salary = self.salary
        amt = current_salary * 0.30  # 30% of present salary as amt
        
        # Call the increment function with amt
        self.increment(amt)
        
        # Update position
        self.position = position
        
        return True
        pass

    # To get the name of any employee from their ID
    def get_employee_name_by_id(emp_id, Salesman):
        for employee in Salesman:
            if employee['ID'] == emp_id:
                return employee['name']
        return None  # Return None if employee with given ID is not found


    def find_superior(self) -> tuple[int, str]:
        # Return the employee ID and name of the superior
        # Report a tuple of None, None if no superior.
        if self.superior is None:
            return (None, None)
        else:
            superior_id = self.superior
            superior_name = self.get_employee_name_by_id(superior_id, Salesman)
            return (superior_id, superior_name)

        pass

    def add_superior(self) -> bool:
        # Add superior of immediately higher rank.
        # If superior doesn't exist return false,
        pass


    def migrate_branch(self, new_code: int) -> bool:
        # This should simply add a branch to the list; even different cities are fine
        self.branches.append(new_code)
        pass





    
    
