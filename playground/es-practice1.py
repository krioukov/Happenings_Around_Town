#!/usr/bin/python3
'''Playing with python elasticsearch low level client'''
import requests, json
from pprint import pprint
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, DocType
'''
# check ES is up and running
res = requests.get('http://localhost:9200')
print(res.content)
'''
# connect to ES server
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

event1 = {
    'address': '124 Ellis Street, San Francisco, CA',
    'cost': 'free',
    'date': 'Fri Feb 9',
    'link': 'https://www.sfstation.com//dj-karma-at-flightfridays-e2339977',
    'name': 'DJ Karma at #FlightFridays',
    'tags': ['Clubs', 'Music'],
    'time': '9p-2a'}

event2 = {
    'address': '124 Ellis Street, San Francisco, CA',
    'cost': 30,
    'date': 'Fri Feb 9',
    'link': 'https://www.sfstation.com//flight-fridays-guest-list-2-9-2018-e2338597',
    'name': 'Flight Fridays Guest List - 2.9.2018',
    'tags': ['Clubs', 'Art'],
    'time': '09:00 PM'}

event3 = {
    'address': '540 Howard Street, San Francisco, CA',
    'cost': 15,
    'date': 'Fri Feb 9',
    'link': 'https://www.sfstation.com//don-diablo-e2338813',
    'name': 'Don Diablo',
    'tags': ['Clubs',
             'Music',
             'Dance Club',
             "DJ's",
             'Electronic Music',
             'Hip Hop',
             'House Music'],
    'time': '10pm-2am'}


# store event data using elasticsearch
es.index(index='event_test', doc_type='practice', id=1, body=event1)
es.index(index='event_test', doc_type='practice', id=2, body=event2)
es.index(index='event_test', doc_type='practice', id=3, body=event3)

'''
# query data with specific tags
pprint(es.search(index='event_test', doc_type='practice',
                 body={"query": {
                     "constant_score": {
                         'filter': {
                             'term': {
                                 "cost": 'free'
                             }
                         }
                     }
                 }
            }))
'''

# query cost by range
pprint(es.search(index='event_test', doc_type='practice',
                 body={"query": {
                     "constant_score": {
                         'filter': {
                             'range': {
                                 "cost": {
                                     "gte": 10,
                                     "lt": 40
                                 }
                             }
                         }
                     }
                 }
            }))




'''
pprint(es.get(index='event_test', doc_type='practice', id=1))
pprint(es.get(index='event_test', doc_type='practice', id=2))
pprint(es.get(index='event_test', doc_type='practice', id=3))
'''