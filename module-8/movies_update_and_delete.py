//Hlee Xiong
//CSD 310 Module 8 Assignment

import mysql.connector

def show_films(cursor, title, exclude_movie=None):
  if exclude_movie:
      query = f"SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' FROM film INNER JOIN genre ON film.genre_id = genre.genre_id INNER JOIN studio ON film.studio_id = studio.studio_id WHERE film_name != '{exclude_movie}'"
  else:
      query = "SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' FROM film INNER JOIN genre ON film.genre_id = genre.genre_id INNER JOIN studio ON film.studio_id = studio.studio_id"

  cursor.execute(query)

  films = cursor.fetchall()

  print("\n-- {} --".format(title))

  for film in films:
      print("Film Name: {}\nDirector: {}\nGenre Name: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))


# Connect to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Happyhappy20!",
    database="movies"
)

# Create a cursor
cursor = connection.cursor()

# Display films before any modifications
show_films(cursor, "DISPLAYING FILMS")

# Insert a new record into the film table
cursor.execute("""
INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
VALUES ('It', 2022, 120, 'Ridley Scott', 3, 3)
""")
connection.commit()

# Display films after inserting a new record, excluding the newly added movie
show_films(cursor, "DISPLAYING FILMS AFTER INSERT", exclude_movie='It')

# Update the film 'Alien' to be a Horror film
cursor.execute("""
UPDATE film
SET genre_id = 1
WHERE film_name = 'Alien'
""")
connection.commit()

# Display films after updating 'Alien' genre
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Change Alien to Horror")

# Delete the movie 'Gladiator'
cursor.execute("""
DELETE FROM film
WHERE film_name = 'Gladiator'
""")
connection.commit()

# Display films after deleting 'Gladiator'
show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

# Close the cursor and connection
cursor.close()
connection.close()