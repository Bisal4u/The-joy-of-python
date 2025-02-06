
numbers = list(map(int,input().split())
               
unique_numbers=sorted(set(numbers))
length=len(unique_numbers)

if length<2:
    print("No smallest number")
else:
    print(unique_numbers[1])
