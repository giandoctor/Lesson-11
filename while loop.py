n=int(input("Enter a number thats factor you want to find:"))
i=1
while i<=n:
    if n%i==0:
        print(i)
    i=i+1