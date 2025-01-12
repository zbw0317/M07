# 2. Quiz game - match, break, continue statements

# Program symulujący quiz, który wczyta serię pytań i odpowiedzi typu prawda/fałsz z pliku questions.csv. 
# Program ma wyświetlać pytania kolejno i oczekiwać na odpowiedź użytkownika. 
# Poprawna odpowiedź prowadzi do następnego pytania. Gdy użytkownik wpisze skip pomiń pytanie, 
# a gdy wpisze exit natychmiast zakończ quiz. Nie wymagaj ponownego odpowiadania na błędne odpowiedzi; 
# zamiast tego, przechodź do kolejnego pytania. Na zakończenie podaj liczbę poprawnych odpowiedzi 
# uzyskaną przez użytkownika. Wskazówka: Wykorzystaj poznane instrukcje: match, break i continue.


import csv

FILE_PATH = '02-questions.csv'


def load_questions(filename):
    questions = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            questions.append((row[0], row[1].lower()))
    return questions


def run_quiz(questions):
    correct_answers = 0
    for question, answer in questions:
        print(question)
        user_answer = input("Your answer (true/false, skip, exit): ").lower()

        match user_answer:    # korzystamy z konstrukcji match
            case "exit":
                print("Exiting the quiz...")
                break         # przerywa działanie programu
            case "skip":
                print("Skipping to the next question...\n")
                continue      # przeskakuje do kolejnej iteracji pętli

        if user_answer == answer:
            print("Correct!\n")
            correct_answers += 1
        else:
            print(f"Wrong answer. The correct answer was: {answer}\n")

    return correct_answers


def main():
    questions = load_questions(FILE_PATH)
    correct_answers = run_quiz(questions)
    print(f"Quiz finished. You got {correct_answers} out of {len(questions)} questions right.")


if __name__ == '__main__':
    main()








# import csv

# def quiz_from_file(filename):
#     try:
#         # Wczytywanie pytań i odpowiedzi z pliku CSV
#         with open(filename, 'r', encoding='utf-8') as file:
#             reader = csv.reader(file)
#             questions = [row for row in reader]

#         correct_answers = 0
#         print("Rozpoczynamy quiz! Odpowiadaj 'tak' lub 'nie', wpisz 'skip', aby pominąć pytanie, lub 'exit', aby zakończyć quiz.")

#         for question, correct_answer in questions:
#             while True:
#                 user_input = input(f"{question} (tak/nie): ").strip().lower()

#                 match user_input:
#                     case 'exit':
#                         print("Kończymy quiz!")
#                         print(f"Liczba poprawnych odpowiedzi: {correct_answers}")
#                         return
#                     case 'skip':
#                         print("Pytanie pominięte.")
#                         break
#                     case 'tak' | 'nie':
#                         if user_input == correct_answer:
#                             print("Poprawna odpowiedź!")
#                             correct_answers += 1
#                         else:
#                             print("Niepoprawna odpowiedź.")
#                         break
#                     case _:
#                         print("Niepoprawny wybór, spróbuj ponownie.")

#         print("Quiz zakończony!")
#         print(f"Liczba poprawnych odpowiedzi: {correct_answers}")

#     except FileNotFoundError:
#         print(f"Plik {filename} nie został znaleziony.")
#     except Exception as e:
#         print(f"Wystąpił błąd: {e}")

# Uruchomienie quizu z pliku questions.csv
# quiz_from_file('quest?ions.csv')