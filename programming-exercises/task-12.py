def getSign(sign):
    if(sign == 'o'):
        return '0'
    elif(sign == 'e'):
        return '3'
    elif(sign == 'i'):
        return '1'
    elif(sign == 'a'):
        return '4'
    else:
        return sign

sentencja = input("Podaj sentencję: ")

sentencja_zamieniona = ''.join(getSign(i) for i in sentencja)

print("Zamieniona sentencja:", sentencja_zamieniona)
