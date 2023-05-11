raw_text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

def n_gram(raw_list: list or str, n: int) -> list:
    return [raw_list[i:i + n] for i in range(len(raw_list) - n + 1)]

def word_n_gram(raw_text: str, n: int) -> list:
    return n_gram(raw_text.replace(',', '').replace('.', '').split(), n)

def str_n_gram(raw_text: str, n: int) -> list:
    return n_gram(raw_text.replace(',', '').replace('.', ''), n)

def word_bi_gram(raw_text: str) -> list: return word_n_gram(raw_text, 2)

def str_bi_gram(raw_text: str) -> list: return str_n_gram(raw_text, 2)

print(word_bi_gram(raw_text))
print(word_n_gram(raw_text, 3))

test = "I am an NLPer."
print(word_bi_gram(test))
print(str_bi_gram(test))
print(word_n_gram(test, 3))
print(str_n_gram(test, 3))
