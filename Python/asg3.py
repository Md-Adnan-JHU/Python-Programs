#assignment 3.3

score=input("enter score:")
s= float(score)
if s>1.0:
    print("error")
    exit()
if s<0.0:
    print("error")
    exit()    
elif s>=0.9:
    print("A")
elif s>=0.8:
    print("B")
elif s>=0.7:
    print("C")
elif s<0.6:
    print("F")