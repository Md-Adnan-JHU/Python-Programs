count=0
sum=0
while True:
    num=input("Enter The Numbers: ")
    if num == "done":
        break
    try:
        x=int(num)
    except:
        print("Invalid Number")
        continue
    count=count+1
    sum=sum+x
print("Count is ", count)
print("Sum is ", sum)            
print("Average is ", sum/count)