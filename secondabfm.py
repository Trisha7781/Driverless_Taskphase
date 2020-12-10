a=[]
n=int(input("Enter No of Elements"))
print("Enter elements")
for i in range(0,n):
    el=int(input())
    a.append(el)
tup=tuple(a)
print (tup)
b=[]
for j in a:
    if j not in b:
        b.append(j)
tup=tuple(b)
print("Modified Tuple",tup)
def Sum(N):
    if len(N)==0:
        return 0
    else:
        return N[0]+ Sum(N[1:])
print("SUM=", Sum(tup))
