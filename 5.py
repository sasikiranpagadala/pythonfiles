a,b,c=map(int,input("Enter three values: ").split())
sol1=(-b+((b**2-4*a*c)**0.5))/2*a
sol2=(-b-((b**2-4*a*c)**0.5))/2*a
print(f"solution 1: {sol1},solution 2: {sol2}")