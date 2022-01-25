# 1.Numbers that are divisible by 3, you have to print "Nav".
# 2.Numbers that are divisible by 7 so that "Gurukul" is printed.
# 3.Numbers that are divisible by both 3 and 7, print "NavGurukul" there.
# 4.If the number does not come in the above three cases then print the number only.
i=1
while i<=100:
    if i%3==0 and i%7==0:
        print("navgurukul")
    elif i%3==0:
        print("nav")
    elif i%7==0:
        print("gurukul")
    else:
        print(i)
    i=i+1