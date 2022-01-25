# i = 1
# sum=0
# n = int(input("Enter a number: "))
# while(i <= n//2 ):
#     if (n % i == 0) :
#         sum += i
#     i += 1
# if sum == n :
#     print(n,"is a perfect number")

# else :
#     print(n,"is not a perfect number")

# n=int(input("enter a number:-"))
# i=1
# sum=0
# while i<=n//2:
#     if n%i==0:
#         sum=sum+i
#     i=i+1
# if sum==n:
#     print("perfect number")
# else:
#     print("not perfect")



num =int (input ("enter the number"))
i=1
while i<=10:
    if i%num:
        num =i*num
        print(i)
        i=i+1