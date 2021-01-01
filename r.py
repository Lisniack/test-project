import json
p = []
for i in range(1, 5):
    p.append(i)

l = []
for k in range(6, 10):
    l.append(k)
for num in enumerate(l, 1):
    print(f'{num}')
for nur in enumerate(p, 1):
    print(f'{nur}')
    


