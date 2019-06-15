def cipher(s, a):
    alphabet = ('а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
                'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я')
    result = ''
    for i in s.lower():
        if i not in alphabet:
            result+=i
            continue
        if alphabet.index(i) + int(a) > len(alphabet)-1:
            result += alphabet[alphabet.index(i) + int(a) - len(alphabet)]
        else:
            result += alphabet[alphabet.index(i) + int(a)]
    return result

def decipher(s,a):
    alphabet = ('а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
                'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я')
    result = ''
    for i in s.lower():
        if i not in alphabet:
            result += i
            continue
        result += alphabet[alphabet.index(i) - int(a)]
    return result
s = input('введите строку')
a = int(input('введите сдвиг'))
print(cipher(s, a))
print(decipher(s, a))