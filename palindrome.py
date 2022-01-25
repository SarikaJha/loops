num=int(input("Enter any number:"))
var=num
rev=0
while(num>0):
    digit=num%10
    rev=rev*10+digit
    num=num//10
if(var==rev):
    print("The number is palindrome")
else:
    print("Not a palindrome!")
