import math
side1=float(input("enter first side"))
side2=float(input("enter second side"))
side3=float(input("enter third side"))
if side1>0 and side2>0 and side3>0:
    s=(side1+side2+side3)/2
    result=math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
    print("area of trangle ",result)
else:
    print("enter a valid length")