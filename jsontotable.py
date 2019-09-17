# importing modules
import pymysql
import json

# opening a json file and loading it into a list
with open('C://Users//HP//pythonfiles//assignment2//employdetails1.json','r') as file:
    list1 = json.load(file)

# connecting to database with connection name db   (server, username, passward, database)
db = pymysql.connect('localhost','root','vasista22','testdb')#,cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()

# creating mysql table in database 'testdb' by name 'employee'
table_name = "employee"
for dictionary in list1:  # itering over list1 to get column names
    first_name = dictionary['firstname']   # column name
    last_name = dictionary['lastname']     # column name
    age = dictionary['age']                # column name
    sex = dictionary['sex']                # column name
    income = dictionary['income']          # column name
    
    # inserting values into tables using insert query, sending values as variables in a query
    query_str= "insert into "+table_name+" values('"+first_name+"','"+last_name+"',"+str(age)+",'"+sex+"',"+str(income)+");"    
    cursor.execute(query_str)
    db.commit()  # commiting sql query for reflecting changes in mysql table. 
db.close()













