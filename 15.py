a,b=map(int,input("Enter range as two values: ").split())
for j in range(a,b+1):
	flag=1
	for i in range(2,j):
		if(j%i==0):
			flag=0
			break
	if(flag): print(j,end=' ')