import nomcc

# nom-tell equivalent
# nom-tell ansp zone.add name=test.com zone-type=master
# nom-tell ansp zone.update-data name=test.com add='("@ 3600 IN SOA ns hostmaster 602 3600 1800 1800 1800","@ 3600 IN NS ns")'

with nomcc.connect('ansp') as session:
    print(session.tell({'type': 'zone.add', 'name': 'test.com',  'zone-type': 'master'}))
    print(session.tell({'type': 'zone.update-data',
        'name': 'test.com',
        'add': ['@ 3600 IN SOA ns hostmaster 602 3600 1800 1800 1800','@ 3600 IN NS ns']}))

