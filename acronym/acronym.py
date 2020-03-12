def abbreviate(words):
    x = words.replace('-', ' ').replace('_', ' ').replace("'", '').title()
    return "".join(n for n in x if n.isupper())
