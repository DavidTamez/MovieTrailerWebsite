import media
import fresh_tomatoes

# Get a list of the actors in each of the movies and then create an instance of a Movie class with the appropriate information.
the_conjuring_actors = ["Vera Farmiga", "Patrick Wilson", "Lili Taylor", "Ron Livingston"]
the_conjuring = media.Movie("The Conjuring",
                        "Paranormal investigators Ed and Lorraine Warren work to help a family terrorized by a dark presence in their farmhouse.",
                        "http://ia.media-imdb.com/images/M/MV5BMTM3NjA1NDMyMV5BMl5BanBnXkFtZTcwMDQzNDMzOQ@@._V1_SX214_AL_.jpg",
                        "https://www.youtube.com/watch?v=k10ETZ41q5o",
                        "PG-13", "19 July 2013", the_conjuring_actors)

final_destination_actors = ["Devon Sawa", "Ali Larter", "Kerr Smith", "Kristen Cloke"]
final_destination = media.Movie("Final Destination",
                     "After a teenager has a terrifying vision of him and his friends dying in a plane crash, he prevents the accident only to have Death hunt them down, one by one.",
                     "http://ia.media-imdb.com/images/M/MV5BMTU4OTI4OTI4OF5BMl5BanBnXkFtZTgwMDA1MzkyMTE@._V1_SX640_SY720_.jpg",
                     "https://www.youtube.com/watch?v=DD_MAz96L70",
                                "R", "17 March 2000", final_destination_actors)

identity_actors = ["John Cusack", "Ray Liotta", "amanda Peet", "John Hawkes"]
identity = media.Movie("Identity",
                       "Stranded at a desolate Nevada motel during a nasty rain-storm, ten strangers become acquainted with each other when they realize that they're being killed off one by one.",
                       "http://ia.media-imdb.com/images/M/MV5BMjE2NzgyNDYzNl5BMl5BanBnXkFtZTYwODM2Nzc2._V1_SX640_SY720_.jpg",
                       "https://www.youtube.com/watch?v=S8fjyxM7DgU",
                       "PG-13", "25 April 2003", identity_actors)

resident_evil_actors = ["Milla Jovovich", "Eric Mabius", "Colin Salmon", "Martin Crewes"]
resident_evil = media.Movie("Resident Evil", "A special military unit fights a powerful, out-of-control supercomputer and hundreds of scientists who have mutated into flesh-eating creatures after a laboratory accident.",
                             "http://upload.wikimedia.org/wikipedia/en/archive/a/a1/20130202141013!Resident_evil_ver4.jpg",
                             "https://www.youtube.com/watch?v=jiS6gtClrqk",
                            "R", "15 March 2002", resident_evil_actors)

hunger_games_actors = ["Jennifer Lawrence", "Stanley Tucci", "Liam Hemsworth"]
hunger_games = media.Movie("Hunger Games", "Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games, a televised fight to the death in which two teenagers from each of the twelve Districts of Panem are chosen at random to compete.",
                           "http://0707c778e0f1481535fe-36b693bb9065cd15445b260c56542cbf.r55.cf2.rackcdn.com//assets/df5463d8-a3df-11e2-85ca-bc764e10a080.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY",
                           "PG-13", "23 March 2012", hunger_games_actors)

silent_hill_actors = ["Radha Mitchell", "Sean Bean", "Jodelle Ferland", "Laurie Holden"]
silent_hill = media.Movie("Silent Hill", "A woman goes in search for her daughter, within the confines of a strange, desolate town called Silent Hill.",
                          "http://upload.wikimedia.org/wikipedia/en/5/57/Silent_hill.jpg",
                          "https://www.youtube.com/watch?v=f5mT5LhbRJw",
                          "R", "21 April 2006", silent_hill_actors)

# Create a list of Movie instances
movies = [the_conjuring, final_destination, identity, resident_evil, silent_hill, hunger_games]
# Create a new movie webpage by calling open_movies_page in the file fresh_tomatoes with the list of movies defined here
fresh_tomatoes.open_movies_page(movies)

