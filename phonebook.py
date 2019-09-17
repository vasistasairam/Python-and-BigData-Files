
#sample prog for phone book:

print ('enter 1 or >1 to add new contact:')
print ('enter 0 to edit contact:')
print ('enter -1 or <-1  to delete contact:')

phonebook = {}
name_list = []
number_list = []
num = int(input('enter your option:'))
#print ('enter your option:')
if num >= 1:
    name = input('enter contact name:')
    name_list.extend([name])
    number = input('enter contact number:')
    number_list.extend([number])
    saveitems = dict(zip(name_list,number_list))
    phonebook.update(saveitems)
    
    #phonebook.update(saveitems)
    #phonebook.copy()
print (phonebook)
phonebook.items()
print(len(phonebook))
    
    
#num = int(input('enter your option:'))    
if num == 0:
    print('remove name in phonebook:')
    name = input('enter name you want to remove: ')
    if name in phonebook:
        del phonebook[name]
    else:
        print (name, 'is not present in phonebook:')
    
#num = int(input('enter your option:'))
if num <= -1:
    print ('enter contact name which you want to edit:')
    name = input('enter  name: ')
    if name in phonebook:
        phonebook[name] =input('enter new number: ') 
        print (phonebook)
    else:
        print (name, 'is not present in phonebook:')
    


#phonebook.has_key(input('enter contact name which you want to search:'))
#print ('contact exists:')


    
        












