import os
import getpass
user = getpass.getuser()


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
print('Welcome to Kh0p3sh, a commandline tool built for penetration testers.')
print('======================================================================')

print('Kh0p3sh Console:')
print('For list of commands type help')

while True:
    command = input('\033[1;31;40m' + user + '\033[0m' + '\033[1;34;40m@Kh0p3sh-console\033[0m>')
    if str(command) == 'help':
        print('''
    
    ==================
    Available Commands
    ==================

    ==============================================
    Neutral Commands
    ----------------------------------------------
    help - shows available commands and their uses
    exit - will exit out of the Kh0p3sh Console
    hax0r - give you encouraging thoughts!
    ==============================================

    ==============================================
    Vulnerability Assessment Commands
    ----------------------------------------------
    firewall - will check if firewall is up
    findSUID - will list all SUID files found
    findGUID - will list all GUID files found
    getRules - will list all iptables rules
    get
    ==============================================

        ''')
    elif str(command) == 'exit':
        print('Goodbye!')
        break
    elif str(command) == 'hax0r':
        print('you are a hax0r')
    
#################END OF NEUTRAL COMMANDS##################




    else:
        print('Command does not exist! try the "help" command')