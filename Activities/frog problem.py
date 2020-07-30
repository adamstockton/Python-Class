import random

river_width = 10
cap = 500000
results = []

for i in range(cap):
    total = 1
    spot = random.randint(0, river_width - 1)
    while(spot < 9):
        spot += random.randint(1, ((river_width - 1) - spot))
        total += 1
    results.append(total)

print(round(sum(results) / len(results), 2))