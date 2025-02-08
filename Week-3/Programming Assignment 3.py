input_numbers = list(map(int, input().split()))  # Taking input from user

def process_list(number):
    reversed_number = number[::-1]
    result = []
    
    for i in range(len(number)):
        if i % 2 == 0:
            result.append(number[i] + reversed_number[i])
        else:
            result.append(number[i])
    
    return result

output = process_list(input_numbers)  

print(" ".join(map(str, output)),end="")  
