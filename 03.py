text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
replaced_text = text.replace(',', '').replace('.', '')
wclist = [len(word) for word in replaced_text.split()]
print(wclist)
