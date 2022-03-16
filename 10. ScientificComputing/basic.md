# SCIENTIFIC COMPUTING with Python
- Python is a high-level, general-purpose interpreted programming language that is widely used in scientific computing and engineering.
- This ecosystem includes development tools and interactive programming environments, such as Spyder and IPython, which are designed particularly with scientific computing in mind. 
- It also includes a vast collection of Python packages for scientific computing. This ecosystem of scientifically oriented libraries ranges from generic core libraries – such as NumPy, SciPy, and Matplotlib – to more specific libraries for particular problem domains.
- Python and its scientific computing libraries are free and open source. This eliminates economic constraints on when and how applications developed with the environment can be deployed and distributed by its users.

## Environments for Computing with Python
1. The Python interpreter or the IPython console to run code interactively. Together with a text editor for writing code, this provides a lightweight development environment.
2. The Jupyter Notebook, which is a web application in which Python code can be written and executed through a web browser. This environment is great for numerical computing, analysis, and problem-solving, because it allows one to collect the code, the output produced by the code, related technical documentation, and the analysis and interpretation, all in one document.
3. The Spyder Integrated Development Environment, which can be used to write and interactively run Python code. An IDE such as Spyder is a great tool for developing libraries and reusable Python modules.

### IPython console
- IPython 3 is an enhanced command-line REPL environment for Python, with additional features for interactive and exploratory computing. For example,
	1. IPython provides improved command history browsing (also between sessions), 
	2. an input and output caching system, 
	3. improved autocompletion, 
	4. more verbose and helpful exception tracebacks

- *Installing IPython*
$ pip install ipython
- *upgrade an already installed package*
$ pip install --upgrade ipython
- *Running the ipython command launches the IPython command prompt:*
$ ipython

#### Input and Output Caching
- The input prompt is denoted as In [1]: and the corresponding output is denoted as Out [1]:, where the numbers within the square brackets are incremented for each new input and output. These inputs and outputs are called cells in IPython. 
- Both the input and the output of previous cells can later be accessed through the In and Out variables that are automatically created by IPython. The In and Out variables are a list and a dictionary, respectively, that can be indexed with a cell number.
- For instance, consider the following IPython session:
	*'
	In [1]: 3 * 3
	Out[1]: 9
	In [2]: In[1]
	Out[2]: '3 * 3'
	In [3]: Out[1]
	Out[3]: 9
	In [4]: In
	Out[4]: [", '3 * 3', 'In[1]', 'Out[1]', 'In']
	In [5]: Out
	Out[5]: {1: 9, 2: '3 * 3', 3: 9, 4: [", '3 * 3', 'In[1]', 'Out[1]', 'In', 'Out']}
	'*
- A single underscore _ is a shorthand notation for referring to the most recent output, and a double underscore __ refers to the output that preceded the most recent output.

- Note that when a cell is executed, the value of the last statement in an input cell is by default displayed in the corresponding output cell, unless the statement is an assignment or if the value is Python null value None. 
- The output can be suppressed by ending the statement with a semicolon:
	*'
	In [6]: 1 + 2
	Out[6]: 3
	In [7]: 1 + 2;    # output suppressed by the semicolon
	In [8]: x = 1     # no output for assignments
	In [9]: x = 2; x  # these are two statements. The value of 'x' is shown in the output
	Out[9]: 2
	'*
#### Autocompletion and Object Introspection
- pressing the TAB key activates autocompletion, which displays a list of symbols (variables, functions, classes, etc.) with names that are valid completions of what has already been typed. The autocompletion in IPython is contextual.
	*'
	In [10]: import os
	In [11]: os.w<TAB>
	os.wait  os.wait3  os.wait4  os.waitpid  os.walk  os.write  os.writev
	'*

#### Documentation
- A Python object followed by a question mark displays the documentation string for the object. This is similar to the Python function help. 
- An object can also be followed by two question marks, in which case IPython tries to display more detailed documentation, including the Python source code if available. For example, to display help for the cos function in the math library:
	*'
	In [12]: import math
	In [13]: math.cos?
	Type:        builtin_function_or_method
	String form: <built-in function cos>
	Docstring:
	cos(x)
	Return the cosine of x (measured in radians).
	'*

#### Interaction with the System Shell
- Anything that follows an exclamation mark is evaluated using the system shell (such as bash shell).
	*'
	In[14]: !ls
	file1.py    file2.py    file3.py
	'*
- The output generated by a command following an exclamation mark can easily be captured in a Python variable. For example, a file listing produced by !ls can be stored in a Python list using
	*'
	In[15]: files = !ls
	In[16]: len(files)
	3
	In[17] : files
	['file1.py', 'file2.py', 'file3.py']
	'*
- Likewise, we can pass the values of Python variables to shell commands by prefixing the variable name with a $ sign:
	*'
	In[18]: file = "file1.py"
	In[19]: !ls -l $file
	-rw-r--r--  1 rob  staff 131 Oct 22 16:38 file1.py
	'*

#### Running Scripts from the IPython Console
- an external Python source code file can be executed within an interactive IPython session with the command %run 
In [21]: %run fib.py
Out[22]: ...



### Jupyter
- The Jupyter project 7 is a spin-off from the IPython project that includes the Python independent frontends – most notably the notebook application.
	1. The Jupyter QtConsole
	2. The Jupyter Notebook

#### The Jupyter QtConsole
- The Jupyter QtConsole is an enhanced console application that can serve as a substitute to the standard IPython console. The QtConsole is launched by passing the qtconsole argument to the jupyter command:
	*'
  	$ jupyter qtconsole
  	'*
- This opens up a new IPython application in a console that is capable of displaying rich media objects such as images, figures, and mathematical equations.

#### The Jupyter Notebook
- Jupyter also provides the web-based notebook application
- The notebook environment allows to write and to run code, to display the output produced by the code, and to document and interpret the code and the results: all in one document. This means that the entire analysis workflow is captured in one file, which can be saved, restored, and reused later on.
- The Jupyter Notebook features a rich display system that can show media such as equations, figures, and videos as embedded objects in the notebook. It is also possible to create user interface (UI) elements with HTML and JavaScript, using Jupyter’s widget system.
- To launch the Jupyter Notebook environment, the notebook argument is passed to the jupyter command-line application.
	*'
  	$ jupyter notebook
  	'*  	
- This launches a notebook kernel and a web application that, by default, will serve up a web server on port 8888 on localhost, which is accessed using the local address in a web browser.
	*'
	http://localhost:8888/ 
	'*
#### Jupyter Lab
Jupyter Lab is a new alternative development environment from the Jupyter project. It combines the Jupyter Notebook interface with a file browser, text editor, shell, and IPython consoles, in a web-based IDE-like environment.


### Spyder: An Integrated Development Environment
- An integrated development environment is an enhanced text editor that also provides features such as integrated code execution, documentation, and debugging.
- the Spyder IDE was specifically created for Python programming and in particular for scientific computing with Python.
	1. Source code editor
	2. Consoles for the Python and the IPython interpreters and the system shell
	3. Object inspector, for showing documentation for Python objects
	4. Variable explorer
	5. File explorer
	6. Command history
	7. Profiler

