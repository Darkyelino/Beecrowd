N = int(input())
a, b = 0, 1
count = 1
output = str(a)
while count < N:
    output += " " + str(b)
    a, b = b, a + b
    count += 1
print(output)