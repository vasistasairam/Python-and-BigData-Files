'''import json

data = {}  
data['people'] = []  
data['people'].append({  
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({  
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({  
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'w') as outfile:  
    json.dump(data, outfile)'''

    
    
    
    
import json
def options():   
    print (
'''    Select an option
    1. Add New Contact
    2. Delete Contact
    3. Edit Contact
    4. Search Contact
    5. Display All Contacts
    6. Exit'''
            )
    return

options()

num = int(input('Enter your option: '))

while(num <= 6):
    if num == 1:        # NEW CONTACT
        name = input('Enter name: ')
        number = int(input('Enter number: '))
        #number_list.append(name,number)
# =============================================================================
#         items = {name:number}
#         print (items)
#         contacts.update(items)
# =============================================================================
        try:
            with open('contacts.json','r') as file:
                data = json.load(file)
            data[name]=number
            with open("contacts.json", "w") as file:
                json.dump(data, file)
            options
            num = int(input('Enter your option: '))
        except FileNotFoundError:
            with open('contacts.json', 'w') as outfile:
                json.dump({'aaa':123}, outfile)
            with open('contacts.json','r') as file:
                data = json.load(file)
            data[name]=number
            del data['aaa']
            print ('contact has been added')
            with open("contacts.json", "w") as file:
                json.dump(data, file)
            options()
            num = int(input('Enter your option: '))
# =============================================================================
#     elif num == 2:      # DELETE CONTACT
#         name = input('enter name of the contact you want to delete: ')
#         with open('phonebook.json','r') as file:
#             data = json.load(file)
#         if data[name]:
#             del data[name]
#             print('contact has been removed')
#             with open("phonebook.json", "w") as file:
#                 json.dump(data, file)
#             options()
#             num = int(input('Enter your option: '))
# # =============================================================================
# #         if num == 2:
# #             try:
# #                 file = json.loads('phonebook.json')
# #             except ValueError:  
# #                 for i in range(len(file)):
# #                     if [i] == name_list.index(name):
# #                         file.pop(i)
# #                         print ('contact has been deleted: ')
# #                     
# #                     else:
# #                         print('contact does not exist' )
# #             
# #             '''with open('phonebook.json','a') as file:
# #                 file.write('\n')
# #                 json.dump(contacts,file)'''
# =============================================================================
# =============================================================================
    elif num == 3:      # EDIT CONTACT
        name = input('enter name of the contact you want to edit: ')
        with open('contacts.json','r') as file:
            data = json.load(file)
        if data[name]:
            number = input('enter new number: ')
            data[name] = number
            with open('contacts.json','w') as file:
                json.dump(data,file)
                print ('contact edited',name,data.key(name))
                options()
                num = int(input('Enter your option: '))
        else:
            print('no such contact exist,please add new contact:')
            options()
            num = int(input('Enter your option: '))
    
else:
    print('exit phonebook')
    
    
    





















