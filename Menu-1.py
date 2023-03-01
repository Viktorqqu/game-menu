from tkinter import *
import tkinter.ttk as ttk
import tkinter as tk
import random
import winsound
import pygame_menu
import pygame


pygame.init()
surface = pygame.display.set_mode((600, 400))
bg_image = pygame.image.load("fonnjpg.jpg")








def start_the_game():
    # Do the job here !


    questions = {
        "Какой язык программирования используется для создания приложений для Android?": "Java",
        "Как называется операционная система, разработанная компанией Apple?": "MacOS",
        "Какой цвет получится при смешении желтого и красного?": "Оранжевый",
        "Какое животное изображено на флаге Австралии?": "Кенгуру",
        "Какая столица у Швеции?": "Стокгольм",
        "Какой металл является самым распространенным на Земле?": "Желзо",
        "Какой город является столицей России?": "Москва",
        "Как называется научная дисциплина, которая изучает процессы в организмах и клетках?": "Биология",
        "Какой континент является самым большим по площади?": "Азия",
        "Какое животное является символом государства США?": "Орёл",
        "Кто был первым космонавтом?": "Юрий Гагарин",
        "Какой год был концом Второй мировой войны?": "1945",
        "Какой год был началом Первой мировой войны?": "1914",
        "Кто написал Войну и мир? ": "Лев Толстой",
        "Как называется крупнейшее озеро в мире по площади?": "Каспийское",
        "Как называется самая большая планета в Солнечной системе?": "Юпитер",
        "Как называется самое большое животное на Земле?": "Голубой кит",
        "Кто написал Мертвые души?": "Николай Гоголь",
        "Кто написал Идиот?": "Федор Достоевский",
        "Как называется самое большое государство по территории?": "Россия",
        "Какой цвет имеет костюм Санты Клауса?": "Красный",
        "Какой цвет имеют бананы?": "Жёлтый",
        "Как зовут главного персонажа мультфильма Том и Джерри?": "Том",
        "Как зовут главного персонажа сказки Красная Шапочка?": "Красная Шапочка",
        "Сколько пальцев на руке у человека?": "5",
        "Как называется наука, которая изучает растения?": "Ботаника",
        "Сколько ног у паука?": "8",
        "Какое животное является символом Китая?": "Панда",
        "Какоке из чисел(12, 30, 89, 100) не делится на 2": "89",
        "Как зовут основателя компании Apple?": "Стив Джобс",
        "":"",
        "":"",
        "":"",
        "":"",
































    }   






    sked_questions = []  # список уже заданных вопросов

    def choose_question():
        available_questions = list(set(question_list) - set(asked_questions))  # список вопросов, которые еще не были заданы
        if not available_questions:  # если все вопросы уже были заданы, начните заново
            asked_questions.clear()
            available_questions = question_list
        question = random.choice(available_questions)
        asked_questions.append(question)  # добавить вопрос в список заданных вопросов
        return question, questions[question]






    question_list = list(questions.keys())


    def choose_question():
        question = random.choice(question_list)
        return question, questions[question]


    def check_answer():
        global score
        user_answer = answer.get()
        if user_answer == current_answer:
            result.config(text="Верно!", fg="green")
            score += 1
            winsound.PlaySound("E:/project/python/game/AnswerTheQuestion/Lose.wav", winsound.SND_ASYNC)
        else:
            result.config(text="Неверно!", fg="red")
            winsound.PlaySound("E:/project/python/game/AnswerTheQuestion/Lose.wav", winsound.SND_ASYNC)
        score_label.config(text="Очки: {}".format(score))



    def show_other_apps():
    # список других приложений
        other_apps = ["Калькулятор", "Календарь", "Блокнот", "Видеоплеер", "Музыкальный плеер"]

    # создание окна меню
        menu_win = Toplevel(root)
        menu_win.title("Другие приложения")
        menu_win.geometry("300x200")

    # создание элементов меню
        label = Label(menu_win, text="Другие приложения:")
        label.pack(pady=10)

        for app in other_apps:
            app_button = Button(menu_win, text=app, command=lambda: print(app))
            app_button.pack(pady=100)

    # отображение окна меню
        menu_win.mainloop()




    def create_widgets():
    # кнопка для отображения других приложений
        other_apps_button = Button(root, text="Другие приложения", font=("Arial", 40), command=show_other_apps, relief="raised")
        other_apps_button.pack(anchor="nw", padx=20, pady=20)

    # остальные элементы интерфейса
        question.pack(pady=20)
        answer.pack(pady=10)
        submit.pack(pady=10)
        result.pack(pady=10)
        new_question_button.pack(pady=10)
        score_label.pack(pady=10)






    def new_question():
        global current_question, current_answer
        current_question, current_answer = choose_question()
        question.config(text=current_question, fg="black")
        result.config(text="")
        answer.delete(0, END)





    root = Tk()
    root.title("Игра: ответь на вопрос")
    root.geometry("1980x1200")
    root.configure(background='#FFDAB9')

















    menu = Menu(root)
    root.config(menu=menu)
    file_menu = Menu(menu)
    menu.add_cascade(label="Файл", menu=file_menu)
    file_menu.add_command(label="Выход", command=root.quit)


    button_style = {'bg': '#FF1493', 'fg': 'white', 'font': ("Arial", 12), 'border-radius': '20px', 'border': 'none',
                    'activebackground': '#1976D2', 'activeforeground': 'white'}



    question = Label(root, text="", font=("Arial", 30))
    question.pack(pady=20)
    answer = Entry(root, font=("Arial", 30))
    answer.pack(pady=10)
    submit = Button(root, text="Ответить", font=("Arial", 30), bg="#4CAF50", fg="white", command=check_answer)
    submit.pack(pady=10)
    result = Label(root, text="", font=("Arial", 30))
    result.pack(pady=10)
    new_question_button = Button(root, text="Новый вопрос", font=("Arial", 30), bg="#2196F3", fg="white", command=new_question)
    new_question_button.pack(pady=10)
    score = 0
    score_label = Label(root, text="Очки: {}".format(score), font=("Arial", 30))
    score_label.pack(pady=10)


    new_question()


    root.mainloop() 
























    pass



def chislo_game():
    class GuessingGame:
        def __init__(self):
            self.number_to_guess = random.randint(1, 100)
            self.guesses_left = 10
        
        # создаем главное окно
            self.main_window = tk.Tk()
            self.main_window.geometry("1980x1200")
            self.main_window.title("Игра Угадай Число")
            self.main_window.configure(bg="#FFDAB9")

        # создаем виджеты
            self.create_widgets()

        

        # запускаем главный цикл
            self.main_window.mainloop()

        def create_widgets(self):
        # Определяем параметры текстового виджета
            self.text = tk.StringVar()
            self.text.set("Угадайте число от 1 до 100")
            self.label = tk.Label(self.main_window, textvariable=self.text, font=("Arial", 20))

        # Определяем параметры поля ввода
            self.entry = tk.Entry(self.main_window)

        # Определяем параметры кнопок
            self.button = tk.Button(self.main_window, text="Проверить", command=self.check_guess)
            self.new_game_button = tk.Button(self.main_window, text="Новая игра", command=self.new_game)

        # Конфигурируем шрифт и размер шрифта для текстового виджета и кнопок
            self.label.configure(font=("Arial", 20))
            self.button.configure(font=("Arial", 16))
            self.new_game_button.configure(font=("Arial", 16))

        # Размещаем виджеты на окне
            self.label.pack(pady=10)
            self.entry.pack(pady=10)
            self.button.pack(pady=10)
            self.new_game_button.pack(pady=10)



    



        def check_guess(self):
            guess = int(self.entry.get())
            self.entry.delete(0, tk.END)

            if guess == self.number_to_guess:
                self.text.set("Поздравляем! Вы угадали число.")
                self.button.config(state="disabled")
            elif guess < self.number_to_guess:
                self.text.set("Загаданное число больше.")
            else:
                self.text.set("Загаданное число меньше.")

            self.guesses_left -= 1
            self.new_game_button.config(state="normal")
            self.label.config(text=f"Осталось попыток: {self.guesses_left}")

            if self.guesses_left == 0:
                self.text.set(f"Вы проиграли. Загаданное число было {self.number_to_guess}.")
                self.button.config(state="disabled")
                self.new_game_button.config(state="normal")

        def new_game(self):
            self.number_to_guess = random.randint(1, 100)
            self.guesses_left = 10
            self.label.config(text="Угадайте число от 1 до 100")
            self.button.config(state="normal")
            self.new_game_button.config(state="disabled")


    game = GuessingGame()


pass
    






















main_theme = pygame_menu.themes.THEME_DARK.copy()


menu = pygame_menu.Menu('', 600, 400,
                        theme=pygame_menu.themes.THEME_DARK)


menu.add.button('Ответь правильно', start_the_game)
menu.add.button('Угадай число', chislo_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

while True:

    surface.blit(bg_image, (0, 0))




    

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if menu.is_enabled():
        menu.update(events)
        menu.draw(surface)

    pygame.display.update()