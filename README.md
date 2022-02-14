<h1>API Testing Framework</h1>

![Contributors](https://img.shields.io/github/contributors/LaCost777/api-base-framework?style=for-the-badge&logo=dependabot&logoColor=white)
![Forks](https://img.shields.io/github/forks/LaCost777/api-base-framework?style=for-the-badge&logo=dependabot&logoColor=white)
![Issues](https://img.shields.io/github/issues-raw/LaCost777/api-base-framework?style=for-the-badge&logo=dependabot&logoColor=white)

<h3>About the project</h3>

Place to keep basic features, required for:
 - setting a connection with API Service; 
 - test client-server communications (prepare requests, invastigate responses, do parameterization, do 'smart' asserts, build UI reports).
 <img width="1792" alt="pytets_api_results" src="https://user-images.githubusercontent.com/41265956/153844079-03a51bbd-7c26-4945-ab7b-8833cae5ded9.png">
<img width="1792" alt="Screen Shot 2022-02-14 at 12 16 44 PM" src="https://user-images.githubusercontent.com/41265956/153845212-39be2d7f-1334-4ee0-84af-5444bf09d87b.png">

<h3>Built With</h3>

Basic libraries.
- Python 3.9.10
- Pip 22.0.3
- Pytest 6.2.5 
- Requests 2.27.1 python library (https://docs.python-requests.org/en/master/)
- PyHamcrest 2.0.3


<details>
  <summary>Full list</summary>
  
  - Package                Version
  ---------------------- ---------
  - allure-pytest          2.9.45
  - allure-python-commons  2.9.45
  - aspy.refactor-imports  2.2.1
  - attrs                  21.4.0
  - autoflake              1.4
  - black                  22.1.0
  - cached-property        1.5.2
  - Cerberus               1.3.4
  - certifi                2021.10.8
  - cfgv                   3.3.1
  - charset-normalizer     2.0.10
  - click                  8.0.3
  - colorama               0.4.4
  - distlib                0.3.4
  - docopt                 0.6.2
  - filelock               3.4.2
  - flake8                 4.0.1
  - Flask                  2.0.2
  - identify               2.4.9
  - idna                   3.3
  - iniconfig              1.1.1
  - isort                  5.10.1
  - itsdangerous           2.0.1
  - Jinja2                 3.0.3
  - MarkupSafe             2.0.1
  - mccabe                 0.6.1
  - mypy-extensions        0.4.3
  - mysql                  0.0.3
  - mysqlclient            2.1.0
  - nodeenv                1.6.0
  - orderedmultidict       1.0.1
  - packaging              21.3
  - pathspec               0.9.0
  - pep517                 0.12.0
  - pi                     0.1.2
  - pip                    22.0.3
  - pip-api                0.0.27
  - pip-shims              0.6.0
  - pipreqs                0.4.11
  - platformdirs           2.4.1
  - plette                 0.2.3
  - pluggy                 1.0.0
  - pre-commit             2.17.0
  - protobuf               3.19.3
  - py                     1.11.0
  - pycodestyle            2.8.0
  - pyflakes               2.4.0
  - PyHamcrest             2.0.3
  - pyparsing              3.0.7
  - pytest                 6.2.5
  - python-dateutil        2.8.2
  - pyupgrade              2.31.0
  - PyYAML                 6.0
  - reorder-python-imports 2.7.1
  - requests               2.27.1
  - requirementslib        1.6.1
  - setuptools             60.5.0
  - six                    1.16.0
  - tokenize-rt            4.2.1
  - toml                   0.10.2
  - tomli                  2.0.1
  - tomlkit                0.9.2
  - typing_extensions      4.0.1
  - urllib3                1.26.8
  - virtualenv             20.13.1
  - vistir                 0.5.2
  - Werkzeug               2.0.2
  - wheel                  0.37.1
  - yarg                   0.1.9
</details>



<h3>How to Install the Project and Run Tests</h3>

1. Install Python, Pip & Virtual Environment. [Installing packages using pip and virtual environments.](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#installing-packages-using-pip-and-virtual-environments)
2. Install dependencies via installing **requironments.txt** located in project root dir. 
```
pip install -r requirements.txt

```
3. Run tests with pytest (Ensure, API Service is running and tests are correctly setup to connect to it's hostname via clients/restcl.py).

Without UI allur reporting. But with additional verbosity to console. 
```
pytest tests/test_book_creation.py -v
```

With UI allur reporting. And with additional verbosity to console. 
```
pytest tests/test_book_creation.py -v --alluredir=/tmp/my_allure_results
allure serve /tmp/my_allure_results

   Generating report to temp directory...
   Report successfully generated to /var/folders/b5/z9rrx3rj3c13pmfw3c7xr2s00000gn/T/16722575253899066065/allure-report
   Starting web server...
   2022-02-14 12:55:27.445:INFO::main: Logging initialized @1579ms to org.eclipse.jetty.util.log.StdErrLog
   Server started at <http://192.168.0.102:62687/>. Press <Ctrl+C> to exit
```

<h3>XXXX</h3>
