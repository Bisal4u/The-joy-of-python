user_input=list(map(int,input().split()))

def duplicates_remover(numbers):
    seen_f1=set()
    even_f2=set()
    result=[]
    
    for i in numbers:
        if i%2==0:
            if i in even_f2:
                continue
            even_f2.add(i)
            
        result.append(i)
        
    return result
            

output=duplicates_remover(user_input)

print(" ".join(map(str,output)),end="")
