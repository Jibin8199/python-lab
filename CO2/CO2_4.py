import math
p=[]
even=[]
m=int(input("Enter starting :"))
n=int(input("Enter ending :"))
for i in range(m,n) :
    if math.sqrt(i) % 1 == 0 :
        p.append(i)
print("perfect square numbers are :",p)        
for x in p :
    c=0
    num=x
    while num > 0 :
        d=num % 10 
        if d in [0,2,4,6,8]:
            c+=1
        num=int(num/10) 
    if c == 4 :
        even.append(x) 
print("\n\nEven digit perfect square numbers are :",even)               