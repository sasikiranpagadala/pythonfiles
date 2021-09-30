n=input("Enter input: ")
try:
	float(n)
	print(f"{n} is a number.")
except ValueError:
	print(f"{n} is not a number.")