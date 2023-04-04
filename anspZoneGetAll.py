import nomcc

#nom-tell equivalent
#nom-tell ansp zone.mget

with nomcc.connect('ansp') as session:
    for r in session.sequence('zone.mget'):
        print(r)
    

