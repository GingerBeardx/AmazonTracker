# python37
"""
A console app that tracks amazon prices and sends email notificatinos of drops in prices in order to
facilitiate smart purchases

Author: Eric Greenhalgh
Project started: 1/5/2020
"""

# requirements module imports
import mysql.connector

#native module imports
import os

num_hyphens = 90

class dbConnect():
    """ Establishes a connection to the database and facilitates database interactions """
    
    def __init__(self):
        config = {
            # Connection data is obviously sensitive and I would not include this information in
            # a production environment.  It is only here for ease of use during development.
            'host':'localhost',
            'database': 'amazonpricetracker',
            'user':'root',
            'password':'root',
            'port':'3305'
        }
        self.cnx = mysql.connector.connect(user=config['user'], password=config['password'], host=config['host'], database=config['database'], port=config['port'])
        
def login_user(email, password, user_verified):
    """ Logs in a new user to the database once valid login credentials have been supplied """
    cnx = dbConnect().cnx
    cursor = cnx.cursor()
    query = (f'''SELECT email, passwd, first_name FROM users WHERE email="{email}";''') 
    
    data = email
    result = cursor.execute(query, data)
    name = ""
                
    for r in cursor:
        if r[1] == password:
            name = r[2]
            user_verified = True
    cursor.close()
    cnx.close()
    return user_verified, name
    
def register_user():
    """ Creates a new user as long as the user supplies an unique email address """
    unique_email = False
    print("Thank you for registering. Please enter the following:")
    print("-" * num_hyphens)
    first_name = input("Please enter your first name -> ")
    last_name = input("Please enter your last name -> ")
    email = input("Please enter your email -> ")
    
    cnx = dbConnect().cnx
    cursor = cnx.cursor()
    
    while not unique_email:
        query = (f'''SELECT email FROM users WHERE email="{email}";''') 
        
        data = email
        cursor.execute(query)

        result = [r for r in cursor]                            
        
        if len(result) > 0:
            print("I'm sorry, that is not a valid email.")
            email = input("Please enter your email -> ")
        else:
            unique_email = True
        
    password = input("Please enter your password -> ")
        
    query = f'''INSERT INTO users (first_name, last_name, email, passwd)
                VALUES ("{first_name}", "{last_name}", "{email}", "{password}");'''
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()
    input(f"A new user has been created succesfully! Welcome, {first_name}! -> ")

def main():
    """ This is the main program loop that will run when this file is executed """
    
    running = True
    while running:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-" * num_hyphens)
        print("Welcome to The Amazon Price Tracker")
        print("-" * num_hyphens)
        print("Please choose one of the options below:")
        print("-" * num_hyphens)
        print("1) Register a New User")
        print("2) Login a Registered User")
        print("3) Exit Program")
        print("-" * num_hyphens)
        choice = input("Your choice -> ")
        print("-" * num_hyphens)
        
        if int(choice) == 1:
            register_user()
        elif int(choice) == 2:
            user_verified = False
            print("You are logging in. Please enter your login info:")
            print("-" * num_hyphens)
            email = input("Please enter your email address -> ")
            password = input("Please enter your password -> ")
            
            user_verified, name = login_user(email, password, user_verified)
                            
            if user_verified:
                print(f"Welcome back, {name}!")
            else:
                print("I could not find a user with those credentials.")
                print("Please try again or register a new user.")
            input("Press a key to continue -> ")
        elif int(choice) == 3:
            print('Until next time!')
            running = False
        else:
            continue
        

if __name__ == "__main__":
    main()

