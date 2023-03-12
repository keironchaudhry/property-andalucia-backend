# **Coverage** 

* The tool use to measure coverage of code was the [coverage.py](https://coverage.readthedocs.io/en/7.2.1/) package.
* To check coverage in the HTML format run in the terminal:
    * `coverage run --source=appname manage.py test` (or simply `coverage run manage.py test`)
    * `coverage html`
    * Run `python3 -m http.server` (in case there is a server already running, enter `python3 -m http.server 8080`, for example).
    * Live server should be running with a list of HTML options.
    * Pick 'htmlcov/' to view a HTML document with the coverage documentation.

![coverage-1](/documents/images/coverage%20top.png)
![coverage-2](/documents/images/coverage%20mid.png)
![coverage-3](/documents/images/coverage%20bottom.png)