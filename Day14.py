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

first_comparison = random.randint(0, len(data))
print(data[first_comparison])
