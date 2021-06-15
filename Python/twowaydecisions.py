#twowaydecisions
#you have to use float() funtion always if you are using input function because it takes string


x=input("enter the value of x")
if float(x)>2:
    print("bigger")
if float(x)==2:
    print("equal")             #u can also use else statement after if in two way decisions
if float(x)<2:
    print("smaller")
print("all done")        