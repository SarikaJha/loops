num = int(input("Enter a number: "))    
sum = 0
var = num   
while(var > 0):    
    digit = var % 10
    sum = sum + digit    
    var = var // 10    
     
if num % sum == 0:    
    print(num, "is a Harshad Number")    
else:    
    print(num, "is not a Harshad Number")