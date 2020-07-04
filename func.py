import os
import subprocess

def line_in_file(path, string):
    try:
        with open(path, 'r') as handle:
            for line in handle:
                if string in line:
                    return True
    except: return False

def ufw_check():
    try:
        handle = subprocess.getoutput("sudo ufw status | grep 'Status: active'")
        if handle == 'Status: active':
            return True
        else:
            return False
    except: return False

def suid_check():
    try: 
        files_found = subprocess.getoutput('sudo find / -perm /4000 2>/dev/null')
        if len(files_found) > 0:
            return files_found
        else:
            return False
    except: return False

def sgid_check():
    try: 
        files_found = subprocess.getoutput('sudo find / -perm /2000')
        if len(files_found) > 0:
            return files_found
        else:
            return False
    except: return False

def rules_check():
    try: 
        rules_found = subprocess.getoutput('sudo iptables -L')
        if len(rules_found) > 0:
            return rules_found
        else:
            return False
    except: return False

def mem_check():
    try:
        messages = []
        if line_in_file('/proc/sys/kernel/randomize_va_space', '1') == True or line_in_file('/proc/sys/kernel/randomize_va_space', '2') == True:
            messages.append('Address space layout randomization is enabled')
    except: return False