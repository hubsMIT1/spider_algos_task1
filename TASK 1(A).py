E = int(input("enter the total number of digit of any binary number : "))

B = int(input("Enter binary number : "))

d = 0  # d is for 
dec = 0 # dec is decimal of number entered binary 
i = 0

l = 0 # l is length of entered binary

   
l = len(str(B))
# print(l)


if(E == l):
    while(B!=0):
        d = B % 10
        dec = dec + d * pow(2,i)
        B = B//10
        i = i + 1
    # print(dec)
    
    j = 1  
    p = 0  # p is for power on 2  

    sums = 0  # sums is for summation of all 2^n-1
  
    for j in range(1,E+1):
        p = E - j 
        sums = sums + pow(2, p)
        
    # print(sums)
    
    s2  = 0 # s2 for value of  2^n-1
    s2 = pow(2, (E-1))
   
    if(dec == s2 or dec == sums):
        print("not possible!!")
        
    else: 
        N1 = dec - 1
        N2 = dec + 1 
        print(bin(N1)[2:]) # as average of this 
        print(bin(N2)[2:])  # And this 
    
      
# for all average value         
        # N1 = dec 
        # N2 = dec
        
        # i = 1
        
        # while(N1 >= s2 and N2 < sums ):
        #     N1 = dec - i 
        #     N2 = dec + i 
        #     i += 1
        #     # print("N1")
        #     print(bin(N1)[2:])
        #     print(bin(N2)[2:])
        #     print("\n")
        
        
else:
    print("Enter values again!!")

