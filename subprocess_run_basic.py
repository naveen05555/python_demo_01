import subprocess

reply = subprocess.run(['ping', '-c', '4', '-n', '10.64.86.1'])
if  reply.returncode == 0:
	print("Alive")
else:
	print("Unreachable")
