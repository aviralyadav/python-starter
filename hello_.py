import re

message='hello 122-123-1234 yessss sds 345-567-6789 is all'
phoneNumberRex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumberRex.findall('hello 122-123-1234 yessss sds 345-567-6789 is all')
print(mo) #for multiple search

mo = phoneNumberRex.search('hello 122-123-1234 yessss sds 345-567-6789 is all')
print(mo.group()) # for single search
