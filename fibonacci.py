def fib(n):
    if n<=1:
        return 1
    else:
        return (fib(n-1)+fib(n-2))
n=int(input('enter the no of fibonacci terms:'))            
for i in range(1,n+1):

    f=fib(i)
    print(f)