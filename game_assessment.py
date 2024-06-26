# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'TOP100GAMES.ASSESSMENT.db'

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
while menu_choice != 'z':
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
                        'Z: Exit\n\nType option here: ')
    menu_choice = menu_choice.upper()
    if menu_choice == 'A': 
        print('all games and genres')
    if menu_choice == 'B': 
        print('all games made after 2000 order by descending order')
    if menu_choice == 'C': 
        print('all games with Action-adventure genre descending by year')
    if menu_choice == 'D': 
        print('all games with adventure genre')
    if menu_choice == 'E': 
        print('all games with strategy genre')
    if menu_choice == 'F': 
        print('every game')
    if menu_choice == 'G': 
        print('game, publisher, genre')
    if menu_choice == 'H': 
        print('games and publishers')
    if menu_choice == 'I': 
        print('games where publisher is nintendo')
    if menu_choice == 'J': 
        print('games where the publisher is mojand or bandai')
    if menu_choice == 'K': 
        print('games and year')
    