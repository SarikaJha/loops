n=int(input("enter the number:-"))
i=1
while i<=n:
    if n%2==0:
        print(n,"even")
    else:
        a=n//2
        b=0
        while b<a:
            print(n,"odd")
            b=b+1
        break
    i=i+1