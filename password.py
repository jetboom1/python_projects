def passworddifficulty(a: 'password'):
    """Определяет надежность пароля и возвращает True если:
    1. длина 10 символов и более;
    2.должен иметь хотя бы одно число;
    3.должен иметь хотя бы одну букву в верхнем регистре;
    4.должен иметь хотя бы одну букву в нижнем регистре;
    5.пароль может содержать только латинские буквы."""
    latinalphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w',
                     'x','y','z','1','2','3','4','5','6','7','8','9','0'}
    a = str(a)
    for i in a:
        if len(a) < 10 or a.isdigit() == True or a.isalpha() == True or a.isupper() == True or a.islower() == True or i.lower() not in latinalphabet:
            return False
        else:
            return True


a = input('введите пароль: ')
print(passworddifficulty(a))
