hrs=input("enter hours")
rph=input("enter rate per hours")
a=float(hrs)
b=float(rph)
def computepay(a,b):
    x=40*b
    y=(a-40)*(1.5)*b
    added=x+y
    return added

print("pay", computepay(a,b))    