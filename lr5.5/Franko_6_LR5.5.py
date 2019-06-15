for i in range(100,10000):
    if len(str(i))==3:
        k=i
        num1 = k%10
        k = k//10
        num2 = k%10
        k = k//10
        num3 = k%10
        if i == num1**3+num2**3+num3**3:
            print(i)
    elif len(str(i))==4:
        k=i
        num1 = k%10
        k = k//10
        num2 = k%10
        k = k//10
        num3 = k%10
        k = k//10
        num4 = k%10
        if i == num1**4+num2**4+num3**4+num4**4:
            print(i)
