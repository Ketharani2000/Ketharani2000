dimension=input("Enter the dimension: Enter Matrix A: \n").split(",")
A=[]
B=[]
BT=[]
ABT=[]
def insert_matrix(q):
    r=0
    while True:
        p=input().split()
        try:
            if len(p)!=int(dimension[1]):
                a=2/0
        except:
            print("Invalid Matrix")
            continue
        q.append([int(i) for i in p])
        r+=1
        if r<int(dimension[0]):
            continue
        else:
            break
"""def get_transpose():
     for i in range(int(dimension[1])):
        trans=[]
        for j in B:
            trans.append(j[i])
        BT.append(trans)
get_transpose()"""
insert_matrix(A)
print("Enter Matrix B: ")
insert_matrix(B)
for i in A:
    row_ABT=[]
    for j in B:
        element=0
        for k in range(int(dimension[1])):
            element+=i[k]*j[k]
        row_ABT.append(element)
    ABT.append(row_ABT)
for m in ABT:
    for n in range(int(dimension[0])):
        print(m[n],end=" ")
    print()






            
            
