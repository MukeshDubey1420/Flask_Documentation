# **Flask - A Python Web Micro-Framewrok :- Documentation**

Flask is a micro web framework written in Python and based on the Werkzeug toolkit and Jinja2 template engine.

### Installation

Flask depends on some external libraries, like **Werkzeug and Jinja2**. *Werkzeug* is a toolkit for **WSGI (Web Server Gateway Integration)**, the standard Python interface between web applications and a variety of servers for both development and deployment. *Jinja2* renders **templates**. (We will Study about them in brief).

So how do you get all that on your computer quickly? There are many ways you could do that, but the most kick-ass method is **virtualenv**, so let’s have a look at that first.

1. Virtual Environment :- Python, like most other modern programming languages, has its own unique way of downloading, storing, and resolving packages (or modules). These packages are installed on your system. However third party packages installed by using easy_install or pip are typically placed in one of the directories pointed to by site.getsitepackages:
* It’s important to know this because, by default, every project on your system will use these same directories to store and retrieve site packages (3rd party libraries).
* Consider the following scenario where you have two projects - ProjectA and ProjectB, both of which have a dependency on the same library, ProjectC. The problem becomes apparent when we start requiring different versions of ProjectC. Maybe ProjectA needs v1.0.0, while ProjectB requires the newer v2.0.0, for example.
* This is a real problem for Python since it can’t differentiate between versions in the “site-packages” directory. So both v1.0.0 and v2.0.0 would reside in the same directory with the same name:  And since projects are stored according to just their name there is no differentiation between versions. Thus, both projects, ProjectA and ProjectB, would be required to use the same version, which is unacceptable in many cases.
* This is where the concept of virtual environments (and the virtualenv/venv tools) comes into play…

####  What is a virtual environment?
At its core, the main purpose of Python virtual environments is to create an isolated environment for Python projects. This means that each project can have its own dependencies, regardless of what dependencies every other project has.

2. Requirement.txt --
`pip freeze > requirements.txt` apply this without  activating virtual environment and with virtual environment and see the Difference.

`pip install -r requirements.txt` to install the dependencies.

**If you are on Mac OS X or Linux, chances are that the following command will work for you:**

`$ sudo pip install virtualenv`
 It will probably install virtualenv on your system.
Maybe it’s even in your package manager. If you use Ubuntu, try:

`$ sudo apt-get install python-virtualenv`

**If you are on Windows use**

`pip install virtualenv` this will install virtual environment. Now our task is to Activate this environment.

Once you have `virtualenv` installed, just fire up a shell and create your own environment.

```
# Create a new virtualenv named "myproject" using command.
$ virtualenv myproject
New python executable in myproject/bin/python
Installing setuptools, pip, wheel...done.

Now, whenever you want to work on a project, you only have to activate the corresponding environment

# Activate the virtualenv (OS X & Linux)
$ source myproject/bin/activate

# Activate the virtualenv (Windows)
$ myproject\Scripts\activate


And if you want to go back to the real world, use the following command:

$ deactivate

```


Now, let’s move on. Enter the following command to get Flask activated in your virtualenv:

`$ pip install Flask`
A few seconds later and you are good to go.

After you get your dependencies installed and confirm they're doing the trick for you, you'll probably want to keep track of and control what versions of the dependencies you're using. Pip allows us to "freeze" our dependencies, and record which versions we are using in a file that (by convention) is called requirements.txt. Create a requirements file with this command:

pip freeze > requirements.txt
If later on you wish to install this same set of dependencies again, you can install them from this file with the following command:

pip install -r requirements.txt

### System-Wide Installation
This is possible as well, though I do not recommend it. Just run pip with root privileges:

`$ sudo pip install Flask`
(On Windows systems, run it in a command-prompt window with administrator privileges, and leave out sudo.)
