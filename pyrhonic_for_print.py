
numberstring = '112,124,0.23,12345,1345667,.5678,-.12,-12345,.67,-234'

print(sum(float(number) for  number in numberstring.split(',')))


