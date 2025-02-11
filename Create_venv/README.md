
```shell
mkdir my_venv
cd my_venv
python3 -m venv ./venv
source ./venv/bin/activate 
```

In PyCharm: 
------------
1. Settings -->  Project: <project name> --> Python Interpreter. 
2. Click the Add Interpreter  --> add local interpreter
3. Select the project folder (need new name i.e venv_1 ) 
4. Select the Inherit global site-packages checkbox 
Or Select the Make available to all projects checkbox if you want to reuse this environment when creating Python interpreters in PyCharm.

Then in the parent directory below venv_1 run 
source venv_1/bin/activate 