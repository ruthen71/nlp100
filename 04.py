raw_text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
text = raw_text.replace(',', '').replace('.', '')
one_word_index = [1, 5, 6, 7, 8, 9, 15, 16, 19]
word_to_index = {(word[:1] if i in one_word_index else word[:2]): i for i, word in enumerate(text.split(), 1)}
print(word_to_index)
print(word_to_index['H'])
print(word_to_index['He'])
