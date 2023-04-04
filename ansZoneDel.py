import nomcc

# nom-tell equivalent
# nom-tell ansp zone.delete name=test.com

with nomcc.connect('ansp') as session:
    print(session.tell({'type': 'zone.delete', 'name': 'test.com'}))

