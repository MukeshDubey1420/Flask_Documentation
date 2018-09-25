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

## Back-end Web Framework: Flask (Part-1: Beginning )

### Why is Flask a good web framework choice?
Flask is considered more Pythonic than the `Django web framework` because in common situations the equivalent Flask web application is more explicit. Flask is also easy to get started with **as a beginner because there is little boilerplate code for getting a simple app up and running.**

### Create a simple Flask application
We can test that our development environment is configured correctly by creating a simple Flask application. We’ll grab the nine-line example from Flask’s homepage and drop it in a new file called `app.py`.

### Make Sure don't save this File as `flask.py`. bcz it is predefined-module file . just like we can't use an keyword as an identifier.

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()

```

* We import the **flask** dependency. **Remember to use a capital Flask** while importing.

* We create the `app` object as an instance of class Flask imported from the flask package. The `__name__` variable passed to the Flask class is a Python predefined variable, **which is set to the name of the module in which it is used. It is helpful when we want to find other static files such as HTML, CSS files.**

* **__name__ == "__main__"** is required for a quick check so as **to make sure that we only start the web server or web app when this piece of code is called directly.**

* app.run() is used to run the code.

The above code shows "Hello, World!" as Response on `localhost port 5000`   `http://localhost:5000`in a web browser when run with the `python app.py` command.



## Back-end Web Framework: Flask (Part-2: Routing & URL Binding)

Web frameworks nowadays use the routing technique to help users to navigate through a web without having to remember application URLs. It is useful to access the desired page directly without having to navigate from the home page.

```python
from flask import Flask
app = Flask(__name__)
@app.route('/')
    def index():
    return 'This is homepage'
@app.route('/about')
     def about():
     return '<h2> About page </h2>'

if __name__ == "__main__":
    app.run(debug = True)

```

#### **Route() decorator** can be used to inject additional functionality to one or more functions.

* `app.route(rule, option)` Rule represents the URL binding with the function and option is a list of parameters to be forwarded to the underlying Rule options.

* `@app.route(‘/’)` This is the URL and whenever a client requests it the server will send back the return value i.e. return `‘This is homepage’ `. Now, suppose we want to go to the about page, then we write this `@app.route(‘/about’) `. This returns `return ‘<h2> About page </h2>’ `. We can also put HTML codes in the return statement. `def index():` and `def about():` are functions (basically Views).

* `app.run(host, port, debug, option)` But we just use the `debug` in this example. host defaults to `127.0.0.1 (localhost)` and Sets at port number 8000 by default.


* debug defaults to `false`. If set to `true`, provides a `debug information`

* options forwards to underlying Werkzeug server.

* `app.run(debug = True)` when the app is `under development,` it should be restarted manually for each change in the code. **To avoid this inconvenience, we enable the debug mode**. *The server then will reload itself with any changes in code. It’s also useful when there is a bug in the code and helps find errors.*


* There is `url_for` function which is very useful if we want a dynamically build URL.

```python
from flask import Flask
 app = Flask(__name__)
@app.route('/teacher')
     def hello_teacher():
     return 'Hey Teacher'
@app.route('/students/<student>')
     def hello_students(student):
     return 'Hello %s as student' %student
@app.route('/user/<name>')
     def hello_user(name):
         if name == 'teacher':
              return redirect(url_for('hello_teacher'))
         else:
              return redirect(url_for('hello_students'))
if __name__ == "__main__":
     app.run(debug = True)

```

#### This is a dynamic URL example

* `@app.route('/user/<name>)` This here suggests the variable part <name> , it takes in any variable name and displays it later. **If ‘teacher’ is supplied to def hello_user(name): function as argument. The hello_user() function checks if an argument received matches ‘teacher’ or not. If it matches, the application is redirected to the hello_teacher() function using url_for(), otherwise to the hello_students() function passing the received argument as guest parameter to it.**


## Back-end Web Framework: Flask (Part-3: How to make a simple Login Page using Get and Post)

* `HTTP protocol` is the core basis of data communication in **(WWW) world wide web**. It is *designed to communicate between clients and servers*. It works as a request-respond protocol. HTTP has different methods of data retrieval from specified URL and those methods have been defined in this protocol.

* **GET**: Browser requests server to get data in an unencrypted form stored on that page and send it. **It’s the default method**. *It can be cached and remains in browser history*.

* **POST**: It is **used to send HTML form data to be processed to a specified resource**. *Browser tells the server that it wants to posts some new data to the URL and it is only stored once. Data received by POST method is not cached by server*.

* **PUT**: It replaces all current representations of the target resource with the uploaded content. Similar to Post, it might trigger the store procedure multiple times by overwriting the old data. It is helpful when suppose your connection is lost during transmission. In this situation a system between the browser and the server might receive the request safely a second time without breaking things.

* **DELETE**: It removes all current representations of the target resource given by a URL.


* *By default, a route answers to GET requests only*, but that can be changed by providing the methods argument to the route() decorator. Here I am just going to use here two common HTTP methods: **GET and POST**

**For GET request `request.args.get('username')` is used .**

**For POST request `request.form[‘username’]` is used.**

`'username'`  is the name (Value) of the input defined by us in HTML Form Code.
To collect form data we require module: `request`

```python
from flask import Flask, redirect, url_for, request
app = Flask(__name__)
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['username']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('username')
      return redirect(url_for('success',name = user))
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name
if __name__ == '__main__':
   app.run(debug = True)

```

#### The HTML code inside the `templates` folder is ->

``` HTML
<html>
<body>
<form action = "http://localhost:5000/login" method="post">
 <p> Enter Name:</p>
 <p> <input type="text" name="username"></p>
 <p> <input type="submit" name="submit"></p>
</form>
</body>
</html>

```

* The http://localhost:5000/login is mapped to `login()` function (or we can say View). As the server has received the submitted data by POST method, value of ‘username’ parameter obtained from the form data is by: user = request.form[‘username’] . It is then passed to the /success URL as the variable part /<name> . The browser will display it on the screen.


## Back-end Web Framework: (Flask Part 4: Jinja2 Explanation in Detail)

#### What is Jinja 2?

* Jinja2 is **a modern day templating language for Python developers**. It was made after Django’s template. It is used to create HTML, XML or other markup formats that are returned to the user via an HTTP request. You can read more [here...](https://en.wikipedia.org/wiki/Jinja_%28template_engine%29)

#### Installation : How To Get Jinja 2

```
pip install jinja2
easy_install jinja2
```

### Why do we need Jinja 2?

* **Sandboxed Execution**: It provides a protected framework for automation of testing programs, whose behaviour is unknown and must be investigated.

* **HTML Escaping**: Jinja 2 has a powerful automatic HTML Escaping, which helps preventing Cross-site Scripting (XSS Attack). **There are special characters like >,<,&, etc. which carry special meanings in the templates**. So, if you want to use them as regular text in your documents then, replace them with entities. Not doing so might lead to XSS-Attack.

* **Template Inheritance**: This is the most important feature, We will study in detail later on.

#### What are Templates?
Back in the days, servers used to have a collection of files, like HTML files, which were sent over as requested by clients. These were static data being sent over.

Now, in the modern web world, we have less of static data and more of dynamic data being requested from clients and therefore sent by the server. The web totally depends on what the client is asking for, and on which user is signing in and who is logging out. So, Jinja2 templating is being used.

**A template contains variables which are replaced by the values which are passed in when the template is rendered. Variables are helpful with the dynamic data.**

##### Structure of Flask App
```
/flaskproject
   -/app.py
    /templates
       -/index.html

```
The structure of your application helps to keep your code organised and accessible. **Flask expects the templates directory to be in the same folder as the module in which it was created**. *You can specify the location of the `template_folder`. **Remember to keep your templates file in the templates folder**.*

```python
app = Flask(__name__, template_folder='../pages/templates')
```

#### Delimiters(Syntaxes)
```
{%....%} are for statements(if,else and for loops)
{{....}} are expressions used to print to template output
         (to pass python defined variable in html template)
{#....#} are for comments which are not included in the template output
#....## are used as line statements

````
##### Write this file in flaskproject/templates/index.html:

```html
<!DOCTYPE html>
<html>
<p>Hello {{ username }}</p>
</body>
</html>

```

This is a very simple HTML file. **Variables are like the placeholders which store dynamic data or values**. These values may be passed or provided as arguments in `render_template() ` call. **Rendering** is a process of filling these placeholders with actual data. As HTML file is rendered, data is sent to a client.

#### Write this file in flaskproject/app.py:

```python
from flask import Flask, render_template
app = Flask(__name__, template_folder=’’) # by default set to root directory. if we want to change then we use template_folder() function and pass new location.
@app.route(‘/user/<username>’)
def index(username):
    return render_template(‘index.html’, username=username)
if __name__ == ‘__main__’:
 app.run(debug=True)

```

So, now we render HTML by using `render_template()` . The syntax is:
```python
flask.render_template(template_name_or_list,**content)
```

This renders a template from the templates folder with the given content.

* template_name_or_list is the name of the template to be rendered or iterated.
* ** means it is looking for keyword arguments.

Values can also be passed to the templates via the content dictionary. To print the value of variable, we use a {{ username }} .To access the variable’s attributes, we can either use {{ username.surname}} or {{ username['title'] }}.


#### Conditional Statement
So long we’ve seen only seen one of the many advantages of Jinja 2. **To control the flow of the program, we create a structure which is controlled by conditional statements. {%....%} these are the placeholders from which all the conditions are executed.**

This is the flaskproject/app.py file

```python
from flask import Flask, render_template

app = Flask(__name__)
@app.route(‘/’)
def index():
 list_example = [‘Mukesh’, ‘MukeshDubey’, ‘Mukul’]
 return render_template(‘index.html’, list_example=list_example)

if __name__ == ‘__main__’:
 app.run(debug=True)

 ```

##### Next is the HTML file stored in flaskproject/templates/index.html:

```html
<!DOCTYPE html>
<html>
<head>
 <title>Conditions Demonstration</title>
</head>
<body>
<ul>
 {% for name in list_example %}
 <li>{{ name }}</li>
 {% endfor %}
 </ul>

 <ol>
 {% for name in list_example %}
 <li>{{ name }}</li>
 {% endfor %}
 </ol>

</body>
</html>

```
So, we use for loop to iterate over the `list_example` and print it with this placeholder `{{ name }}`. To end for loop use `{%endfor%}` and to end if loop, use `{%endif%}`.
