import nomcc

# nom-tell equivalent
# nom-tell ansp zone.update-data name=test.com add='("subzone.test.com 3600 IN NS ns","ns 3600 IN NS ns")'
# nom-tell ansp zone.add name=subzone.test.com zone-type=master
# nom-tell ansp zone.update-data name=subzone.test.com add='("@ 3600 IN SOA ns hostmaster 602 3600 1800 1800 1800","@ 3600 IN NS ns")'

with nomcc.connect('ansp') as session:
    print(session.tell({'type': 'zone.update-data',
        'name': 'test.com',
        'add': ['subzone.test.com. 3600 IN NS ns','ns 3600 IN A 10.0.0.1']}))
    print(session.tell({'type': 'zone.add', 'name': 'subzone.test.com',  'zone-type': 'master'}))
    print(session.tell({'type': 'zone.update-data',
        'name': 'subzone.test.com',
        'add': ['@ 3600 IN SOA ns hostmaster 602 3600 1800 1800 1800','@ 3600 IN NS ns']}))

