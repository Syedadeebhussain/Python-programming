#Problem Statement: Leap Year Reversal

 #               Write a Python script to find and display leap years within a specified range provided by the user. 
  #              For each leap year found in the range, reverse the year and display both the original and reversed forms on the screen.
                
   #             Example :- 
    #            Enter the starting year: 2000
     #           Enter the ending year: 2025
      #          Leap years and their reversed forms:
       #         2000 -> 0002
        #        2004 -> 4002
         #       2008 -> 8002
          #      2012 -> 2102
           #     2016 -> 6102
            #    2020 -> 0202
             #   2024 -> 4202

              #  WRITE THE SOLUTION OF THE ABOVE BY USING LISTS AND FUNCTIONS CONCEPT.
                
def leap_year_rev(a,b):
    for n in range(a,b+1):
      if n % 400 == 0 or n % 100 != 0 and n % 4 == 0:
        print(f"{n}->{str(n)[::-1]}")
a=int(input("Enter the starting year: "))
b=int(input(" Enter the ending year: "))
print("Leap years and their reversed forms:")
leap_year_rev(a,b)