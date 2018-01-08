import media
import fresh_tomatoes

#Creating movie instances
aruvi = media.Movie("Aruvi","Aruvi is a gentle yet spirited girl who decides to break bad and rebel against the oppressive forces that has treated her unfairly. Her audacity to vent out is not without consequences","https://upload.wikimedia.org/wikipedia/en/a/a0/Aruvi_First_Look_Poster.jpg","https://www.youtube.com/watch?v=jgYYxs_d_bo")
predestination = media.Movie("Predestination","An agent is tasked to travel back in time to prevent a bomb attack in New York in 1975.","https://upload.wikimedia.org/wikipedia/en/4/4b/Predestination_poster.jpg","https://www.youtube.com/watch?v=xxG-YfedrfU")
source_code = media.Movie("Source Code","Army pilot Stevens, recruited for a top-secret operation, finds himself in the body of an unknown man. Soon, he is on a mysterious trail to track down the bomber of the Chicago commuter train.","https://upload.wikimedia.org/wikipedia/en/e/e5/Source_Code_Poster.jpg","https://www.youtube.com/watch?v=t5roJgHV_lA")
arrival = media.Movie("Arrival","Louise Banks, a linguistics expert, along with her team, must interpret the language of aliens who've come to earth in a mysterious spaceship.","https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg","https://www.youtube.com/watch?v=ZLO4X6UI8OY")
shutter_island = media.Movie("Shutter Island","Teddy Daniels and Chuck Aule, two US marshals, are sent to an asylum on a remote island in order to investigate the disappearance of a patient, but Teddy uncovers a shocking truth about the place.","https://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg","https://www.youtube.com/watch?v=5iaYLCiq5RM")
beautiful_mind = media.Movie("Beautiful Mind","John Nash, a brilliant but asocial mathematical genius, finds himself in pain when he encounters a cruel disorder. He ultimately overcomes his struggles and emerges free of any trauma.","https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg","https://www.youtube.com/watch?v=WFJgUm7iOKw")

#Adding all the movies to a list
movies = [aruvi, predestination, source_code, arrival, shutter_island, beautiful_mind]

#Call open_movies_page methos to display all the movies
fresh_tomatoes.open_movies_page(movies)

