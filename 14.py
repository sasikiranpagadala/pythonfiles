n=int(input("Enter a number: "))
flag=1
for i in range(2,n):
	if(n%i==0):
		print(f"{n} is not a prime")
		flag=0
		break
if(flag): print(f"{n} is a prime")
