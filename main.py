from func import *
import getpass
import os

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
#################START OF NEUTRAL COMMANDS##################
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
    ufw - will check if ufw is installed is up
    findSUID - will list all SUID files found
    findSGID - will list all SGID files found
    getRules - will list all iptables rules
    memCheck - will check for any memory security measures in place (useful for pwning or privelage escalation)
    ==============================================

    ==============================================
    Persistence Commands
    ----------------------------------------------
    bashBack - will attempt to setup a bash backdoor
    ncBack - will attempt to setup a netcat backdoor
    createSUID - will attempt to create a file with SUID priveleges
    ==============================================    
        ''')

    elif str(command) == 'exit':
        print('Goodbye!')
        break
    elif str(command) == 'hax0r':
        print('you are a hax0r')
#################END OF NEUTRAL COMMANDS##################

#################START OF VULN ASSESSMENT COMMANDS##################
    elif str(command) == 'ufw':
        if ufw_check() == True:
            print('The \033[1;31;40mUncomplicated Firewall\033[0m IS enabled')
        else:
            print('The \033[1;31;40mUncomplicated Firewall\033[0m IS NOT enabled')

    elif str(command) == 'findSUID':
        if suid_check() == False:
            print('No files with \033[1;31;40mSUID\033[0m permissions found')
        else:
            print('============Finding ALL files with SUID permissions set============')
            print(suid_check())
            print('======================================================')

    elif str(command) == 'findSGID':
        if suid_check() == False:
            print('No files with \033[1;31;40mSGID\033[0m permissions found')
        else:
            print('============Finding ALL files with SGID permissions set============')
            print(sgid_check())
            print('======================================================')

    elif str(command) == 'getRules':
        if suid_check() == False:
            print('No IPtables rules found')
        else:
            print('============Listing ALL iptables rules============')
            print(rules_check())
            print('======================================================')

    elif str(command) == 'memCheck':
        print(mem_check())

    else:
        print('Command does not exist! try the "help" command')