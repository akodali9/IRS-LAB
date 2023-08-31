def generate_ngrams(text, n):
    words = text.split()
    words.insert(0,"#")
    print(words)
    ngrams = []
    if(len(words) % 2 != 0):
        words.append("#")
    for i in range(0, len(words) - n + 1):
        ngram = ' '.join(words[i:i + n])
        ngrams.append(ngram)
    return ngrams


text = input("Enter sentence: ")
n = int(input("n-gram n value: "))

ngrams = generate_ngrams(text, n)
for ngram in ngrams:
    print(ngram)