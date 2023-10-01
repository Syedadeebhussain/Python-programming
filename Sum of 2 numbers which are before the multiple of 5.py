n=int(input("enter the ending range"))
s=0
for i in range(5,n+1):
     if i%5==0:
          i1=i-2
          i2=i-1
          s=s+(i1-2)+(i2-1)
     else:
        print(" ")
print(f"sum is {s}")
 