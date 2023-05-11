def n_gram(raw_list: list or str, n: int) -> list:
    return [raw_list[i:i + n] for i in range(len(raw_list) - n + 1)]

def word_n_gram(raw_text: str, n: int) -> list:
    return n_gram(raw_text.replace(',', '').replace('.', '').split(), n)

def str_n_gram(raw_text: str, n: int) -> list:
    return n_gram(raw_text.replace(',', '').replace('.', ''), n)

def word_bi_gram(raw_text: str) -> list: return word_n_gram(raw_text, 2)

def str_bi_gram(raw_text: str) -> list: return str_n_gram(raw_text, 2)

a = "paraparaparadise"
b = "paragraph"
X = str_bi_gram(a)
Y = str_bi_gram(b)
print(X, Y)
print(set(X) | set(Y))
print(set(X) & set(Y))
print(set(X) - set(Y))
print("se" in X)
print("se" in Y)