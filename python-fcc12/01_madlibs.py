# # string concatenation (aka how to put strings together)
# # suppose we want to create a string that says "subscribe to _______ "
# youtuber = "Pablo" # some string variable

# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjetivo (participio): ")
verb1 = input("Verbo (infinitivo): ")
verb2 = input("Verbo (gerundio): ")
famous_person = input("Persona famosa: ")

madlib = f"¡Estoy {adj}! Menudo fin de semana aquí en La Alameda, \
sin parar de {verb1}. Sigamos {verb2} como si fuéramos {famous_person}!"

print(madlib)