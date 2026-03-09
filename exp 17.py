import string
from collections import Counter
import matplotlib.pyplot as plt

feedback = [
    "The product is very good",
    "Good quality and service",
    "Product quality is good",
    "Service is slow but product is good"
]

text = " ".join(feedback).lower()
text = text.translate(str.maketrans('', '', string.punctuation))

stop = ["the","and","is","but"]
words = [w for w in text.split() if w not in stop]

freq = Counter(words)
top = freq.most_common(5)

print(top)

w,c = zip(*top)
plt.bar(w,c)
plt.show()
