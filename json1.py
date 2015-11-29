__author__ = 'kwoshvick'

import json
input2 = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]'''

info = json.loads(input2)
print('user count', len(info))

for item in info:
    print('Name',item['name'])
    print('Id',item['id'])
    print('Attribute',item['x'])
