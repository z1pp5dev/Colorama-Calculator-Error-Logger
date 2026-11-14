#Logger Utility Week 9 Project

#Imports
import datetime
from colorama import Fore, Style, init
init(autoreset=True)

#File Paths and Variables
log_filename = "error.log"
#Get user input for basic calucator functions
operation = int(input(Fore.CYAN + "Please select calculation type: 1. Add, 2. Subtract, 3. Divide, 4. Multiply "))
first_num = float(input(Fore.CYAN + "Please enter your first number: "))
second_num = float(input(Fore.CYAN + "Please enter your second number: "))
#Defining Function and Safe File I/O

def log_error(error_message):
    """Writes timestamed error messafes to a local log file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_filename, 'a') as log_file:
        log_file.write(f"[{timestamp}] ERROR: {error_message}\n")

#Core Logic Loop with error handling
try:
    if operation == 1:
        print(f"Your Total is: {first_num + second_num}")
    elif operation == 2:
        print(f"Your Total is: {first_num - second_num}")
    elif operation == 3:
        print(f"Your Total is: {first_num / second_num}")
    elif operation == 4:
        print(f"Your Total is: {first_num * second_num}")
    else:
        print(Fore.RED + "Error! Please enter a valid option: 1, 2, 3, or 4")
except ZeroDivisionError as e:

#Print out error if one if caught
    print(Fore.RED + Style.BRIGHT + "Caught a runtime error! Logging to disk...")

#Call log_error function from above to write data to error log
    log_error(str(e))
    print(Fore.YELLOW + f"Error successfully written to {log_filename}")
