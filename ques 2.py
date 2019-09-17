import re              #import regular expression modules

pw = input("enter passwords : ") # enter passwords separated by comma(,)

p = pw.split(',')    # split each password when encounters comma(',') and saved the object into variable 'p'

print(p)        # returns the list of passwords as element

for i in range(len(p)):

    if (len(p[i])<6 or len(p[i])>12):
        print(p[i], 'is not a valid password')
    
    if not re.search('[a-z]',p[i]):
        print(p[i],'is not a valid password')
        
    elif not re.search('[A-Z]',p[i]):
        print(p[i],'is not a valid password')

    elif not re.search('[0-9]',p[i]):
        print(p[i],'is not a valid password')

    elif not re.search('[$#@]',p[i]):
        print(p[i],'is not a valid password')

    else:
        print(p[i],'is a valid password')
