# CS166 Software Testing

## Objective

The source code provided in this project will serve as the subject for your test cases.



## General Setup

Requires Python >= 3.5 (download here is you don't have it: https://www.python.org/downloads/)

You are welcome to setup and run this project however you'd like. I use PyCharm frequently on my larger Python projects, so that is my IDE of choice these days. If you haven't used PyCharm before, it's worth a look. You can get the professional version for free with an .edu domain email address, apply here: https://www.jetbrains.com/community/education/#students

To get setup in PyCharm, first download the project files from GitLab, then you can simply create a new project and add the downloaded files to that project, placing the `database.json` file in the same directory as the Python script. You may need to play around with the PyCharm preferences to ensure you're interpreter is setup correctly and you're running the project in Python >= 3.5


If setting up the project via the command line, you (likely) will want to use a virtual environment, in which case...

    python -m venv venv
    
If this doesn't work, you may have Python 2.7 in your path before Python 3+.

    python -V
    
Will let you know what version you are using. The location of your Python 3 
installation will vary, but if you can start Python 3 (from a command prompt
or IDLE, etc.) try this:

    >> import sys
    >> sys.path
    
This will display your Python path. You should be able to figure out the path
to your Python binary. It will likely look something like this

    /some/path/somewhere/bin/python3.7
    
Once you find the path to the correct Python binary you can call this explicitly
to create your virtual environment, e.g.,

    /some/path/somewhere/bin/python3.7 -m venv venv
    
This will create a virtual environment in a directory named 'venv'. To activate
`cd` to the directory just above `venv` (if you aren't already there) and run

    . venv/bin/activate
    
Your prompt should change -- you should see `venv` prepended. This way you know
if you have your virtual environment activated.

If you are using an IDE like PyCharm, go to Preferences and set the project
interpreter to the Python in this virtual environment. If you are running
PyCharm from the same directory as above, PyCharm will automatically detect
the virtual environment and make this an option. Just select, apply, and click
OK. Other IDEs should have similar options.
    
Make sure you have the correct version of Python and (if needed) a new virtual
environment set up.


## Running the application

With the `database.json` file in the same directory as `authentication.py`, run `authentication.py` from your IDE, or from the command line (whichever of the following runs the script in Python 3.5+ in your operating system):

    python authentication.py
or
    
    python3 authentication.py
    
Read through the code and experiment with the various options presented in the menu, such as creating a new user and logging in as an existing user. Once you are comfortable with how the program works, begin writing your test cases as described in the the lab instructions.




