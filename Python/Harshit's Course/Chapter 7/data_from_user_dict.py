# Program to return
# The user data from 
# Dictionary to simple format

user={}                                                 # Dictionary

name=input("Enter your name : ")                        # User data
age=input("Enter your age : ")
fav_mov=input("Enter your favourite movies : ").split()
fav_songs=input("Enter your favourite songs : ").split()

user['name']=name                                       # Storing in Dictionary
user['age']=age
user['favourite_movies']=fav_mov
user['favourite_songs']=fav_songs

for i,j in user.items():                                # Farmatting    
    print(f"{i} : {j}")
