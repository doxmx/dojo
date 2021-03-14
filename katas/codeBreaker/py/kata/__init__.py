# Implement functions here

def encrypt(arg):
    result = ''
    alphaSet = 'abcdefghijklmnopqrstuvwxyz'
    keySet = '!)"(£*%&><@abcdefghijklmno'
    for argKey in arg:
        alphaIndex = alphaSet.find(argKey)
        if alphaIndex != -1:
            result += keySet[alphaIndex]
        else: 
            result += ' '

    return result

