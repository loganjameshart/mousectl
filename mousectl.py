#!/usr/bin/env python3
'''
Runs ratbagctl on startup. Identifies name given to mouse, and sets LED to 0.
'''
import subprocess

proc = subprocess.run(['ratbagctl'], stdout=subprocess.PIPE, shell=True)

mouse_name = proc.stdout.decode().split(":")[0]

subprocess.run(['ratbagctl', mouse_name, 'led', '0', 'set', 'mode', 'on'], shell=True)
