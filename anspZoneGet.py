import nomcc

# nom-tell equivalent
# nom-tell ansp zone.get name=test.com

with nomcc.connect('ansp') as session:
    print(session.tell({'type': 'zone.get', 'name': 'test.com'}))

