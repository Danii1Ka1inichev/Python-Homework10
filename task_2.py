
def gen_range(first, last, step=0):
    sstep = 0
    while True:
        if sstep == 0:
            yield first
            if step == 0:
                first += 1
            sstep = step
            # sstep -= 1
        if sstep != 0:
            first += 1
            sstep -= 1
        if first == last:
            break


ra = gen_range(1, 12)
for i in ra:
    print(i)
print('_____________')
for i in range(1, 12):
    print(i)