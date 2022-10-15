
from webbrowser import get
from artHigher import logo
from artHigher import vs
from HigherData import data
import random
'''
def get_random_ac():
     return random.choice(data)
'''

#data2 = get_random_ac()

def get_account(data):
    """Format account into printable format: name, description and country"""
    data = random.choices(data)  
    for i in range(len(data)):
        name = data[i]['name']
        description = data[i]["description"]
        country = data[i]["country"]
        follower = data[i]['follower_count']
    return print("{0}, a {1}, from {2}".format(name,description,country))
#data = random.choices(data)
#acc2  =random.choice(data)
data['follower_count']
ac1 = get_account(data)
ac2 = get_account(data)   
#follow = ac1['follower_count']
#')
    
'''
    
    name = ac["name"]
    description = ac["description"]
    country = ac["country"]
    # print(f'{name}: {data["follower_count"]}')
    return print("{0}, a {1}, from {2}".format(name,description,country))
ac = random.choice(data)
c= random.choice(data)
account_a = get_account(data)
#acc = account_a.items()
#aq = acc['follower_count']
account_b = get_account(data)
#follow = data[]
#print(follow)


'''


#account_a = random.choice(data)
#account_b = random.choice(data)


#account_a = get_account(data)
#account_b = get_account(data)
#account_b = account_a
#account_bb = random.choice(data)
#account_b = get_account(account_bb)
'''
def get_follower():
    follower_a = data['follower_count']
    follower_b = data['follower_count']
    return print("{0},  {1},".format(follower_a, follower_b))
#get_follower(data)

'''




    
"""
def valueGet():
  name = data["name"]
  description = data["description"]
  country = data["country"]
  return name, description, country
  print(name+description+country)
    
print(valueGet(data))
print(logo)
print("Compare A: {}, a {}, from {}.".format())
print(vs)
input(who has more followers? Type 'A' or 'B':)
#Then A becomes B
#loop through the dictionary data
#using randomzier
#compare Instagram follower
# create Final answer leaderboard
## 
"""
'''
for i in data:
        for key,val in i.items():
            print("name is{0}, follower is {1}".format(key,val))
            #a = print(key)
            
            
           #a = print(key,val)
           '''