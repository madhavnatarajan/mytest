a=['karnataka','tamilnadu','karnataka','karnataka','kerala','tamilnadu']
b=['bangalore','chennai','hassan','mysore','trivandrum','madurai']
def dictionary():
    d={}
    i=0
    d[a][i]=b[i]
    i+=1
    return d
print(dictionary())