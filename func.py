import os
import subprocess

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