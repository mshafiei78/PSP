Step 1: Install Python
Download Python from https://www.python.org/downloads/
Run the installer.
✅ Tick "Add Python to PATH"
Click Install Now
Step 2: Install VS Code
Download VS Code from https://code.visualstudio.com/
Install using the default settings.
Step 3: Install the Python Extension
Open VS Code.
Click Extensions (left sidebar).
Search for Python.
Install the extension published by Microsoft.
Step 4: Create Your First Program
Create a folder called PSP.
Open the folder in VS Code.
Create a file named:
Python
1
hello.py
Show more lines
Add:
Python
1
print("Hello PSP!")
Show more lines
Save the file.
Step 5: Run the Program

Click the Run ▶ button in the top-right corner.

OR

Open Terminal:

Shell
1
python hello.py
Show more lines

Expected output:

Plain Text
1
Hello PSP!
Show more lines
Common Problems
Python not found

Run:

Shell
1
python --version
Show more lines

If this does not work, reinstall Python and ensure:

✅ Add Python to PATH

Wrong Interpreter

Press:

Plain Text
1
Ctrl + Shift + P
Show more lines

Type:

Plain Text
1
Python: Select Interpreter
Show more lines

Choose the installed Python version.