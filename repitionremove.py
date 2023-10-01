str=input("enter any string")
reg=" "
s=" "
for ch in str:
    if ch not in reg:
       out=str.count(ch)
       s+=f'{ch}{out}'
       reg+=ch
print(s)
str=s