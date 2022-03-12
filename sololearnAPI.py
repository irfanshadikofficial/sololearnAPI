#This will determine the UserID of the dedicated user :) - version3.0.4
profile_id = str(input('Paste the url of the profile or the UserID :'))
u_id = ''
print('Fetching Data From Server ...')
print('Wait Patiently ... ')
if len(profile_id) == 7:
    print(profile_id)
elif    len(profile_id) == 43:
        u_id = profile_id[-9:-1]
elif    len(profile_id) == 42:
        u_id = profile_id[-8:]
else:
    u_id = profile_id[34:]
#The Final Variable for UserID is [u_id]
#--------------------------------------Retrive Data From URI
from urllib.request import urlopen
import json
url = 'https://api.sololearn.repl.co/profile/'
#-------------------------------------version3.0.4
profileid = u_id
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
