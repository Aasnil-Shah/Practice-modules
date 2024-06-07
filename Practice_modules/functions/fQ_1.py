'''Create a function that can accept two arguments employee name and ID and
print its value as shown in the example, and if the ID is missing in function call
it should show it as 001:
Example: Employee Name - XYZ
Employee ID - 555 '''

def employee(ename,eid = "001"):
    Name = ename
    ID = eid
    print("EmployeeID -", ID)
    print("Employee Name -", Name)

employee("aASNIL", 4)
employee("Aasu")