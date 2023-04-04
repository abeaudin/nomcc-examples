import nomcc

# nom-tell equivalent
# nom-tell ansp zone.update-data name=test.com add='("newhost 3600 IN A 1.2.3.4")'

with nomcc.connect('ansp') as session:
    print(session.tell({'type': 'zone.update-data',
        'name': 'test.com',
        'add': ['newhost 3600 IN A 1.2.3.4']}))

