# API Testing

## Environment

```bash
brew install python                 # I use brew to install python
python -m venv venv                 # The last venv is the name of the directory to store my virtual Python environment, I use venv because it is in my .gitignore
source venv/bin/activate
pip install -r requirements.txt
```

If you add libraries you need to import to any of your code, you want to add that library to the _requirements.txt_ file and run the **pip install** again.

* Install VS Code
* Open VS Code and install the following extensions:
    * Pylance
    * Python
    * Python Debugger
    * Python Environments
    * Test Explorer UI
    * Live Server

### VS Code settings.json

Create a directory in the root of your project called _.vscode/_ and create a file called settings.json with the following content:

```json
{
    "python.testing.pytestEnabled": true,
    "python.testing.unittestEnabled": false,
    "python.testing.cwd": "${workspaceFolder}",
    "python.testing.pytestArgs": [
        "tests",
        "-vv",
        "-s",
        "-rA",
        "--color=yes",
        "--html=reports/test-report.html",
        "--self-contained-html"
    ],
    "python.envFile": "${workspaceFolder}/.env",
    "python.terminal.activateEnvironment": true
}
```

This will set up Test Explorer UI to be the same as running tests from the command line.
Note: some of the tests in this project are for the website httpbin.org and some are for
petstore.swagger.io. If you set the environment variables to point to httpbin.org and try
running a test for petstore.swagger.io, it will fail. 

It is assumed that you will set your environment variables and only run the tests, from Test Explorer UI, that
apply to those variables. From the command line, you can control which tests get run. See below for more details.

### Pylance

In order for Pylance to highlight the python code correctly, you need to tell VS Code which Python interpreter you are using.

* Enter CMD + Shift + P and type _**Python: Select Interpreter**_
* Select the _./venv/bin/python_ version (usually Recommended)

Selecting your virtual Python environment like this will also automatically start it when you open a terminal
because of the ```"python.terminal.activateEnvironment": true``` line in _**settings.json**_

### Test Explorer UI

In order to set up Test Explorer UI you want to click the beaker icon to open it. Then click on the _Configure Python Tests_ button.

* Select _pytest_
* Select the _tests_ folder

Now you can run tests from the Test Explorer UI. You can also run a test from the editor using the icon on the left of the test function. If you hold the option key, the test icon will change to a debug icon.

The settings in _**settings.json**_ will help to configure how Test Explorer UI works as well. If there are command line options you want to use, you can add them to _**settings.json**_ and they will be used by Test Explorer UI as well.

### Running tests from the command line

Create a directory to hold the test results:

```bash
mkdir reports
```

To actually run the tests:

```bash
pytest tests -vv -s -rA --color=yes --html=reports/test-report.html --self-contained-html
```

You can also limit the tests you run via markers. For example, the tests that run against the site httpbin.org have been marked with the _httpbin_ marker. To run only those tests:

```bash
pytest -m "httpbin"
```

You can also use switches like:

```bash
pytest -m "not httpbin"
pytest -m "httpbin or smoke" # runs if marked as httpbin or smoke
pytest -m "httpbin and smoke" # has to be marked for httpbin and smoke
```

So if you are using the environment variables for httpbin.org, you can run using:

```bash
pytest tests -vv -s -rA --color=yes --html=reports/test-report.html --self-contained-html -m "httpbin"
```

To run tests for petstore.swagger.io you would use:

```bash
pytest tests -vv -s -rA --color=yes --html=reports/test-report.html --self-contained-html -m "petstore"
```

Just remember to set the environment variables from _**.env**_, i.e. edit the file then

```bash
set -a; source .env; set +a
```

### Viewing the test report

After you run the tests, the --html switch will generate a test report in the _reports/_ folder. We can right click on it and use **Live Server** to view the report in your browser.
