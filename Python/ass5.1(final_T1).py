largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    
    if num == "done":
        break 
    
    try:
        inp=int(num)
        
    except:
        print("Invalid input")
        continue
        
    if smallest is None:
        smallest=inp
    elif inp<smallest:
        smallest=inp
        
    if largest is None:
        largest=inp
    elif inp>largest:
        largest=inp
                
        
   

print("Maximum is", largest)
print("Minimum is", smallest)