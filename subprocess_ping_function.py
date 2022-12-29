#!/usr/bin/env python3
import subprocess

def check_ip(ip_address):
	result = subprocess.run(['ping', '-c', '4', '-n', ip_address], 
	stdout = subprocess.PIPE,
	stderr = subprocess.PIPE,
	encoding = 'utf-8')
	
	if  result.returncode == 0:
		return True, result.stdout
	else:
		return False, result.stderr

print(check_ip('10.64.86.231'))

print(check_ip('a'))
