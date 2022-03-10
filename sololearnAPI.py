#--------------------------------------Retrive Data From URI
from urllib.request import urlopen
import json
url = 'https://api.sololearn.repl.co/profile/'
profileid = int(input('Enter User ID (Exp : 20098177) :'))
link = f'{url}{profileid}'
resp = urlopen(link)
data = json.loads(resp.read())
#--------------------------------------STORAGE
name = data['userDetails']['name']
bio = data['userDetails']['bio']
level = data['userDetails']['level']
xp = data['userDetails']['xp']
countryCode = data['userDetails']['countryCode']
followers = data['userDetails']['followers']
following = data['userDetails']['following']
registerDate = data['userDetails']['registerDate']
pro = data['userDetails']['isPro']
modifiedPro = ''
badge = data['userDetails']['badges'][0]['name']
#--------------------------------------ARGUMENTS
if pro == False:
    modifiedPro = 'Free User'
else:
    modifiedPro = 'Pro User'
#--------------------------------------OUTPUT
print('[[[[[[[[    SOLOLEARN USER DETAILS THROUGH PYTHON(API)    ]]]]]]]')
print('\t')
print(f'NAME        :{name}')
print(f'BIO         :{bio}')
print(f'LEVEL       :{level}')
print(f'XP          :{xp}')
print(f'USER TYPE   :{modifiedPro}')
print(f'BADGE       :{badge.capitalize()}')
print(f'FOLLOWERS   :{followers}')
print(f'FOLLOWING   :{following}')
print(f'COUNTRY     :{countryCode.upper()}')
print(f'REG. DATE   :{registerDate[:10]} at {registerDate[11:]}')
print('\t')
print('[[[[[[[[      CREATED BY -IRFAN SHADIK- USING API        ]]]]]]]')
#@irfanshadikofficial