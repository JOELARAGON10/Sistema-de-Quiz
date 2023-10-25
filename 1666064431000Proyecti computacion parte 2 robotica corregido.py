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
 "Qué es exactamente un robot móvil autónomo?: ": "A",
 "Qué pasa si el robot se encuentra frente a un obstáculo?: ": "B",
 "En qué áreas o sectores se puede aplicar la robótica móvil colaborativa?: ": "C",
 "Qué entiendes por el término robótica?: ": "A",
 "Cuales son los componentes principales de un robot?: ": "D",
 "Que es un robot humanoide?: ": "B",
 "Cual es la funcion de los sensores en un robot?: ": "A",
 "A quien se le atribuye el termino robotica?: ": "C",
 "Cual es la vida media de un robot?: ": "D",
 "Cual es el objetvio de los robots?: ": "B",
}

options = [["A. dispositivos capaces de realizar tareas sin la necesidad de que nadie los dirija.",
            "B. es un robot que pueden operar con un alto grado de autonomía",
            "C. dispositivos que siguen ordenes humanas por medio de comandos",
            "D. es un robot que sirve para el proceso de datos"],
          ["A. seguira su trayectoria",
           "B. evitara el obstaculo cambiando de rumbo",
           "C. detendra sus acciones",
           "D. apagara sus circuitos"],
          ["A. industrial, negocios, finanzas",
           "B. contabilidad, marketing, agroalimentario",
           "C. industrial, agroalimentario, construcción",
           "D. ventas, recursos humanos, industrial"],
          ["A. es una rama de la ingeniería que se ocupa del estudio y control de robots inteligentes.",
           "B. es el proceso por el cual se construyen los robots.",
           "C. es una rama de la Fisica en el que se estudia como funcionan los robots.",
           "D. es transcurso que lleva a los robots a tener las funciones para las que fueron programados."],
          ["A. sistema de control,movimiento,transmision,luces.",
           "B. luces,receptor,dispositivo de rastreo,sensor.",
           "C. circuito,control,antena,dispositivo de comando.",
           "D. manipulador,controlador,dispositivo de entrada y salida,dispostivios especiales."],
          ["A. un robot diseñado para pensar como los humanos.",
           "B. un robot diseñado para imitar los movimientos de un ser humano.",
           "C. un robot diseñado para remplazar a los humanos.",
           "D. un robot diseñado para ofrecer compañia a los humanos."],
          ["A. premitir que el robot reciba informacion de todo lo que lo rodea.",
           "B. indicar al robot por donde tiene prohibido pasar.",
           "C. para marcar objetivos y que el robot pueda realizar sus tareas.",
           "D. para indicarle al robot sus ordenes de lo que debe hacer."],
          ["A. Victor Scheinman.",
           "B. George Devol.",  
           "C. Isaac Asimov.",
           "D. Joseph Engelberger."],
          ["A. 1 a 4 años.",
           "B. 5 a 10 años.",
           "C. 25 a 50 años.",  
           "D. 12 a 15 años."],
          ["A. tienen la funcion de servir y hacer todo lo que los humanos ordenen.",
           "B. tienen la finalidad de realizar varias funciones o tareas complejas que los humanos no podrian.",
           "C. sirven para proteger a los humanos como guardaespladas.",
           "D. tienen la funcion de enseñar a los humanos nuevas cosas."]]
         
             

new_game()

while play_again():
    new_game()

print("Gracias por participar!")
