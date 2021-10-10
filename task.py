#requirements:
#- don't use external libraries
#- the process of loading data can be changed if needed


import json

data = []
with open('example1.json') as f:
    for line in f:
        data.append(json.loads(line))

line1 = data[0]
line2 = data[1]
line3 = data[2]
line4 = data[3]

def flattenjson(b, delim):
    val = {}
    for i in b.keys():
        if isinstance(b[i], dict):
            get = flattenjson(b[i], delim)
            for j in get.keys():
                val[i + delim + j] = get[j]
        else:
            val[i] = b[i]

    return val
# TASK -
# the function flattenjson recursively parses a nested json structure to produce a flattended dict
# the process, in absence of arrays "[]", works as intended, see the output below:
flattenjson(line1, '__')

# in the presence(run below) of arrays the key value is 'g__h__i__j': [{'k': 'Aird'}]
flattenjson(line2, '__')
# and not 'g__h__i__j__k': 'Aird', which is the result needed.

# the task is changing the flattenjson function, ore creating a new one, that produce the output of:
flattenjson(line1, '__')
# even for line2, line3 and line4
# note: see the structure of arrays of line2, line3 and line4.
