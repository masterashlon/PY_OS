#show python version used to run this program and other info stuff
import sys

def python_version_info():
	print(f"\tPY-OS core/engine version(python): { sys.version_info[0]}.{ sys.version_info[1]}.{ sys.version_info[2]}")

def command_version_info():
	print("\tPY-Command : 0.2.0a")	