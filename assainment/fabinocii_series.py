def fabinocci(n):
    a = 0
    b= 1
    c = 0
    print(a)
    print(b)
    for i in range(2,n+1):
        c = a + b
        a = b
        b = c
        print(c)
    return c
n = int(input('enter +ve number:   '))
if n<=0:
    print('please enter +ve number')
else:
    x = fabinocci(n)
    print('fabinocci of ',n,'number is ',x)

