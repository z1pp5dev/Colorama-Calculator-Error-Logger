
# Colorama Calculator & Error Logger

A robust, command-line calculator built in Python that supports basic arithmetic operations, utilizes [Colorama](https://github.com/tartley/colorama) for vibrant terminal styling, and features automated timestamped error logging for runtime exceptions (such as division by zero).
## Features

* **Interactive CLI Menu:** Select from Addition, Subtraction, Multiplication, and Division with clean text prompts.
* **Vibrant Terminal Output:** Powered by Colorama to deliver color-coded success messages, prompts, and critical error warnings.
* **Defensive Input Validation:** Typecasts and handles user inputs safely using try/except blocks to prevent unexpected crashes.
* **Automated File Persistence:** Automatically logs timestamped runtime exceptions to a local `error.log` file on disk.
## Prerequisites & Installation

1. **Python 3.x** installed on your local machine.
2. Clone the repository and navigate into the project directory:
   ```bash
   git clone https://github.com/z1pp5dev/colorama-calculator.git
   cd colorama-calculator
    
## Create and activate a virtual environment:

Bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
## Install required dependencies:

Bash
pip install -r requirements.txt
## Usage Run the calculator script from your terminal:

"python calculator.py"

Follow the on-screen prompts:

Select your calculation type (1 for Addition, 2 for Subtraction, 3 for Division, 4 for Multiplication).

Enter your first numerical value.

Enter your second numerical value.

View your total output instantly in the terminal!
## Error Handling & Logging

If a runtime error occurs—such as attempting to divide any number by zero (ZeroDivisionError)—the application will:

1. Catch the exception safely.

2. Display a bold, color-coded warning message in the terminal using Colorama.

3. Automatically append a timestamped error entry to your local error.log file:

Plaintext
[2026-11-14 12:00:00] ERROR: division by zero
## 🚀 About Me
I'm am a independent backend devleoper, looking to create and share helpful and meaningfull projects and programs for all to use!
## Support

For support, email z1pp5.dev02@gmail.com


