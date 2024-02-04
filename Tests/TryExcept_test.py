username = input('Username: ')
try:
    number = int(username)
    print(number)
except:
    print('Invalid Username')