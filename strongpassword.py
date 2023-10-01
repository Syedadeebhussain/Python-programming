while True:
     password=input("enter your password") 
     if len(password)<12:
         print("enter your password again")
         continue
     else:
         hasupper=False
         haslower=False
         hasdigit=False
         haspecial=False
         hasspace=False

         for char in password:
            if char.isalpha():
              if char.isupper():
                hasupper=True
              elif char.islower():
                haslower=True
            elif char.isdigit():
                   hasdigit=True
            elif char.isspace():
                 hasspace=True
            else:
                  hasspecial=True
         if hasupper and hasupper and hasdigit and hasspecial:
            print("strong password")
         else:
           print("thisis not a strong password pleqse try again")
