
fh = open('data/data2.txt', 'r')
text = fh.read()
words = text.split()
counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)
big_count = None
big_word = None
for word, count in counts.items():
    if big_count is None or count > big_count:
        big_word = word
        big_count = count
        print('--------'*3)

        print(big_word, big_count)
