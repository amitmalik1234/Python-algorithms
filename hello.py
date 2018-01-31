print('Testing:GitHub with Visual Studio Code')



print("Hello")

a = "Hi"
b="a"

val = ord(b)
print(val)


def GetAsciiVal():
    str_Len = len(a)
    chars = list(a)

    asciiVal =0
    for i in range(str_Len):
        asciiVal = asciiVal + ord(chars[i])
    return asciiVal
 
asciiVal = GetAsciiVal()


print("Convert Hi -- > " + str(asciiVal))
