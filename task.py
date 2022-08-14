

def f_gen(n):
    fac = 1
    if n == 0:
        yield 0
    for i in range(1, n+1):
        if i == 1:
            fac = 1
        else:
            fac = fac * i
        yield fac


e = f_gen(0)
for i in e:
    print(i)
