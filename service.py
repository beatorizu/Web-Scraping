import argparse
from sys import exit

import requests
from pymongo import MongoClient

import core
from web_scraping.settings import COLLECTION, DATABASE, DATABASE_CONN, URL

parser = argparse.ArgumentParser(
    description='''''', formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-user", "--user", type=str,
                    dest='user', help="Database user", default=None)
parser.add_argument("-password", "--password", type=str,
                    dest='password', help="Database password", default=None)
args = parser.parse_args()


if __name__ == "__main__":
    if args.password is None or args.user is None:
        exit()
    req = requests.get(URL)
    dataframe = core.html_to_dataframe(req.content)
    client = MongoClient(DATABASE_CONN.format(
        **{'user': args.user, 'password': args.password}))
    db = client[DATABASE]
    collection = db[COLLECTION]
    collection.insert_many(dataframe.to_dict(orient='records'))
