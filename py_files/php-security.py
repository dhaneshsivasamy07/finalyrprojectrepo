#!/usr/bin/env python3

import os, re
from pwn import *

score =  0
f_score = 0


def calc(function):
	if function in funcs:
		# log.success(f"Immune to {function} function call")
		global f_score
		f_score += 1

def conf_check(setting):
	if setting in php_ini:
		log.warning(f"{setting} is enabled use with caution / disable the function")
		global score
		score -= 1
	else:
		score += 1

def check_me():
    log.info("Checking PHP Security")
    try:
        dn = os.popen("grep -i disable_functions /etc/php/*/apache2/php.ini | cut -d '=' -f 2 | sed 's/\s//'g").read()
        funcs = dn.replace(',', '\n')

        functions = ['system', 'exec', 'shell_exec', 'passthru', 'phpinfo', 'show_source', 'highlight_file', 'popen', 'proc_open', 'fopen_with_path', 'dbmopen', 'dbase_open', 'putenv', 'move_uploaded_file', 'chdir', 'mkdir', 'rmdir', 'chmod', 'rename', 'filepro', 'filepro_rowcount', 'filepro_retrieve', 'posix_mkfifo']
        for dn in functions:
    	    calc(dn)
    except:
        print("SOMETHINGS WRONG")

log.info("Reading php configuration")
try:
	php_file = os.popen("ls /etc/php/*/apache2/php.ini").read().strip()
	php_ini = open(f'{php_file}', 'r').read()
except FileNotFoundError as e:
    print("PHP doesnt seems to be installed")
    sys.exit(0)

conf_check("allow_url_fopen = On")
conf_check("log_errors = Off")
conf_check("display_startup_errors  = On")
conf_check("display_errors = On")
conf_check("track_errors = On")
conf_check("html_errors = On")

if f_score in range(20,24):
	score += 1
log.success(f"Patched Funtions: {f_score - 1}/23")

print(f"Total Score: {score}")
