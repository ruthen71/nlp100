import random

def word_shuffle(s: str) -> str:
    slist = s.split()
    res = []
    for word in slist:
        print(word)
        if len(word) > 4:
            word = word[0] + ''.join(random.sample(list(word[1:-1]), len(word[1:-1]))) + word[-1]
        res.append(word)
    return ' '.join(res)

text = "I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(word_shuffle(text))

