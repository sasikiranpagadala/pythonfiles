text=input("Enter something to enter into a file: ")
with open('kiran.txt','a') as file:
	file.write(text)
with open('kiran.txt','r') as file:
	for i in file:
		print(i)