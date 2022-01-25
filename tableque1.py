#if we enter any number as user input it should print table upto that specific number given in user input.
user_input=int(input("enter the number:-"))
i=1
while i<=user_input:
    j=1
    while j<=10:
        print(i,"*",j,"=",i*j)
        j=j+1
    i=i+1
    print()
