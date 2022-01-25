a=int(input("enter number a"))
b=int(input("enter number b"))
c=int(input("enter number c"))
if a>=b and a<=c or a<=b and a>=c:
    print("a is 2nd maximum")
elif b>=a and b<=c or b<=a and b>=c:
    print("b is 2nd maximum")
else:
    print("c is 2nd maximum")