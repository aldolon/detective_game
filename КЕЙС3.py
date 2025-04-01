import random
from localizer import *

# Варианты элементов
weapons = ["Револьвер", "Веревка", "Свинцовая труба", "Отравленное вино", "Шарф"]
locations = ["Библиотека", "Погреб", "Зимний сад", "Ванная комната", "Кухня"]
motives = ["Наследство", "Самооборона", "Месть", "Устранение свидетеля", "Жертвоприношение"]

weapon_clues = {
    "Револьвер": [
        "“На каминной полке шесть свечей, но только пять следов воска, будто одну специально задули”",
        "“В старинной коллекции графа пропал экземпляр 1873 года”",
        "“В коллекции музыкальных шкатулок не хватало той, что играла “Шесть маленьких барабанщиков”"
    ],

    "Веревка": [
        "Мокрые вещи были разбросаны по всей комнате"
        "Кто-то зажег камин, хотя за окном стояла июльская жара "
        "В спальне одно окно распахнуто, подхваты на шторе отсутствуют"
    ],

    "Свинцовая труба": [
        "В водостоке найден необычный осадок - серые кристаллы, которых не должно быть в дождевой воде"
        "Ковер в гостинной был сожжен, по-видимому серной кислотой, которая отдавала неприятным запахом"
        "На чердаке найдены обрывки старой газеты с заметкой о краже металлических деталей"
    ],

    "Отравленное вино": [
        "Застолье организовывала сестра Графа"
        "В мусорке были найдены осколки темного стекла"
        "Скатерть с кухонного стола была замочена с содой"
    ],

    "Шарф": [
        "В гардеробе висит пальто с неестественно вытяну"
        "Несмотря на жару, жертва была в высоком воротнике"
        "На шее жертвы заметны белые разводы, будто что-то стёрло её макияж"

    ]
}

location_clues = {
    "Библиотека": [
        "Воздух здесь пропитан ароматом старых фолиантов и чего-то ещё - сладковатого, почти лекарственного"
        "Лишь здесь ощущалось насколько по-настоящему был богат хозяин дома"
        "Только здесь хозяин особняка мог забыть о своих проблемах и понаблюдать за людьми со стороны"
    ],

    "Погреб": [
        "Скрипучие ступени лестницы пронумерованы мелом, но цифра “13” зачеркнута трижды"
        "В углу стоит дубовая бочка с выцарапанной надписью 'Последний тост'"
        "В ночь убийства что-то нарушило там многовековой холо"
    ],

    "Зимний сад": [
        "Несмотря на холод снаружи, днём здесь теплее, чем обычно"
        "По ночам здесь страшно находиться, кажется, что ты не один из-за пугающих теней"
        "На стеклянной стене обнаружен едва заметный отпечаток - будто от прикосновения едва теплой ладони"
    ],

    "Ванная комната": [
        "В шкафчике лежит пузырёк с этикеткой “для полоскания”, но жидкость внутри маслянистая и пахнет булочками с корицей"
        "На полу - мокрый след, ведущий к закрытому шкафчику, но полотенца внутри абсолютно сухие"
        "Зеркало даёт странное отражение - будто его повернули после происшествия"
    ],

    "Кухня": [
        "В углу валяется разбитая чашка - осколки разлетелись неестественно ровно, будто удар был направленным"
        "На столе лежит раскрытая поваренная книга, но страница с рецептом “Миндального печенья” аккуратно вырвана по линии сгиба"
        "На большой белой двери висят разные картинки из путешествий"
    ]
}

motive_clues = {
    "Наследство": [
        "В календаре отмечен день рождения человека, умершего 20 лет назад"
        "Для проведения застолья в особняке Графа был важный повод"
        "В записной книжке были обнаружены контактные данные уважаемого юриста"
    ],

    "Самооборона": [
        "На двери были обнаружены царапины только с одной стороны - там где обычно стоит зеркало"
        "Под ногтями жертвы можно было заметить кровь"
        "За тумбой была найдена открытая аптечка, в которой отсутствовал йод и бинт"
    ],

    "Месть": [
        "В книге отзывов театра сохранилась программа с пометкой “Все получат по заслугам”"
        "На удивление, в день застолья, на лице пожилой дамы присутствовало выражение излишней удовлетворенности"
        "В туфлях, которые надежно спрятаны под кроватью, были найдены маленькие кусочки стекла"
    ],

    "Устранение свидетеля": [
        "Когда жертва зашла в помещение, она увидела того, кто не должен был находится в этой комнате"
        "За шкафом был спрятан блокнот, в котором прописаны все передвижения жертвы"
        "На столе в компьютере найдены записи с камер-видеонаблюдения, установленных в доме жертвы"
    ],

    "Жертвоприношение": [
        "Лунный календарь открыт на странице с отметкой “Полнолуние”, хотя сегодня 3-ая четверть"
        "Это место было выбрано не случайно, ведь оно являлось сакральным"
        "На стене виднелся едва заметный символ, который не принадлежит известным религиям"
    ]
}


# Загаданные элементы
correct_weapon = random.choice(weapons)
correct_location = random.choice(locations)
correct_motive = random.choice(motives)

# Создание команд
teams = {}
for i in range(3):
    team_name = input(enter_team_name.format(i + 1))
    teams[team_name] = {
        'lives': 3,
        'score': 0,
        'guesses': {'weapon': None, 'location': None, 'motive': None},
        'found_clues': []
    }

guessed_weapon = False
guessed_location = False
guessed_motive = False

def get_available_categories():
    available = []
    if not guessed_weapon:
        available.append('weapon')
    if not guessed_location:
        available.append('location')
    if not guessed_motive:
        available.append('motive')
    return available

def get_random_clue():
    available = get_available_categories()
    if not available:
        return None

    category = random.choice(available)
    if category == 'weapon':
        clue = random.choice(weapons)
    elif category == 'location':
        clue = random.choice(locations)
    else:
        clue = random.choice(motives)
    return (category, clue)

# Основной игровой цикл
game_over_flag = False
while not game_over_flag:
    for team_name, team in list(teams.items()):
        if team['lives'] <= 0:
            continue

        print(f"\nХод команды {team_name}:")
        print(f"{lives}: {'❤️' * team['lives']}")
        print(f"{score}: {team['score']}")
        print(f"1. {search_room}")
        print(f"2. {interrogate}")
        print(f"3. {hack_computer}")
        print(f"4. {experiment}")
        print(f"5. {make_guess}")
        print(f"6. {view_hints}")     

        choice = input(choose_action)

        if choice in ['1', '2', '3', '4']:  # Получение подсказки
            if random.random() < 0.5:
                clue = get_random_clue()
                if clue:
                    category, clue_text = clue
                    team['found_clues'].append((category, clue_text))
                    print(found_clue.format(clue_text))
                else:
                    print(no_new_clues)
            else:
                team['lives'] -= 1
                print(trap_triggered)

        elif choice == '5':  # Сделать предположение
            print("\nЧто вы хотите угадать?")
            print("1. Орудие убийства")
            print("2. Место преступления")
            print("3. Мотив убийства")

            guess_type = input("Ваш выбор (1-3): ")

            if guess_type == '1' and not guessed_weapon:
                guess = input(f"\n{weapons}\nВведите ваш ответ: ")
                if guess == correct_weapon:
                    print(correct_guess.format("орудие"))
                    team['score'] += 1
                    team['guesses']['weapon'] = correct_weapon
                    guessed_weapon = True
                else:
                    print(wrong_guess.format("орудие"))
                    team['lives'] -= 1

            elif guess_type == '2' and not guessed_location:
                guess = input(f"\n{locations}\nВведите ваш ответ: ")
                if guess == correct_location:
                    print(correct_guess.format("место"))
                    team['score'] += 1
                    team['guesses']['location'] = correct_location
                    guessed_location = True
                else:
                    print(wrong_guess.format("место"))
                    team['lives'] -= 1

            elif guess_type == '3' and not guessed_motive:
                guess = input(f"\n{motives}\nВведите ваш ответ: ")
                if guess == correct_motive:
                    print(correct_guess.format("мотив"))
                    team['score'] += 1
                    team['guesses']['motive'] = correct_motive
                    guessed_motive = True
                else:
                    print(wrong_guess.format("мотив"))
                    team['lives'] -= 1
            else:
                print(already_guessed)

            if guessed_weapon and guessed_location and guessed_motive:
                print(game_over.format(team_name))
                game_over_flag = True
                break

        elif choice == '6':  # Просмотреть подсказки
            print("\nНайденные подсказки:")
            for category, clue in team['found_clues']:
                print(f"- [{category.upper()}] {clue}")

        if team['lives'] <= 0:
            print(team_eliminated.format(team_name))
            del teams[team_name]
            if len(teams) == 1:
                winner = list(teams.keys())[0]
                print(game_over.format(winner))
                game_over_flag = True
                break

print(final_answers.format(correct_weapon, correct_location, correct_motive))
