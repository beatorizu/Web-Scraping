## Web Scraping

### Technologies

* [Beautiful Soup] 4.7.1
* [Pandas] 0.24.2
* [PyMongo] 3.8.0
* [Requests] 2.22.0
* [virtualenvwrapper]

### Build environment

1. Run `mkvirtualenv --python=python3.6 web-scraping` command to create a python virtual environment named **web-scraping** and using 3.6 version of python
2. To work on **web-scraping** environment run `workon web-scraping` command
3. Once virtual environment is activated run `pip install -r requirements.txt` to install project dependencies
4. To fetch and upload data run `python service.py --user username --password password`

[Beautiful Soup]: <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>
[Pandas]: <https://pandas.pydata.org/>
[PyMongo]:<https://api.mongodb.com/python/current/>
[Requests]:<https://2.python-requests.org/en/master/>
[virtualenvwrapper]: <https://virtualenvwrapper.readthedocs.io/en/latest/>
