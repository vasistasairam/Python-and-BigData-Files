# working with JSON
# json syntax, objects and etc.. and json is lightweighted than XML
# in python there is no object called json object.

# example
book = {}  # creating a dictionary ith key 'tom' and value {}
book['tom'] = {
        'name':'tomm',
        'address':'abc road,xyz colony',
        'phone':'1234566'
        }

import json 
s = json.dumps(book) # python dict to json string
print (s)
with open('C:\\Users\\HP\\pythonfiles\jsonprectice.json','a') as file:
    file.write(s)
    # in json dict are treated as objects. we can iterate over json objects.
    # here are the list of python to json convertion of data structures.
    
    '''Python	  JSON
    
       dict	     object
       list,      tuple	array
       str	     string
       int,float, 
       int-&float-derived
       Enums	     number
       True	     true
       False	     false
       None	     null'''
# in json all the keys must be strings. and values can be anything.

with open('C:\\Users\\HP\\pythonfiles\jsonprectice.json','r') as f:
    s = f.read()  # here  s is a string. json is returning it as string.
    print(s)
    import json  # here we need toimport json bcoz, we are dealing with json string.
    book = json.loads(s)   # here we are using using loads bocz s is a string.  
    print(book)
    book['tom']['phone']  # taking  values from the dict.



# json parsing()











