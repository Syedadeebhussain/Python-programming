arm=int(input("enter any number"))
n=len(str(arm))
n=int(n)
s=0
p=arm
while p!=0:
      l = p % 10
      res = l**n
      s+=res
      p=p//10
if s==arm:
   print(f"{arm} is an armstrong number")
else:
     print(f"{arm} is not an armstrong number ")           
