from flask import Flask, request, render_template
from subprocess import *
import os
from pwn import *

app = Flask(__name__)

@app.route('/')
def functest():
	# general user information
	whoami = os.popen("whoami").read()
	log.info("User information")
	id = os.popen("id").read()
	log.info("User ID Information")
	host = os.popen("hostname").read()
	log.info("Machine Hostname Information")
	arch = os.popen("uname -m").read()
	log.info("Machine Architecture information")
	arch = arch.strip()
	
	# ip tables
	ipt = os.popen("cat /home/dnoscp/Desktop/LinuxSecurityFramework/web/iptables.txt").read()
	ipt = ipt.split('\n')
	iprule = ipt

	processes = os.popen("ps aux | wc -l").read()

	return render_template('debug.html', user = whoami,id = id, host=host, arch=arch, iprule=iprule, process=processes)

@app.route('/gotty')
def liveStream():
	return render_template('gotty.html')

@app.route('/results')
def resScan():
	# ./LinuxSecurityFramework.sh -N | tee NOCOLORS.log
	data = open("/home/dnoscp/Desktop/LinuxSecurityFramework/sh_files/NOCOLORS.log", 'r').read()
	data = data.split('\n')

	return render_template('results.html', data = data)	

if __name__ == "__main__":
	app.run(debug = True)


"""
# MAIN HTML FILES
1. debug.html
2. results.html
3. gotty.html
"""