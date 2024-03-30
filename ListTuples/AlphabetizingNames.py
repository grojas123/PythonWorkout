def alphabetize_names(PEOPLE):
   return sorted(PEOPLE, key=lambda k: k['last'])


PEOPLE = [{'first':'Reuven', 'last':'Lerner',
   'email':'reuven@lerner.co.il'},
{'first':'Donald', 'last':'Trump',
   'email':'president@whitehouse.gov'},
{'first':'Vladimir', 'last':'Putin',
   'email':'president@kremvax.ru'}
]
print(alphabetize_names(PEOPLE))