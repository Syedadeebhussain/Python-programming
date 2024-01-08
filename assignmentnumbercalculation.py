#Problem Statement: Number Calculation with Digit Manipulation
#Write a Python program that takes a starting and ending number from the user and identifies even and odd numbers 
#within that range. Apply the following rules:
#For even double-digit numbers, calculate the sum of squares of the digits using a function.
#For odd double-digit numbers, calculate the sum of cubes of the digits using a function.
#For single-digit numbers, print the number as it is.

                #Example:
                #Enter the starting range: 10
                #Enter the ending range: 20
                #Numbers and their respective calculations within the range 10 to 20:
                #10 - 1
                #11 - 2
                #12 - 5
                #13 - 28
                #14 - 17
                #15 - 126
                #16 - 37
                #17 - 344
                #18 - 65
                #19 - 730
                #20 - 4  
def sum_squares(i):
   sum=0
   tem=i
   while(i>0):
       r=i%10
       sum+=r**2
       i=i//10
   print(f"{tem}-{sum}")
def sum_cube(i):
    sum=0
    tem=i
    while(i>0):
       r=i%10
       sum+=r**3
       i=i//10
    print(f"{tem}-{sum}")
a=int(input("Enter the starting range: "))
b=int(input("Enter the ending range: "))
print(f"Numbers and their respective calculations within the range {a} to {b}:")
for i in range(a,b+1):
    if i%2==0:
        sum_squares(i)
    else:
        sum_cube(i)