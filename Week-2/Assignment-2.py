

userinput = input()  

inputlist = userinput.replace(",", " ").split() 

numbers = [float(num) for num in inputlist]  

a = sum(numbers) 
b = len(numbers) 
c = a / b  
d=int(c)
print(d,end="")
