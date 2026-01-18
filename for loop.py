n=int(input("Enter a number thats factor you want to find:"))
i=1
for i in range(1,n+1):
    if n%i==0:
        print(i)