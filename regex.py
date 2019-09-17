# Write a regular expression to tag following string:
# 1) @sonu#$

s = '@sonu#$'
import re
x = re.findall('\W+\w+\W+',s)
print (x)


# other way
y = re.findall('[\W]sonu\W+',s)
print (y)




