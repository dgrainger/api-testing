# API Testing

## Environment

```bash
brew install python
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

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
}
```

This will set up Test Explorer UI to be the same as running tests from the command line.

### Pylance

In order for Pylance to highlight the python code correctly, you need to tell VS Code which Python interpreter you are using.

* Enter CMD + Shift + P and type _**Python: Select Interpreter**_
* Select the _./venv/bin/python_ version (usually Recommended)

### Test Explorer UI

In order to set up Test Explorer UI you want to click the beaker icon to open it. Then click on the _Configure Python Tests_ button.

* Select _pytest_
* Select the _tests_ folder

Now you can run tests from the Test Explorer UI. You can also run a test from the editor using the icon on the left of the test function. If you hold the option key, the test icon will change to a debug icon.

### Running tests from the command line

Create a directory to hold the test results:

```bash
mkdir reports
```

To actually run the tests:

```bash
pytest tests -vv -s -rA --color=true --html=reports/test-report.html --self-contained-html
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
