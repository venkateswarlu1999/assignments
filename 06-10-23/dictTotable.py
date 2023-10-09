# hash table stracture
import pandas as pd 

employeeData={
    "employee":[
        {'id':1, 'name':'venkat', 'des':'developer', 'salary':'3.2lpa'},
        {'id':2, 'name':'siva', 'des':'tester', 'salary':'3lpa'},
        {'id':3, 'name':'nani', 'des':'backend', 'salary':'2lpa'},
        {'id':4, 'name':'raju', 'des':'data scince', 'salary':'2.3lpa'}
    ]
}
table=pd.DataFrame(employeeData['employee'])
print(table)