def arr(A):
	xor = 0
	count=0
	for i in A:
		xor ^= (1<<i)
	for i in A:		
		if (xor & (1<<i) !=0):
			count+=1
			xor ^= (1<<i)
	return count

for i in range(int(input())):
	n,m,q = map(int,input().split())
	lisrow =[]
	liscol=[]
	for j in range(q):
		x,y = map(int,input().split())
		lisrow.append(x)
		liscol.append(y)
	count1 = arr(lisrow)
	count2 = arr(liscol)
	print (count1*m + count2*n - 2*count1*count2)

