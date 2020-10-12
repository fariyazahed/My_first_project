word = 'mypassword'
password = ''

for i in range(len(word)):
    if word[i] == 'o':
        password = password + '!'
    elif word[i] == 'B':
        password = password + '@'
    elif word[i] == 'm':
        password = password + 'M'
    elif word[i] == 'a':
        password = password + '8'
    elif word[i] == 'i':
        password = password + '.'
    elif word[i] == 's':
        password = password + '$'
    else:
        password = password + word[i]

new_pass = password + 's!d'
print(new_pass)
