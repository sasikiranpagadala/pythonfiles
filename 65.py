string=input("Enter a string: ")
start,end=map(int,input("Enter index of start and end points: ").split())
print(string[start:end+1])