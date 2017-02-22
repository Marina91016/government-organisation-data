#!/usr/bin/env python3

import sys
import openpyxl

fields = ['urn', 'name']
sep = '\t'

wb = openpyxl.load_workbook(sys.argv[1])
sh = wb.get_active_sheet()

oscar = {}

print(sep.join(fields))

for r in sh.rows:
    row = {}
    row['urn'] = r[0].value
    row['name'] = r[1].value

    row['segment'] = r[4].value

    if row['urn'] == 'Organisation Code':
        continue

    if row['segment'].upper() == row['name']:
        row['name'] = row['segment']

    key = "%s:%s" % (row['urn'], row['name'])
    oscar[key] = row

for key in sorted(oscar):
    row = oscar[key]
    print(sep.join([str(row[field]) for field in fields]))