l=eval(input('Enter a list: '))
c_size=int(input('Enter chunck size: '))
print([l[i:i+c_size] for i in range(0,len(l),c_size)])