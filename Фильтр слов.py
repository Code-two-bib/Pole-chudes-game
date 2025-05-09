def filt():
    text = list()
    a = open('words.txt', 'r', encoding='UTF-8')
    for i in a:
        b = i.strip()
        if 5 < len(b) >= 8:
            if "-" in b:
                pass
            else:
                text.append(b)
    a.close()
    return text
