"""
Really basic bootstrap script

Only expected to be called in dockerfile to initialise /etc/config.json with parsed through items
and always expected to receive admissible values
"""
from argparse import ArgumentParser
import json

parser = ArgumentParser()
parser.add_argument("dbHost")
parser.add_argument("dbName")
parser.add_argument("dbUser")
parser.add_argument("dbPwd")
args = parser.parse_args()


data = {'dbHost': args.dbHost,
        'dbName': args.dbName,
        'dbUser': args.dbUser,
        'dbPwd': args.dbPwd
        }

with open('/etc/config.json', 'w') as outfile:
    json.dump(data, outfile)
