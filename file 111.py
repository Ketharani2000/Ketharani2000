num=int(input("Input number: "))
count=0
if num<2:
    print("Invalid number")
else:
    for j in range(2,num+1):
        proper_divisors=[]
        total=0
        for i in range(1,j):
            if j%i==0:
                proper_divisors.append(i)
        for k in proper_divisors:
            total+=k
        if total>j:
            count+=1
print("Number of abundant numbers from 1 to",num,"is",count)            
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
