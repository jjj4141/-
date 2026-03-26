data = list(input())
total = 0

for i in range(len(data)):
    
    if (data[i].isupper()):
        total += ord(data[i]) - 38

    else:
        total += ord(data[i]) - 96

is_prime = True        
        
if(total == 1):
        pass
    
else:

    for n in range(2, total):
             
     if (total%n == 0):
        
        is_prime = False
        break

if (is_prime == True):
    print("It is a prime word.")

else:
    print("It is not a prime word.")
