# i=int(input("enter the number:-"))
# a=i
# sum=0
# while i>0:
#     sum=sum+(i%10)*(i%10)*(i%10)
#     i=i//10
# if a==sum:
#     print("number is armstrong")
# else:
#     print("number is not armstrong")

num=int(input("enter the number:-"))
length=len(str(num))
var=num
sum=0
while var>0:
    digit=var%10
    sum+=digit**length
    var=var//10
if sum==num:
    print(num,"is an Armstrong Number")
else:
    print(num,"is not an Armstrong Number")