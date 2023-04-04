import nomcc

# nom-tell equivalent
# nom-tell ansp zone.add name=slave.com zone-type=slave masters='((addrport 1.0.0.1))'

with nomcc.connect('ansp') as session:
    print(session.tell({'type': 'zone.add', 
        'name': 'slave.com',  
        'zone-type': 'slave',
        'masters': [['addrport', '1.0.0.2']]}))

