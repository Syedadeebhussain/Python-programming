#Problem Statement: Armstrong Number Manipulation
 # Write a Python script that takes a starting and ending number from the user and identifies Armstrong numbers within that range. 
#For Armstrong numbers less than 300, print them as they are. 
# For Armstrong numbers greater than or equal to 300, reverse each number and display both the original and reversed numbers side by side.
                
                #Example:
                 #   Enter the starting range: 100
                  #  Enter the ending range: 2000
                   # Original and reversed Armstrong numbers within the range 100 to 2000:
                   # 153
                    # 370 -> 073
                    # 371 -> 173
                    # 407 -> 704
                    # 1634 -> 4361

              #  PERFOMR THE ABOVE BY USING FUNCTION AND LISTS CONCEPT.
      
def armstrong(a,b):
    for i in range(a,b+1):
            summ=0
            order = len(str(i))
            tem=i
            while(tem>0):
                r=tem%10
                summ+=r**order
                tem=tem//10
            if summ==i:
              if i<300:
                print(i) 
              elif i>=300:
                  print(f"{i}->{(str(i))[::-1]}")
a=int(input("Enter the starting range: "))
b=int(input("Enter the ending range: "))
print(f"Original and reversed Armstrong numbers within the range {a} to {b}:")
armstrong(a,b) 