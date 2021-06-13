T = int(input("Enter the nuber of test case : "))


for i in range(1,T+1):
    N = int(input("Enter the size of pattern : "))
    k = int((N-1)/2) 
    print("*"*N)
    for i in range(1,N+1):
        
        print("*"*(int((N-(2*i-1))/2)), end=' '*(2*i-1))
       
        print("*"*(int((N-(2*i-1))/2)))
        i = i + 1
    
        if(int((N-(2*i-1))/2)<1):
            break
    while k>1:
        k -= 1
        print("*"*(int((N-(2*k -1))/2)), end=' '*(2*k-1))
        print("*"*(int((N-(2*k-1))/2)))
        
    print("*"*N)
    
    # or 
#     import numpy as np 
# T = int(input("Enter the nuber of test case : "))

# N = np.ndarray(shape=(T,),dtype=int)

# for i in range(0,T):
#     N[i] = int(input("Enter the size of pattern : "))
# # for i in range(0,T):
# #     print(N[i])
# for i in range(0,T):    
#     k = int((N[i]-1)/2) 
#     print("*"*N[i])
#     for j in range(1,N[i]+1):  # for print upper half stars
        
#         print("*"*(int((N[i]-(2*j-1))/2)), end=' '*(2*j-1))
       
#         print("*"*(int((N[i]-(2*j-1))/2)))
#         j = j + 1
    
#         if(int((N[i]-(2*j-1))/2)<1):
#             break
#     while k>1:    #  for print lower half stars
#         k -= 1
#         print("*"*(int((N[i]-(2*k -1))/2)), end=' '*(2*k-1))
#         print("*"*(int((N[i]-(2*k-1))/2)))
        
#     print("*"*N[i])
# #     print("\n")


       
        
    


        
        
    



