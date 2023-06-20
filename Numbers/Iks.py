import math
n_numbers = int(input())
inp = list(map(int, input().split()))

factors_list = [None] * n_numbers
fact_count = {}

for n in range(n_numbers):
    dct = {}
    while inp[n] % 2 == 0:
        inp[n] = inp[n] // 2

        if not 2 in dct:
            dct[2] = 1
        else:
            dct[2] += 1


        if not 2 in fact_count:
            fact_count[2] = 1
        else:
            fact_count[2] += 1
    for i in range(3, inp[n] + 1, 2):
        while inp[n] % i == 0:
            inp[n] = inp[n] // i

            if not i in dct:
                dct[i] = 1
            else:
                dct[i] += 1

            if not i in fact_count:
                fact_count[i] = 1
            else:
                fact_count[i] += 1
    factors_list[n] = dct

opp_count = 0
gcd = 1
for key in fact_count:
    repeating = fact_count[key] // n_numbers
    gcd = gcd * (key ** repeating)
    for elem in factors_list:
        if not key in elem:
            opp_count += repeating
        elif elem[key] < repeating:
            opp_count += repeating - elem[key]

print(gcd, opp_count)

