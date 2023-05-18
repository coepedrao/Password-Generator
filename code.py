import random
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowcase_letters = uppercase_letters.lower()
digits = '0123456789'
symbols = '() { [] / ? . : , + = - _ '

upper, lower, nums, syms = True, True, True, True

all = ''

if upper:
    all += uppercase_letters
if lower:
    all += lowcase_letters
if nums:
    all += digits
if syms:
    all+= symbols

length = 20
amount = 10

print('Aqui estão suas senhas: ')
for x in range(amount):
    password = ''.join(random.sample(all, length))
    print(password)
    
