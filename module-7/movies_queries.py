import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': 'Happyhappy20!',
    'host': 'localhost',
    'database': 'movies'
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    # Select all fields for studio
    cursor.execute("SELECT studio_id, studio_name FROM studio")
    studios = cursor.fetchall()
    print("-- DISPLAYING Studio RECORDS --")
    for studio in studios:
        print("Studio ID: {}\n Studio Name: {}\n".format(studio[0], studio[1]))

    # Select all fields for genre
    cursor.execute("SELECT genre_id, genre_name AS Genre FROM genre")
    genres = cursor.fetchall()
    print("-- DISPLAYING Genre RECORDS --")
    for genre in genres:
        print("Genre ID: {}\n Genre Name: {}\n".format(genre[0], genre[1]))

    # Movie name and movie runtime less than 2 hours
    cursor.execute("SELECT film_name, film_runtime AS Short_Film FROM film WHERE film_runtime < 120")
    short_films = cursor.fetchall()
    print("-- DISPLAYING Short Film RECORDS --")
    for short_film in short_films:
        print("Film Name: {}\n Runtime: {}\n".format(short_film[0], short_film[1]))

    # List of film names and directors grouped by director
    cursor.execute("SELECT film_name, film_director AS Director FROM film ORDER BY film_director")
    directors = cursor.fetchall()
    print("-- DISPLAYING Director RECORDS in Order --")
    for director in directors:
        print("Film Name: {}\n Director: {}\n".format(director[0], director[1]))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Access denied: Wrong username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

finally:
    cursor.close()
    db.close()



















