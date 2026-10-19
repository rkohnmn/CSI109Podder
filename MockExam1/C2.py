temps=[72,75,68,81,79,77,70]

a = 0
c = 0
for i in range(len(temps)):
    b = temps[i]
    if b > a:
        a = b
        c = i+1

print(str(a) + " degrees on day " + str(c))