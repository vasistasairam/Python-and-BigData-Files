# 1) Write a program to read a text file and print count number of lines, 
# number of words and number of characters in file.
count = 0
with open('xyzfile.txt','r') as file: # read lines
    #file.readlines()
    for lines in file:
        count += 1
    #for line,lines in enumerate(file):
    print (count)




with open('xyzfile.txt','r') as file: # total lines in a file
    print (len(file.readlines()))


with open('xyzfile.txt','r') as file:
    x = file.read().strip().split()
    words = sum(len(line.split()) for line in x)
    print (words)
    
    
    
with open('xyzfile.txt','r') as f:  # to find no.of charecters in a file.
    list1 = f.read().strip().split()
    charecters  = sum(len(word) for word in list1)
    print (charecters)



        

with open('wordcountfile.txt','r') as file:
    list1 = file.read().strip().split()
    words = sum(len(line.split()) for line in list1) # no of words in a file
    charecters  = sum(len(word) for word in list1) # no of charecters in a file
    print ('no of lines in a file: ',len(file.readlines()))
    print ('no of words in a file: ',words)
    print ('no.of charecters in a file: ',charecters)





line_counter = 0
word_counter = 0
charecter_count = 0
with open('wordcountfile.txt','r') as file:
    list1 = file.readlines() # reading the file into a list
    for line in list1:  # counting no.oflines in a file
        line_counter += 1
        #print ('no of lines in a file: ',line_counter)
    
        for word in len(line.split()): # for no.of words ineach line
            word_counter += word
            
            for charecter in len(word):
                charecter_count += charecter
                
    print ('no of lines in a file: ',line_counter)
    print ('no of words in a file: ',word_counter)
    print ('no of charecters in a file: ',charecter_count)
    

















    
    
        
    
    
    



