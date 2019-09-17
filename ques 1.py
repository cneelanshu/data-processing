

b = input('enter the comma separated binary nos. :')

s = b.split(',')                  # split each binary no. when encounters comma(',') 

print(s)                          # output is the list of binary nos. after comma separation

items = []                        # empty list is created to later append binary nos. divisible by 5

for j in s:
    num = int(j,2)                #converting each binary no. into decimal no.
    print(num, end = ' ')

    if num % 5 == 0:
        items.append(j)           # appending binary nos. divisible by 5

print('\n')
print(items)                      # return the list of binary nos. divisible by 5

print(','.join(items))            
