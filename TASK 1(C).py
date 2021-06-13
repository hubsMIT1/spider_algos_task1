n = int(input("Enter number of days : "))
r = int(input("Enter intial amount : "))
x = int(input("Enter Money which will increase after successful workshop : "))
y = int(input("Enter Money which will decrease after unseccessful workshop : "))
b =  r  # let for check 

for i in range(n):
    c = int(input("Enter 1 if contest takes place on %dth day  otherwise enter 0 : " %(i+1)))
    s = int(input("Enter 1 if the team eat pizza on %dth day otherwise enter 0 : " %(i+1)))
    if(c==1 and s ==1):
    
        b += x
    elif((c==0 and s == 1) or (s==1 and c == 0)):
        b -= y
    else:
        b = r 
if(b>r):
    print("promoted")
elif(b<r):
    print("demoted")
else:
    print("no change")
    



