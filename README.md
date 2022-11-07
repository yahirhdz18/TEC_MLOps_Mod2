# TODOS
## How to use the package

### 1. Download the tec_mlops_mod2-0.1.0-py3-none-any.whl file

### 2. Put the tec_mlops_mod2-0.1.0-py3-none-any.whl in the working directory

### 3. Open a terminal and intall the package

<code> pip install tec_mlops_mod2-0.1.0-py3-none-any.whl </code>

or if you wish to instal it in a virtual environment, enter the following code for **Windows Powershell**:

<code> python -m venv venv </code>

<code> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser  </code>

<code>  venv\Scripts\activate.ps1 </code>

<code> pip install tec_mlops_mod2-0.1.0-py3-none-any.whl </code>

### 4. Once the package has been installed it is ready to use.

#### 4.1 Create a new list

To create a new todo list (still with the virtual enviroment activated) enter the code
<code> python -m tec_mlops_mod2 create -ln or --listname <"listname"> </code>

#### 4.2 Show the list of todo lists

<code> python -m tec_mlops_mod2 list </code>

#### 4.3 Check the content of a specific todo list

<code> python -m tec_mlops_mod2 show -ln <"listname"> </code>

#### 4.4 Add a task to a specific todo list

<code> python -m tec_mlops_mod2 add -ln or --listname <"listname"> -tn or --taskname <"taskname"> -d or --description <"description"> -o or --owner <"owner"></code>

#### 4.5 Update a task to a specific todo list

<code> python -m tec_mlops_mod2 update -ln or --listname <"listname"> -i or --taskid <"taskid"> -f or --filed <"field"> -c or --change <"new_value"></code>

### 5 Check the app commands

<code> python -m tec_mlops_mod2 --help </code>
