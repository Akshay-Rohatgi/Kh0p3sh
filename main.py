import os
import getpass
getpass.getuser()


print('''
==========================================================
  _  ___      ___       ____      _     
 | |/ / |    / _ \     |___ \    | |    
 | ' /| |__ | | | |_ __  __) |___| |__  
 |  < | '_ \| | | | '_ \|__ </ __| '_ \ 
 | . \| | | | |_| | |_) |__) \__ \ | | |
 |_|\_\_| |_|\___/| .__/____/|___/_| |_|
                  | |                   
                  |_|                   
==========================================================

    ''')

print('Kh0p3sh Console:')
print('For list of commands type help')

while True:
    command = input('>')
    if str(command) == 'help':
        print('Available Commands:')
        print('''
        help - shows available commands and their uses
        exit - will exit out of the Kh0p3sh Console
        hax0r - will spam cool text to make it look like you are an epic hacker
        ''')
    elif str(command) == 'exit':
        print('Goodbye!')
        break
    elif str(command) == 'hax0r':
        print('you are a hax0r')
    else:
        print('Command does not exist! try the "help" command')