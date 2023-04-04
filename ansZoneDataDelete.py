import nomcc

# nom-tell equivalent
# nom-tell ansp zone.update-data name=test.com delete='("newhost")'

with nomcc.connect('ansp') as session:
    print(session.tell({'type': 'zone.update-data',
        'name': 'test.com',
        'delete': ['newhost']}))

