s=input("enter any string")
str=" "
for i in range(0,(len(s))):
    if i%2==0:
        if str[i].islower():
            str+=s[i].upper()
        elif str[i].isupper():
             str+=s[i].lower()
        else:
             str+=s[i]
    else:
         str+=s[i]
print(str)
            
           
        