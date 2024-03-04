import random

# генерирует случайный пароль заданной длины из заданных символов
pwd_chars='0123456789'
pwd_len=6
pwd=''
for i in range(pwd_len):
    pwd+=random.choice(pwd_chars)
print(pwd)
