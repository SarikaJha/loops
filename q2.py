#maximum number using loops:
max=0
x=1
while x<=5:
    N=int(input("enter the number:"))
    if N>max:
        max=N
    x+=1
print(max,"is the maximum number")
