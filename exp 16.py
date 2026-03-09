reviews = [
    "This product is good",
    "Good quality product",
    "This product is very good"
]

freq = {}

for r in reviews:
    for w in r.lower().split():
        freq[w] = freq.get(w, 0) + 1

print(freq)
