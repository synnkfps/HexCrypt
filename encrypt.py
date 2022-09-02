alphabet = 'abcdefghijklmnopqrstuvwxyz'
dictionary = {}

for i in enumerate(alphabet):
    dictionary[i[1]]=hex(i[0])
    

string = input(f'Digite um texto para ser encriptado: ')

# Encrypt 1
encrypt1 = ''
for i in string:
    if i not in alphabet:
        encrypt1 += i
    else:
        encrypt1 += dictionary[i.lower()]

# Encrypt 2
encrypt2 = ''
for i in string:
    if i not in alphabet:
        encrypt2 += i 
    else:
        encrypt2 += str(dictionary[i.lower()]).replace('0x', '')

print(encrypt1)
print(encrypt2)
