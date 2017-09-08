def n_sum(a,n):
    sum=0
    i=0
    while int(i)<int(n):
        sum+=a[i]
        i=i+1

    return sum

n=input('Enter howmany elements:')
print('enter the elements')
a=[]
i=0
while int(i)<int(n):
    x=input()
    a.append(x)
    i=i+1

z=n_sum(a,n)
print('sum={0}'.format(z))

        
