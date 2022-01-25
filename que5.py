n=int(input("enter the number:-"))
i=1
even=0
odd=0
while i<=n:
    if i%2==0:
        even+=1
    else:
        odd+=1
    i=i+1
print("even=",even)
print("odd",odd)