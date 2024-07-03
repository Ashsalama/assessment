# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'TOP100GAMES.ASSESSMENT.db'

TABLES = ("games "
           "Left join publisher_ID on games.publisher_ID = publisher_ID .publisher_ID "
           "Left join platform_ID on games.platform_ID = platform_ID .platform_ID ")

def print_parameter_query(fields:str, where:str, parameter):
    """ Prints the results for a parameter query in tabular form. """
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = ("SELECT " + fields + " FROM " + TABLES + " WHERE " + where)
    cursor.execute(sql,(parameter,))
    results = cursor.fetchall()
    print(tabulate(results,fields.split(",")))
    db.close()  

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()
menu_choice =''
while menu_choice != 'Z':
    menu_choice = input('Welcome to the top games database\n\n'
                        'Type the letter for the information you want:\n'
                        'A: All games and their genre\n'
                        'B: All games made after the year 2000\n'
                        'C: All games with action-adventure genre\n'
                        'D: All games with adventure genre\n'
                        'E: All games with strategy genre\n'
                        'F: All games\n'
                        'G: All games, publisher, and genre\n'
                        'H: all games and publishers\n'
                        'I: All games where publisher is Nintendo\n'
                        'J: All games where publisher is Mojang or Bandai\n'
                        'K: All games and year\n'
                        'X: Choose the game you would like to see\n'
                        'Z: Exit\n\nType option here: ')
    menu_choice = menu_choice.upper()
    if menu_choice == 'A': 
        print_query('all games and genres')
    elif menu_choice == 'B': 
        print_query('all games made after 2000 order by descending order')
    elif menu_choice == 'C': 
        print_query('all games with Action-adventure genre descending by year')
    elif menu_choice == 'D': 
        print_query('all games with adventure genre')
    elif menu_choice == 'E': 
        print_query('all games with strategy genre')
    elif menu_choice == 'F': 
        print_query('every game')
    elif menu_choice == 'G': 
        print_query('game, publisher, genre')
    elif menu_choice == 'H': 
        print_query('games and publishers')
    elif menu_choice == 'I': 
        print_query('games where publisher is nintendo')
    elif menu_choice == 'J': 
        print_query('games where the publisher is mojand or bandai')
    elif menu_choice == 'K': 
        print_query('games and year')
    elif menu_choice == 'X':
       game = input('Which games would you like to see: ')
       print_parameter_query("game, genre, publisher, platform, year", "game = ? ORDER BY game DESC",game)



