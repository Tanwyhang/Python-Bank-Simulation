import time
import os

# index
name, password, balance = 0, 1, 2
logged_in = False

# read data
fdata = open('accounts.txt', 'r')
data = fdata.read()
fdata.close()
data = data.split()
data = [x.split(':') for x in data]
for i in data:
    i[balance] = float(i[balance])

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def log(x):
    print(f'--{str(x)}!!--')
    time.sleep(1.5)
    os.system('cls')

def header(x):
    print(f'--{x}--')
    print('-' * 20)

def login(username, passw):
    for i, x in enumerate(data):
        if x[name] == username and passw == x[password]:
            return [log('logged in'), i]
    return False

def register():
    os.system('cls')
    header('Registration site')
    username = input('Username: ')
    password = input('Password: ')
    balance = input('Balance: ')
    if username != '' and password != '' and isfloat(balance) and username not in [x[name] for x in data]:
        fdata = open('accounts.txt', 'a')
        fdata.write(f'{username}:{password}:{balance}\n')
        fdata.close()
        log('User successfully registered, proceed to login')
    else:
        log('Failed to register')

while not logged_in:
    header('Goofy ahh bank simulation')
    if input('1 login\n2 register\n>') == str(1):
        logged_in = login(input('Username: '), input('Password: '))
        if not logged_in:
            log('Username and password does not match')
            continue
    else:
        register()
        fdata = open('accounts.txt', 'r')
        data = fdata.read()
        fdata.close()
        data = data.split()
        data = [x.split(':') for x in data]
        for i in data:
            i[balance] = float(i[balance])

    while logged_in:
        header('User info')
        userindex = logged_in[1]
        userdat = data[userindex]
        print(f'Username: {userdat[name]}\n' + 'Password: ' + '*' * len(userdat[password]) + '\n' + f'Balance: {userdat[balance]}')
        print('1 Withdraw\n2 Deposit\n3 Change password\n4 logout')
        query = input('>')
        if query == str(3):
            if input('Old password: ') == userdat[password]:
                newpass = input('New password: ')
                dat = open('accounts.txt', 'r')
                lines = dat.readlines()
                dat.close()
                dat = open('accounts.txt', 'w')
                for i in range(len(lines)):
                    if i != userindex:
                        dat.write(lines[i])
                dat.write(f'{userdat[name]}:{newpass}:{userdat[balance]}\n')
                dat.close()
                log('Password changed')
                logged_in = False
            else:
                log('incorrect password')
        elif query == str(2):
            deposit_amount = input('Deposit amount: ')
            if isfloat(deposit_amount):
                dat = open('accounts.txt', 'r')
                lines = dat.readlines()
                dat.close()
                dat = open('accounts.txt', 'w')
                for i in range(len(lines)):
                    if i != userindex:
                        dat.write(lines[i])
                dat.write(f'{userdat[name]}:{userdat[password]}:{float(userdat[balance]) + float(deposit_amount)}\n')
                dat.close()
            else:
                log('invalid')
        elif query == str(1):
            withdraw_amount = input('Withdraw amount: ')
            if isfloat(withdraw_amount) and float(withdraw_amount) <= float(userdat[balance]):
                dat = open('accounts.txt', 'r')
                lines = dat.readlines()
                dat.close()
                dat = open('accounts.txt', 'w')
                for i in range(len(lines)):
                    if i != userindex:
                        dat.write(lines[i])
                dat.write(f'{userdat[name]}:{userdat[password]}:{float(userdat[balance]) - float(withdraw_amount)}\n')
                dat.close()
            else:
                log('invalid')
        elif query == str(4):
            logged_in = False

        fdata = open('accounts.txt', 'r')
        data = fdata.read()
        fdata.close()
        data = data.split()
        data = [x.split(':') for x in data]
        os.system('cls')
