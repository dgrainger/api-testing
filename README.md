# API Testing

## Environment

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python                 # I use brew to install python
python -m venv venv                 # The last venv is name of directory to store virtual Python environment
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
        "-c",
        "pytest.ini"
    ],
    "python.envFile": "${workspaceFolder}/.env",
    "python.terminal.activateEnvironment": true,
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python"
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
pytest -c pytest.ini
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
pytest -c "pytest.ini" -m "httpbin"
```

To run tests for petstore.swagger.io you would use:

```bash
pytest -c "pytest.ini" -m "petstore"
```

Added load_dotenv() to conftest.py. This will automatically load the environment variables from the .env.
So if you are running the command for httpbin tests, make sure the .env is set for httpbin.org and if you are running
tests for petstore.swagger.io, make sure the .env is set for petstore.

### Viewing the test report

After you run the tests, the --html switch will generate a test report in the _reports/_ folder. We can right click on it and use **Live Server** to view the report in your browser.

### Directory Structure

```tree
api-testing
├── .vscode
│   └── settings.json
├── reports
│   └── test-report.html
├── tests
|   ├── __init__.py
│   ├── conftest.py
│   ├── settings.py
│   ├── test_httpbin_org_example.py
│   └── test_petstore_example.py   
├── venv
├── .env
├── .gitignore
├── API Testing Framework.pdf
├── pytest.ini
├── README.md
└── requirements.txt
```

* .vscode/settings.json - VSCode settings for pytest, Test Explorer UI, .env files and terminal virtual environments
* README.md - This file
* reports - Folder for test reports, added to .gitignore so we don't commit test reports to the repository
* requirements.txt - List of Python packages required
* tests - Test files folder, settings.json tells Test Explorer UI this is where tests are located, pytest.ini which files are test files
* venv - Python virtual environment, added to the .gitignore so we don't commit Python binaries to the repository
* .env - Environment variables used by conftest.py to dynamically set the test environment
* .gitignore - Files and folders to ignore when committing to the repository
  * in addition to venv and reports folders, don't commit cached or dynamically generated files to the repository
  * Normally, I'd add .vscode to the .gitignore as files in this directory are often how individuals configure their environment
  * Also and OS generated files, e.g. .DS_Store from macOS

#### Creating directory structure for README.md

```bash
brew install tree
tree --gitignore >> README.md
```
