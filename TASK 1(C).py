n = 0 

n = int(input())        
r = int(input())
x = int(input())
y = int(input())

# n,r,x,y = input().split()
# n = int(n)
# x =int(x)
# r =int(r)
# y = int(y)
c = 0 
s = 0
l1 = [] # to make list of ci
l2 = []  # to make lisk of si
b =  0  # let for check for increasing 

l = 0 # let to check for decreasing 


for i in range(n):
    c = input()
    l1.append(c)
 
for i in range(n):    
    s = input()
    l2.append(s)
for i in range(n):
    # print(l1[i])
    if(l1[i] == '1' and l2[i] == '1'):
        b +=x
# print(b)
for i in range(n):
    # print(l2[i])
    if((l1[i] == '1' and l2[i] == '0') or (l2[i] == '1'and l1[i] == '0')):        
        l += y
# print(l)

if(r+b-l > r):
    print("promoted")
elif(r+b-l < r):
    print("demoted")
elif(r+b-l  == r):
    print("no change")



