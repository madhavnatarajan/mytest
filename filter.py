l=[-1,2,-3,4,-5]
f=list(filter(lambda x:x>0,l ))
print(f)
s='hello world'
g=list(filter(lambda x:x not in 'aeiou',s))
print(g)