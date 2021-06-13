l = int(input("enter length of string : "))  

s = input("enter string   : ")

l1 = len(s)

# print(l1)
n = l
while n!=1:  # for l is only power of 2  
    n = n/2
    
if(n==1):  
    DOS  = 0  # DOS = degree os symetry 
    
    if(l1==l):  # to check that length of string is correct or not 
        s1 = s[int(l1/2):] 
        # print(s1)
        
        s2 = s[:int(l1/2)]
        # print(s2)
        if(s1 == s2):
            DOS = DOS +1
            l2 = l1/2
            while l2>1:
                l2 = l2/2
            
                s1 = s1[int(l2):] 
                # print(s1)
            
                s2 = s2[:int(l2)]
                # print(s2)
            
                while (s2 == s1):
                    DOS = DOS + 1
            
            
        print(DOS)
        
    else:
        print("Enter right value!!")
else:
    print("Enter a valid string lenght!!")
     
    
    
    
    
