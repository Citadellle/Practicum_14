num = int(input())

divs = set()

for i in range(1, int(num ** 0.5) + 1):
    if num % i == 0:
        divs.add(i)
        divs.add(num // i)

print(sorted(list(divs)))