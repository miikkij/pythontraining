# Python – Internal training (mostly TL;DR with links to confirmed decent quality material)
All the material about training is here. Presentations, examples etc. Try to have some kind of structured way if you store something here.

# Install PyCharm IDE from jetbrains 
[PyCharm Editor] Community version should be enough. Use Pro if possible (trial)

# Content
## /Examples/FlaskAPI
This application shows simply how to create API with Flask

## /Examples/HelloWorld
There are two applications showing little difference between Python 2 and 3 when using Print

## /Presentation.ipynb
Run this Jupyter presentation in PyCharm.

## /demos
Demos about using python for testing.

---
---
--- 

## History, Purpose, Capabilities 

What is python? Python is an interpreted, high-level, general-purpose programming language. 

Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales.[26] Van Rossum led the language community until stepping down as leader in July 2018.[27][28] 

### More history 

http://www.trytoprogram.com/python-programming/history-of-python/ 

The programming language Python was conceived in the late 1980s, and its implementation was started in December 1989 by Guido van Rossum at CWI in the Netherlands as a successor to ABC capable of exception handling and interfacing with the Amoeba operating system. 

Python Programming History 
A timeline of Python different versions 
- Python 1.0 
Jan 
1994 
- Python 3.1 
Jun 
2009 
- Python 2.7 
Jul 
2010 
- Python 1.5 
1997 
- Python 3.0 
2008 
- Python 3.2 
Feb 
2011 
- Python 1.6 
Sept 
2000 
- Python 2.6 
2008 
- Python 3.3 
Sept 
2012 
- Python 2.0 
2000 
- Python 2.5 
Sept 
2006 
- Python 3.4 
Mar 
2014 
- Python 2.1 
Apr 
2001 
- Python 2.4 
Nov 
2004 
- Python 3.5 
Sept 
2015 
- Python 2.2 
2001 
- Python 2.3 
Jul 
2003 
- Python 3.6 
2016 

## Where python is used most and with what? 
https://www.quora.com/What-is-Python-mainly-used-for-in-the-real-world-today-Is-it-beneficial-to-use-Python-for-desktop-apps  
3rd most popular programming language according to TIOBE index https://www.tiobe.com/tiobe-index/ 
TIOBE programming community index is a measure of popularity of programming languages 

## Creations  
https://realpython.com/world-class-companies-using-python/ 
https://hackernoon.com/50-popular-python-open-source-projects-on-github-in-2018-c750f9bf56a0 

## Pros and cons  
https://www.infoworld.com/article/2887974/application-development/a-developer-s-guide-to-the-pro-s-and-con-s-of-python.html  

## Different python interpreters 
https://docs.python-guide.org/starting/which-python/  
- CPython
- PyPy 
- Jython
- IronPython
- PythonNet
- And custom ones for e.g. Eve online https://www.eveonline.com/article/carbonio-and-bluenet-next-level-network-technology-1

Quote from eve online article: Most folks familiar with EVE know that it's built on Python, Stackless Python to be specific. Stackless is a micro-threading framework built on top of Python allowing for millions of threads to be live, without a lot of additional cost from just being Python. It is still Python and that means dealing with the Global Interpreter Lock (hereafter known as the damn stinkin' GIL, or just GIL for short). 

## Key differences between python 2 and 3 

https://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html 


## Common IDE / Editors 

- Visual studio Code
- vi/vim
- PyCharm (https://www.shortcutfoo.com/app/dojos/pycharm-win , https://github.com/mstuttgart/flask-pycharm-templates, https://github.com/JetBrains/awesome-pycharm)
 
## Documentation generators 
- Epydoc is a tool for generating API documentation for Python modules, based on their docstrings.  http://epydoc.sourceforge.net/
- There are other document generators for e.g. swagger API document generator that seemed to be very easy to use (but haven't tried it yet) 

## Docker and python
Docker - Python: https://djangostars.com/blog/what-is-docker-and-how-to-use-it-with-python/  


## Web mining / scraping: 

Pattern : https://www.clips.uantwerpen.be/pattern 


## Python GUI: tkinter vs PyQt vs PySide vs WxPython vs Kivy 

https://www.reddit.com/r/learnpython/comments/8ghejx/tkinter_vs_pyqt_vs_pyside_vs_wxpython_vs_kivy_for/ 

 

## virtualenv / venv / Pyenv 

Virtual environments makes multiple python versions possible in same environment 

https://stackoverflow.com/questions/6590688/is-it-bad-to-have-my-virtualenv-directory-inside-my-git-repository 

Might have pros and cons, sometimes packages must be cleaned manually to "reset" the work space, it is recommended just to rebuild virtual env and remove broken one. 


## Message queues 

Kafka, RabbitMQ (Kafka is used mostly by Data Scientist in Python as it gives possibility for streaming the data)

 
## Data scientist tools and stuff

- https://www.tensorflow.org/ 
- https://www.analyticsvidhya.com/blog/2017/03/read-commonly-used-formats-using-python/ 
- https://docs.python.org/3/library/fileformats.html 
- https://wiki.python.org/moin/FlowBasedProgramming 
- https://marcobonzanini.com/2015/10/24/building-data-pipelines-with-python-and-luigi/ 
- panda 
- Jupyter is important tool as it gives DS personnel way to communicate easily even if the system where they get data is different 


## Application structure 

- https://docs.python-guide.org/writing/structure/ 
- https://realpython.com/python-application-layouts/ 
- https://coderwall.com/p/lt2kew/python-creating-your-project-structure 


## Moving from C# or Javascript to python 

- C# https://www.quora.com/Im-moving-from-C-to-Python-what-are-the-major-differences 
- JS http://hg.toolness.com/python-for-js-programmers/raw-file/tip/PythonForJsProgrammers.html  


## Cheat sheets 

- https://www.pythonsheets.com/ 


## Short training session 

- https://www.learnpython.org/ Use this for training, let them practise for 10min and explore -> Continue to do the same practise within your own environment. (host: virtualenv, host: pyenv, docker container, vagrant, virtualbox) 


## Flask Example taken from https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask site 

- How to add API documentation to Flask API https://flask-apispec.readthedocs.io/en/latest/usage.html 


--- Just one more thing before we start: https://en.wikipedia.org/wiki/Zen_of_Python  

 

# Let's practice! 

 
## Download this git repo 

Protip: Linux – Fish shell https://fishshell.com/ , Just remember that if bash or sh or zsh scripts doesn't work you can launch those by using bash, zsh or sh as a command. 

 
## Install python
- python 2.x (https://www.python.org/downloads/release/python-2715/) 
- python 3.x (https://www.python.org/downloads/release/python-372/) 
- https://realpython.com/installing-python/ (different platform)

Note: Install python 2 and 3 into different paths. These are configured little bit differently depending on if the host is Linux / Mac or Windows 

## Remote debuging and development
https://developer.rackspace.com/blog/a-tutorial-on-application-development-using-vagrant-with-the-pycharm-ide/ 

## PIP, how to use, how to upgrade, differences, where do the packages go? (virtual env and host / global).  
- https://pip.pypa.io/en/stable/user_guide/  
- Use pip to avoid package version problems with the python
- Generate requirements     $ env1/bin/pip freeze > requirements.txt
- Install required packages $ env2/bin/pip install -r requirements.txt
- Install virtualenv and venv (through PIP) 


## How to create virtualenv  

When you take stuff from github and want to run those under virtualenv 

### before 15.1.0 

virtualenv --no-site-packages --distribute .env &&\ 
    source .env/bin/activate &&\ 
    pip install -r requirements.txt 
 
### after deprecation of some arguments in 15.1.0 

virtualenv .env && source .env/bin/activate && pip install -r requirements.txt 


## Logging
https://docs.python.org/2/library/logging.html 

## Porting python version 2 to version 3
https://docs.python.org/3/howto/pyporting.html 

Python 3. All code should seamless work with Python 2.7 and Python 3.x. Please read Python’s official guidelines on how to write Python 3.x compatible code, including the usage of the “six” package. It is recommended that you install the “python-modernize” package and run it before submitting any pull requests. 

From <http://pymatgen.org/contributing>  

A word on coding for Python 3 compatibility 

With effect from version 3.0, all pymatgen code must be both Python 2.7+ and 3 compatible. Specifically, we have adopted the following practices throughout pymatgen. 

Unicode-always. Unless you are absolutely sure you need byte literals (rare for pymatgen), always use unicode. In particular, the following should be the first line of all pymatgen modules: 
from __future__ import division, print_function, unicode_literals 
 
Future division means that 1/2 returns a float (0.5), which is more intuitive scientifically, instead of 0 (default integer division in Python 2). print_function ensures that print() is used instead of the print statement. And unicode_literals makes it such that all strings are treated as unicode by default. If you need to use bytes, those should be marked up explicitly as b’byte literal’. 

Use of the six package. Where necessary, use the six package to handle interoperability between Python 2 and 3. Examples include the six.moves functions (common ones are zip, filter, map), and six.stringtypes (testing for string types, which should be rarely done). 

Python-modernize. Use python-modernize to check your code for any potential changes that need to be made. 

Unit testing. The entire pymatgen code base is continuously being tested in both Python 2.7 and >=3.3. If your code fails either of the tests, you need to fix it. 

From <http://pymatgen.org/contributing>  

- Convert it to 3 https://docs.python.org/2/library/2to3.html 

## Python __main__ and modules

https://docs.python.org/3/library/__main__.html 

[PyCharm Editor]: https://www.jetbrains.com/pycharm/

