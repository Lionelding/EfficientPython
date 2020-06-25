# Item 36: Use Subprocess to Manage Child Process
"""
0. Child processes will run independently from their parent process
1. subprocess model is used to run child process
2. Child process run in parallel with the Python interpreter
3. `proc.communicate(timeout=0.1)` as a parameter to avoid the deadlock
"""

## Set-up
import os
from datetime import datetime, time
import subprocess

print("######## Example 1 ########")
# Example 1: Running a child process

proc = subprocess.Popen(['echo', 'Hello World'], stdout=subprocess.PIPE)
out, err = proc.communicate()
print(out.decode('utf-8'))

# Results are polled periodically
proc = subprocess.Popen(['sleep', '0.3'])
while proc.poll() is None:
	print('Working')

print("######## Example 2 ########")
# Example 2: Run multiple child process in parallel

def run_sleep(period):
	proc = subprocess.Popen(['sleep', str(period)])
	return proc

start = datetime.now()
print(start)

procs = []
for _ in range(10):
	proc = run_sleep(0.1)
	procs.append(proc)

for proc in procs:
	proc.communicate()

end = datetime.now()
print(end)
print(f'Finished in {end-start}')

print("######## Example 3 ########")
## Example 3: Pipe data from a python program into a subprocess, 
## this subprocess passes the data to the next subprocess.
## Finally this python program retrives its output

def run_openssl(data):
	env = os.environ.copy()
	env['password'] = b'\xe24U'
	proc = subprocess.Popen(['openssl', 'enc', '-des3', '-pass', 'env:password'], 
							env=env, 
							stdin=subprocess.PIPE, 
							stdout=subprocess.PIPE)
	proc.stdin.write(data)
	proc.stdin.flush()
	return proc

def run_md5(input_stdin):
	proc = subprocess.Popen(['md5'], 
							stdin=input_stdin, 
							stdout=subprocess.PIPE)
	return proc

# procs = []
# for _ in range(3):
# 	data = os.urandom(10)
# 	proc = run_openssl(data)
# 	procs.append(proc)

# for proc in procs:
# 	out, err = proc.communicate()
# 	print(out)

input_procs = []
hash_procs = []
for _ in range(3):
	data = os.urandom(10)
	proc = run_openssl(data)
	input_procs.append(proc)
	hash_proc = run_md5(proc.stdout)
	hash_procs.append(hash_proc)

for proc in input_procs:
	proc.communicate()

for proc in hash_procs:
	out, err = proc.communicate()
	print(out.strip())

print("######## Example 4 ########")
## Example 4: Time-out

proc = run_sleep(10)
try: 
	proc.communicate(timeout=0.1)
except subprocess.TimeoutExpired:
	proc.terminate()
	proc.wait()

print(f'Exit status: {proc.poll()}')
