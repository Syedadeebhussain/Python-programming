start=int(input("enter value for starting"))
end=int(input("enter value for ending"))
s = 0
for x in range(start,end+1):
    s=s+x
print(f"sum of numbers starting from {start} and ending at {end} is {s}")
