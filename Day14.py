# This is a program for a simple form of the higher-lower game
# In this game you'd be giving two options to choose which has the highest instagram follower count.

import random 


# Ascii art
print(
    """
    __  ___       __                 
   / / / (_)___ _/ /_  ___  _____    
  / /_/ / / __ `/ __ \/ _ \/ ___/    
 / __  / / /_/ / / / /  __/ /        
/_/ /_/_/\__, /_/ /_/\___/_/         
   / /  /____/_      _____  _____    
  / /   / __ \ | /| / / _ \/ ___/    
 / /___/ /_/ / |/ |/ /  __/ /        
/_____/\____/|__/|__/\___/_/         
    """
)

vs_logo = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
            
"""

# Program's data 
data = [
  {
    'name': 'Instagram',
    'follower_count': 346,
    'description': 'Social media platform',
    'country': 'United States'
  },
  {
    'name': 'Cristiano Ronaldo',
    'follower_count': 215,
    'description': 'Footballer',
    'country': 'Portugal'
  },
  {
    'name': 'Ariana Grande',
    'follower_count': 183,
    'description': 'Musician and Actress',
    'country': 'United States'
  },
  {
    'name': 'Dwayne Johnson',
    'follower_count': 181,
    'description': 'Actor and professional wrestler',
    'country': 'United States'
  },
  {
    'name': 'Taylor Swift',
    'follower_count': 131,
    'description': 'Musician',
    'country': 'United States'
  },
  {
    'name': 'Kendall Jenner',
    'follower_count': 127,
    'description': 'Reality TV personality and model',
    'country': 'United States'
  },
  {
    'name': 'Jennifer Lopez',
    'follower_count': 119,
    'description': 'Musician and actress',
    'country': 'United States'
  },
  {
    'name': 'Nicki Minaj',
    'follower_count': 113,
    'description': 'Musician',
    'country': 'Trinidad and Tobago'
  },
  {
    'name': 'National Geographic',
    'follower_count': 135,
    'description': 'Magazine',
    'country': 'United States'
  },
  {
    'name': 'Justin Bieber',
    'follower_count': 133,
    'description': 'Social media platform',
    'country': 'Canada'
  }
]

first_comparison = random.randint(0, len(data)-1)
second_comparison = random.randint(0, len(data)-1)
if second_comparison == first_comparison:
    second_comparison -= 1

score = 0
response = False
def start():
  print(f"compare A: {data[first_comparison]['name']}, a {data[first_comparison]['description']}, from {data[first_comparison]['country']}")
  print(
    """
   _    __    
  | |  / /____
  | | / / ___/
  | |/ (__  ) 
  |___/____(_)
            
  """
  )
  print(f"compare A: {data[second_comparison]['name']}, a {data[second_comparison]['description']}, from {data[second_comparison]['country']}")
  resp = input('Who has more followers? Type "A" or "B": ')
  if resp == "A":
     response = True
  else: 
     response = False
  return response
  

def update_score(response):
  if response == True and data[first_comparison]['follower_count'] > data[second_comparison]['follower_count']:
    #if response == "A":
    print("You're right!")
    score += 1
    return score
  else: print("You're wrong! oops")
  print()


print(f"Your current score is: {score}")
update_score(start())

# Display art


# Generate a random account from the game data.


# Format the account data into printable format


# Check if user is correct.
## Get follower count of each account.
## Use if statement to check if user is correct.

# Give user feedback on their guess.

# Score keeping.

# Make the game repeatable.