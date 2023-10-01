start=int(input("enter value for starting"))
end=int(input("enter value for ending"))
s1 = 0
s2 = 0
for i in range(start,end+1):
    if i%2==0:
        s1+=i
    else:
        s2+=i
print(f"sum of even numbers are {s1}") 
print(f"sum of odd numbers are {s2}")       