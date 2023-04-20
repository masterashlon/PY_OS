#PY-OS in PY-Command 0.1.1A
# toroman needs control for number and empty string
import sys
import subprocess

from version import python_version_info, command_version_info
from datetime_1 import today, time_now
from paiy import dialog_with_paiy
from toroman import convert_to_number



commands = [	# list to show every commands that can be used and their description
			"  info\t\t\tInformation about py-command and PY-OS",
			"  vers\t\t\tInformation about core inside PY-OS",
			"  clock\t\t\tTime in hours:minutes:seconds format right now",
			"  date\t\t\tDate about time in day/month/year format",
			"  exit\t\t\tClose the program",
			"  help\t\t\tactually commands list",
			"  hello|hi|ehi|sup\tTo use PaiY , very powerful and useful assistant AI",
			"  toroman\t\tconverts sentence to roman number, every letter(not numbers for now)",
			"  dvd\t\ttry yourself",			
			#"  start|new\t\tNew python on cmd/terminal appears"
			]

def control_command(input_command): #function to control every command and reindirize for every specifically function
	if input_command == "vers":	
		python_version_info()
	
	elif input_command == "date":
		today()
	
	elif input_command == "info":
		command_version_info()
			
	elif input_command == "clock":
		time_now()
		
	elif input_command == "help":
		commands.sort()
		for com in commands:
			print(com)
			
	elif input_command == "hello" or input_command == "hi" or input_command == "ehy" or input_command == "yup":
		dialog_with_paiy()

	elif input_command == "toroman":
		convert_to_number()

	elif input_command == "dvd":
		subprocess.run("python dvd_logo.py")
  
	#elif input_command == "start" or "new":
	#	os.system("start /wait cmd /c python")
		
	else:
		print(f"\t\"{input_command}\" doesn't exist in commands list.\nUse \"help\" for show commands list" )
		
	print()	#one line space


def main():	 #principle function of this program, its like a os terminal
	print("\t\tPY-Command(alpha-version) for PY-OS (use \"help\" for commands list) ")

	bool_condition = True

	while (bool_condition):
		user_command = input("P: PY-OS >> sys --> ").strip().lower()
		if user_command != "":
			if user_command == "exit":
				print("\t\nPY-Command closed successfully...")
				bool_condition = False
				break
			print()
			control_command(user_command)
		else:
			continue

main()

