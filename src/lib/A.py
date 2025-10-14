def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё','Е')
    text = text.strip()
    spec_symb = ['\\t', '\\r', '\\n', '\\w', '\\f', '\\d', '\\v']
    for symb in spec_symb:
        text = text.replace(symb, ' ')
    words = text.split()
    text = ' '.join(words)
    return text



def tokenize(text: str) -> list[str]:
    cleaned = text.replace(',', ' ').replace('.', ' ').replace(':', ' ').replace(';', ' ').replace('!', ' ').replace('?', ' ')
    words = cleaned.split()
    filtered = []
    for word in words:
        if not word[0].isdigit() and not word[0].isalpha():
            pass
        else:
            filtered.append(word)
    return filtered



def count_freq(tokens: list[str]) -> dict[str, int]:
    unic_t = list(set(tokens))
    count_t = []
    for i in unic_t:
        count_t.append(tokens.count(i))
    dict_t = dict(zip(unic_t,count_t))
    return dict_t

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    top = sorted(list(freq.items()), key=lambda x: (-x[1], x[0])) [:n]
    return top




 test_case_normalize = ['ПрИвЕт\nМИр\t', 'ёжик, Ёлка', 'Hello\r\nWorld', '  двойные   пробелы  ']

 for i in test_case_normalize:
     print(normalize(i))

 test_case_tokenize = ['привет мир', 'hello,world!!!', 'по-настоящему круто', '2025 год', 'emoji 😀 не слово']
 for n in test_case_tokenize
     print(tokenize(n))


 test_case_count_freq =[["a","b","a","c","b","a"]]
 for n in test_case_count_freq:
    print(top_n(n))