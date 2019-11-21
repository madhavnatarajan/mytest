n=int(input('enter a no you want the factorial of:'))          
def factorial(n):
    if n==0:
        return 1 #base condn 1
    elif n==1:
        return 1 #base condn 2
    else:
        return n*factorial(n-1)
f= factorial(n)
print(f)
   