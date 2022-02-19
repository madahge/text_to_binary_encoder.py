text_to_conv = input("Type that you want to Convert" )

print("The original string is : " + str(test_to_conv))

res = ''.join(format(i, '08b') for i in bytearray(test_to_conv, encoding ='utf-8'))

print("The string after binary conversion : " + str(res))
