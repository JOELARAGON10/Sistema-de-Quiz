#Proposito hacer un cuestionario de estudio para aprender los temas de teoria en la robotica y la astronomia
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print(key)
        print("================================================================================")
        for i in options[question_num-1]:
            print(i)
        guess = input("Ingrese (A, B, C, or D): ")

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# definir si las respuestas introducidas estan bien o mal.
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        print("")
        print("================================================================================")
        
        return 1
    else:
        print("WRONG!")
        
        print("================================================================================")
        return 0
    

#Entregar al jugador el resultado obtenido tras contestar todas las preguntas.
def display_score(correct_guesses, guesses):
    print("RESULTADOS")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Tu puntaje es: "+str(score)+"%")

# Dar la opcion de si se quiere jugar otra vez.
def play_again():

    response = input("quieres jugar otr vez? (si o no): ")
    response = response.upper()

    if response == "SI":
        return True
    else:
        return False
#dar introduccion de las preguntas y las diferntes respuestas.


questions = {
 "¿Cuál es la estrella más cercana?: ": "B",
 "cuantos planetas tiene nuestro sistema solar?: ": "C",
 "Qué fue el Big Bang?: ": "D",
 "Qué es un cometa?: ": "A",
 "Qué es un agujero negro?: ": "D",
 "Qué tipos de telescopios existen?: ": "B",
 "Qué es una supernova?: ": "A",
 "Cual es el planeta mas frio de nuestro sistema solar?: ": "C",
 "Cual es el planeta mas caliente de nuestro sistema solar?: ": "D",
 "que tan lejos esta el marte de la tierra?: ": "B",
}

options = [["A. Rigel.",
            "B. El sol",
            "C. Achernar",
            "D. Procyon"],
          ["A. 10 planetas",
           "B. 7 planetas",
           "C. 8 planetas",
           "D. 9 planetas"],
          ["A. es la extincion de la la vida",
           "B. es el inicio de la humanidad en el mundo",
           "C. es el origen da la vida como la conocemos",
           "D. es el mismísimo comienzo del cosmos"],
          ["A. es un cuerpo compuesto total o parcialmente de hielo, formado en los confines del Sistema Solar.",
           "B. es una roca proveniente del espacio.",
           "C. es lo que se conoce como un avistamiento de vida proveniente de otro planeta.",
           "D. es una onda emitida por el sol."],
          ["A. es lo opuesto a una estrella.",
           "B. es un metodo de transporte que puede ser aprovechado por las naves espaciales.",
           "C. es una curvatura del espacio-tiempo.",
           "D. es una región del espacio con un tirón gravitatorio tan extremo que ni la luz puede escapar de ella."],
          ["A. de largo, corto y medio alcanze.",
           "B. refractores, reflectores y catadióptricos.",
           "C. campo oscuro,polarización,de fluorescencia.",
           "D. estelar,optico,sistematico."],
          ["A. la explosion de una estrella que libera mucha energia.",
           "B. la colision de dos planetas.",
           "C. la creacion de una nueva estrella.",
           "D. la radiacion exesiva que emite una estrella."],
          ["A. la tierra.",
           "B. Marte.",  
           "C. Neptuno.",
           "D. saturno."], 
          ["A. Marte.",
           "B. Urano.",
           "C. saturno.",  
           "D. Venus."],
           
          ["A. 75 millones de kilómetros.",
           "B. 102 millones de kilómetros.",
           "C. 90 millones de kilómetros.",
           "D. 10 millones de kilómetros."]]
         
             

new_game()

while play_again():
    new_game()

print("Gracias por participar!")

