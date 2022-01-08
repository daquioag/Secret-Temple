
import itertools
import random

MIN_NUM_OF_ROWS = 27  # the minimum number of rows and columns to play on a 25x25 grid is 27
MIN_NUM_OF_COLUMNS = 27


def make_map(rows: int, columns: int) -> list:
    """
    Generate a map.

    :param rows: an integer
    :param columns: an integer
    :precondition: rows must be a positive integer equal to or more than 4
    :precondition: columns must be a positive integer equal to or  more than 4
    :precondition: rows must be equal to columns
    :postcondition: creates a 2-D list in the form of: [['  |  ', '_____', '_____', '  |  '], ['  |  ', '|___|', '|___|', '  |  '], ['  |  ', '|___|', '|___|', '  |  '], ['  |  ', '_____', '_____', '  |  ']]
    :postcondition: the lists elements are lists whose elements are ASCII characters
    :return: list displaying a map

    >>> test_rows = 7  # you can only move around 5x5 of this map
    >>> test_columns = 7
    >>> make_map(test_rows, test_columns)
    [['  |  ', '_____', '_____', '_____', '_____', '_____', '  |  '], ['  |  ', '|___|', '|___|', '|___|', '|___|', '|___|', '  |  '], ['  |  ', '|___|', '|___|', '|___|', '|___|', '|___|', '  |  '], ['  |  ', '|___|', '|___|', '|___|', '|___|', '|___|', '  |  '], ['  |  ', '|___|', '|___|', '|___|', '|___|', '|___|', '  |  '], ['  |  ', '|___|', '|___|', '|___|', '|___|', '|___|', '  |  '], ['  |  ', '_____', '_____', '_____', '_____', '_____', '  |  ']]

    """
    prologue_grid = [["|___|" for _ in range(rows)] for _ in range(columns)]
    for ceiling in range(len(prologue_grid[0])):  # sets the map's ceiling and floor
        prologue_grid[0][ceiling] = "_____"
        prologue_grid[-1][ceiling] = "_____"
    for wall in range(len(prologue_grid[0])):  # sets the map's left and right walls
        prologue_grid[wall][0] = "  |  "
        prologue_grid[wall][-1] = "  |  "
    return prologue_grid


def title_page() -> None:
    print("\033[1;31;40m")
    print(r"""
                      )\         O_._._._A_._._._O           /(                   
                        \`--.___,'=================`.___,--'/
                         \`--._.__                 __._,--'/                        _________          _______        _______  _______  _______  _______  _______ _________      _________ _______  _______  _______  _        _______ 
                           \  ,. l`~~~~~~~~~~~~~~~'l ,.  /                          \__   __/|\     /|(  ____ \      (  ____ \(  ____ \(  ____ \(  ____ )(  ____ \\__   __/      \__   __/(  ____ \(       )(  ____ )( \      (  ____ \
               __            \||(_)!_!_!_.-._!_!_!(_)||/            __                 ) (   | )   ( || (    \/      | (    \/| (    \/| (    \/| (    )|| (    \/   ) (            ) (   | (    \/| () () || (    )|| (      | (    \/
               \\\`-.__        ||_|____!!_|;|_!!____|_||        __,-'//                | |   | (___) || (__          | (_____ | (__    | |      | (____)|| (__       | |            | |   | (__    | || || || (____)|| |      | (__    
                \\    `==---='-----------'='-----------`=---=='    //                  | |   |  ___  ||  __)         (_____  )|  __)   | |      |     __)|  __)      | |            | |   |  __)   | |(_)| ||  _____)| |      |  __)   
                | `--.                                         ,--' |                  | |   | (   ) || (                  ) || (      | |      | (\ (   | (         | |            | |   | (      | |   | || (      | |      | (      
                 \  ,.`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',.  /                   | |   | )   ( || (____/\      /\____) || (____/\| (____/\| ) \ \__| (____/\   | |            | |   | (____/\| )   ( || )      | (____/\| (____/\
                   \||  ____,-------._,-------._,-------.____  ||/                     )_(   |/     \|(_______/      \_______)(_______/(_______/|/   \__/(_______/   )_(            )_(   (_______/|/     \||/       (_______/(_______/
                    ||\|___!`======="!`======="!`======="!___|/||
                    || |---||--------||-| | |-!!--------||---| ||
          __O_____O_ll_lO_____O_____O|| |'|'| ||O_____O_____Ol_ll_O_____O__
          o H o o H o o H o o H o o |-----------| o o H o o H o o H o o H o
         ___H_____H_____H_____H____O =========== O____H_____H_____H_____H___
                                  /|=============|\
        ()______()______()______() '==== +-+ ====' ()______()______()______()
        ||{_}{_}||{_}{_}||{_}{_}/| ===== |_| ===== |\{_}{_}||{_}{_}||{_}{_}||
        ||      ||      ||     / |==== s(   )s ====| \     ||      ||      ||
        ======================()  =================  ()======================
        ----------------------/| ------------------- |\----------------------        
                             / |---------------------| \
        -'--'--'           ()  '---------------------'  ()
                           /| ------------------------- |\    --'--'--'
               --'--'     / |---------------------------| \    '--'
                        ()  |___________________________|  ()           '--'-
          --'-          /| _______________________________  |\
         --'           / |__________________________________| \                         By Al Daquioag
         """)
    print("""\033[1;34;40m                                         ,~~.
                                        (  6 )-_,    'quack, wake up, quack!'
                                   (\___ )=='-'
                                    \ .   ) )
                                     \ `-' /    
                                  ~'`~'`~'`~'`~
            """)
    print("\033[1;33;40m")
    str(input("Press [ENTER] to wake up"))
    print("\033[0m")


def create_name(
        character: dict) -> None:  # cant make doctests because create_name uses the input function. Unit tests done!
    """
    Update character's 'name' value.

    :param character: a dictionary
    :precondition: character is a dictionary whose keys are a string description of its integer or string values
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                    'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                     z is an integer more than or equal to 0, and s is a string
    :postcondition: prompt the user for an input and update that input as the 'name' value for character
    """
    print("You "
          "You wake up, dazed. You see a a giant temple in front of you."
          "\n???: Hey, Champ!. Get up, we got work to do!"
          "\nConfused, you look down. You see a duck."
          "\n???: Whats Your name, Champ?!"
          "\nIt talks. The Duck talks."
          "")

    name = str(input("My name is: "
                     "\n>>> "))
    character.update({"name": name})
    print(f"???: {character['name']}? Weird name."
          f"\n???: My name Is Howard, Howard The Duck")
    print("\033[1;33;40m")
    str(input("Press [ENTER] to continue."))
    print("\033[0m")


def context_info() -> None:
    """
    Prompt the user to press enter a print statement.

    """
    context = ("Howard: \"You my friend, are about to partake in the Secret Wars."
               "\nThere are Four Major Domains participating in the Wars: "
               "\nThe House of Iron"
               "\nThe Asgardian Republic"
               "\nThe Kingdom of Wakanda"
               "\nThe Strange Empire"
               "\nJoining one of the Four Major Domains will give unique powers and skills!"
               "\nYour mission is to stop the evil villain inside the Secret Temple\".")
    print(context)
    print("\033[1;33;40m")
    str(input("Press [ENTER] to continue."))
    print("\033[0m")


def choose_class(
        character: dict) -> str:  # cant make doctests because choose_class uses the input function. Unit tests done!
    """
    Returns a class chosen by the user.

    :param character: a dictionary
    :precondition: character is a dictionary whose keys are a string description of its integer or string values
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                    'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                    z is an integer more than or equal to 0 and s is a string
    :postcondition: the user chooses a class from a list of class titles
    :postcondition: invalid inputs will return the choose_class function
    :postcondition: character is unmodified
    :return: a string representing a class, else the choose_class function
    """
    print("Howard: \"Hey Champ, You wanna pick a class? We gotta get you suped up for the big battle in the "
          "Secret Temple\"\n")
    classes = {"Iron Heart Mark I": ("HP: 200", "Mana: 100", "ATK: 120", "DEF: 120"),
               "Frog of Thunder": ("HP: 220", "Mana: 100", "ATK: 140", "DEF: 80"),
               "Panther": ("HP: 160", "Mana: 80", "ATK: 160", "DEF: 140"),
               "Sorcerer in Training": ("HP: 140", "Mana: 120", "ATK: 200", "DEF: 80")}
    available_classes = {}
    for numbered_choice, choice in enumerate(classes.items(), 1):
        print(
            f"[{numbered_choice}]  Class: {choice[0]}    Stats: {' '.join(choice[1])}\n")  # prints a number, the class, and then the class stats
        available_classes.update({str(numbered_choice): str(
            choice[0])})  # appends the number and the class to an empty dictionary, available_classes

    class_choice = str(input("Please enter a number"
                             "\n>>> "))
    if class_choice in available_classes.keys():
        return available_classes[class_choice]  # returns the class title
    else:
        print("Howard:\"Hey Champ, NO SUCH CLASS EXISTS!! Pick again, and this time, READ THE QUESTION!\"")
        return choose_class(character)


def add_class_stats(character: dict, class_title: str) -> None:  # Unit tests done!
    """
    Update the character dictionary with stats in specific to different class_title.

    :param character: a dictionary
    :param class_title: a string
    :precondition: character is a dictionary whose keys are a string description of its integer or string values
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                    'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                    z is an integer more than or equal to 0 and s is a string
    :precondition: class_title must be one of the following strings: "Iron Heart Mark I", "Frog of Thunder", "Panther",
                    "Sorcerer in Training"
    :postcondition: the character dictionary is modified with certain statistics according to the class_title

    >>> test_class = 'Frog of Thunder'
    >>> test_character = {}
    >>> add_class_stats(test_character, test_class)
    >>> test_character == {'Current HP': 220, 'Current Mana': 100, 'ATK': 140, 'DEF': 80, 'title': 'Frog of Thunder', 'domain': 'Asgardian Republic', 'HP cap': 220, 'Mana cap': 100}
    True
    """

    if class_title == "Iron Heart Mark I":  # each class has different stats
        stat_numbers = [200, 100, 120, 120, "Iron Heart Mark I", "House of Iron", 200, 100]
        stat_names = ["Current HP", "Current Mana", "ATK", "DEF", "title", "domain", "HP cap", "Mana cap"]
        stats = dict(zip(stat_names, stat_numbers))
        character.update(stats)

    elif class_title == "Frog of Thunder":
        stat_numbers = [220, 100, 140, 80, "Frog of Thunder", "Asgardian Republic", 220, 100]
        stat_names = ["Current HP", "Current Mana", "ATK", "DEF", "title", "domain", "HP cap", "Mana cap"]
        stats = dict(zip(stat_names, stat_numbers))
        character.update(stats)

    elif class_title == "Panther":
        stat_numbers = [160, 80, 160, 140, "Panther", "Kingdom of Wakanda", 160, 80]
        stat_names = ["Current HP", "Current Mana", "ATK", "DEF", "title", "domain", "HP cap", "Mana cap"]
        stats = dict(zip(stat_names, stat_numbers))
        character.update(stats)

    elif class_title == "Sorcerer in Training":
        stat_numbers = [140, 120, 200, 80, "Sorcerer in Training", "Temple of Vishanti", 140, 120]
        stat_names = ["Current HP", "Current Mana", "ATK", "DEF", "title", "domain", "HP cap", "Mana cap"]
        stats = dict(zip(stat_names, stat_numbers))
        character.update(stats)


def start_mission() -> None:
    """
    Prompt the user to press enter after a print statement.

    """
    print(r"""
Howard: "Alight, I ain't no Scaredy Duck! Lets go beat up the bad guys!"
Howard jumps on top of your head.
You step inside the Temple....
And you begin....
    """)
    print("\033[1;33;40m")
    str(input("Press [ENTER] to begin."))
    print("\033[0m")


def list_of_titles(character: dict) -> list:  # Picks a list of class titles based on the character's 'Domain'
    """
    Returns a list of strings describing class titles.

    :param character: a dictionary
    :precondition: character is a dictionary whose keys are a string description of its integer or string values
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                    'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                    z is an integer more than or equal to 0 and s is a string
    :postcondition: evaluates the 'domain' key in character and returns a list based on its value
    :return: a list whose elements are strings describing class titles

    >>> test_character_throg = {'Current HP': 220, 'Current Mana': 100, 'ATK': 140, 'DEF': 80, 'title': 'Frog of Thunder', 'domain': 'Asgardian Republic', 'HP cap': 220, 'Mana cap': 100}
    >>> list_of_titles(test_character_throg)
    ['Frog of Thunder', 'Thor Odinson', 'God of Thunder', 'Unworthy Thor', 'God King Thor']

    >>> test_character_sorcerer = {'Current HP': 220, 'Current Mana': 100, 'ATK': 140, 'DEF': 80, 'title': 'Frog of Thunder', 'domain': 'Temple of Vishanti', 'HP cap': 220, 'Mana cap': 100}
    >>> list_of_titles(test_character_sorcerer)
    ['Sorcerer in Training', 'Master of the Mystic Arts', 'Sorcerer Supreme', 'Disciple of Dormamu', 'Dr. StrangeFate']
"""

    domain = character['domain']
    house_of_iron = ["Iron Heart Mark I", "Iron Heart Mark III", "Iron Heart MK 40", "Iron Heart Mark XXII: Thorbuster",
                     "Iron Heart Mark XLIV: Thanos-Buster"]
    asgardian_republic = ["Frog of Thunder", "Thor Odinson", "God of Thunder", "Unworthy Thor",
                          "God King Thor"]
    kingdom_of_wakanda = ["Panther", "Coal Tiger", "Ghost Panther", "The Black Panther", "King of Necropolis"]
    temple_of_vishanti = ["Sorcerer in Training", "Master of the Mystic Arts", "Sorcerer Supreme",
                          "Disciple of Dormamu", "Dr. StrangeFate"]

    if domain == "House of Iron" or domain == "Asgardian Republic":
        titles = house_of_iron if domain == "House of Iron" else asgardian_republic
    else:
        titles = kingdom_of_wakanda if domain == "Kingdom of Wakanda" else temple_of_vishanti

    return titles  # done unit tests!


def set_characters(character: dict, board: dict, map_of_board: list) -> None:  # done unit tests!
    """
    Place ASCII characters representing the user and the final boss on the board.

    :param character: a dictionary
    :param board: a dictionary
    :param map_of_board: a list
    :precondition: character is a dictionary whose keys are a string description of its integer or string values
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                    'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                    z is an integer more than or equal to 0 and s is a string
    :precondition: board must be a dictionary in the form of: {(0, 0): ‘Empty room’, (0, 1): ‘Empty room’, (1, 0): ‘
                    Empty room’, (1, 1): ‘Empty room’}
    :precondition: board's keys are tuples that contain a set of coordinates and the values are string descriptions
    :precondition: map_of_board must be a 2-D list in the form of: [['  |  ', '_____', '_____', '  |  '],
                ['  |  ', '|___|', '|___|', '  |  '], ['  |  ', '|___|', '|___|', '  |  '],
                ['  |  ', '_____', '_____', '  |  ']]
    :precondition: map_of_board's elements are lists whose elements are ASCII characters
    :postcondition: calculate the board's boundaries by evaluating the highest integer in board's key's tuples
    :postcondition: set the ASCII characters representing the user at the top left corner of mop_of_board
    :postcondition: set the ASCII characters representing the final boss at the bottom right corner of the map_of_board
    :postcondition: set the ASCII characters |_*_| and |_!_| on map_of_board by evaluating the coordinates of the rooms
    :postcondition: board must not be modified in anyway
    :postcondition: character must not be modified in anyway

    """
    x_axis_lower_boundary = 0  # changes
    y_axis_right_boundary = 0  # changes
    for coordinates in board.keys():
        if coordinates[0] > x_axis_lower_boundary:
            x_axis_lower_boundary = coordinates[0]
        if coordinates[1] > y_axis_right_boundary:
            y_axis_right_boundary = coordinates[1]
    for coordinates, rooms in board.items():
        if coordinates[0] != 0 and coordinates[1] != 0 and coordinates[0] != x_axis_lower_boundary and coordinates[1] \
                != y_axis_right_boundary:
            if rooms == "a wrecked room full of shattered iron man suits.\nHoward: \'Where could have Tony gone?!\'" \
                    or rooms == "an empty room with used arrows and a broken quiver.\nHoward: \'We need to find Clint!\'":
                map_of_board[coordinates[0]][coordinates[1]] = "|_\033[1;36;40m!\033[1;37;40m_|"
            elif rooms == "a room full of bloody webs.\nHoward: \'Peter's in trouble! We gotta help him!\'" or \
                    rooms == "a dark room. You see a pair of batons on the ground.\nHoward: \'Natasha's in danger!!\'":
                map_of_board[coordinates[0]][coordinates[1]] = "|_\033[1;33;40m*\033[1;37;40m_|"
            else:
                map_of_board[coordinates[0]][coordinates[1]] = "|___|"

    map_of_board[character["X-coordinate"]][character["Y-coordinate"]] = "|YOU|"
    map_of_board[x_axis_lower_boundary - 1][x_axis_lower_boundary - 1] = " BOSS"


def generate_random_room() -> str:  # done unit tests!
    """
    Generate a string description based on a random number.

    :postcondition: create a short string description based on a random number
    :return: a short string description of a room
    """

    random_room = random.randint(1, 25)
    if random_room in range(0, 4):
        return "a wrecked room full of shattered iron man suits.\nHoward: \'Where could have Tony gone?!\'"
    elif random_room in range(4, 8):
        return "an empty room with used arrows and a broken quiver.\nHoward: \'We need to find Clint!\'"
    elif random_room in range(8, 12):
        return "a demolished room.\nHoward: \'Bruce was definitely here.\'"
    elif random_room in range(12, 16):
        return "a room full of bloody webs.\nHoward: \'Peter's in trouble! We gotta help him!\'"
    elif random_room in range(16, 20):
        return "a torn-apart room. You see a severed hand. It waves. You wave back. " \
               "\nHoward: \'Wade's probably okay...probably\'"
    elif random_room in range(20, 23):
        return "a dark room. You see a pair of batons on the ground.\nHoward: \'Natasha's in danger!!\'"
    else:
        return "a room with enemy bodies in pieces. Mystic energy fills the air. " \
               "\nHoward: \"Wanda was just here. She's close by.\""


def make_board(rows: int, columns: int) -> dict:  # done unit tests!
    """
    Generate a board.

    :param rows: an integer
    :param columns: an integer
    :precondition: rows must be a positive integer equal to or more than 4
    :precondition: columns must be a positive integer equal to or  more than 4
    :precondition: rows must be equal to columns
    :postcondition: creates a dictionary in the form of: {(0, 0): ‘Empty room’, (0, 1): ‘Empty room’,
                        (1, 0): ‘Empty room’, (1, 1): ‘Empty room’}
    :postcondition: the dictionary's keys are tuples that contain a set of coordinates and each value is a string
                    description
    :return: dictionary describing a board
    """
    board = {(row, column): generate_random_room() for row in range(rows) for column in range(columns)}
    board.update({(rows - 2, columns - 2): "The Final Destination"})  # sets room where the boss is as final destination
    return board


def get_user_choice() -> str:  # cant make doctests because it asks for an input. # done unit tests!
    """
    Return the user's direction of choice.

    :postcondition: enumerate a dictionary whose keys are numbers, and values are string descriptions of 4
                    different directions
    :postcondition: validate if the integer input of the user matches a string direction
    :return: string describing a direction or get_user_choice function
    """
    directions = ('up', 'down', 'left', 'right', "quit")  # The choices that the user can pick
    available_choices = {}  # initializes a dictionary
    for number, choice in enumerate(directions, 1):
        if number == 5:  # 'quit'  needs to be paired with "q" so this line removes '5' and replaces it with 'q'
            number = "q"
        print(number, choice)
        available_choices.update({str(number): choice})  # updates the values to the empty dictionary

    numbered_choice = str(input("Which direction would you like to go?"
                                "\nPlease enter a number!"
                                "\n>>> ")).lower()
    if numbered_choice in available_choices.keys():
        print(f"You choose to move through a portal in the {available_choices[numbered_choice]}ward direction")
        return available_choices[numbered_choice]
    else:
        print("That is an invalid number!"
              "\nPlease pick again\n")
        return get_user_choice()


def make_character() -> dict:  # done unit tests!
    """
    Generate a dictionary describing a character.

    :postcondition: create a dictionary whose keys are a string description of integer or string values
    :postcondition: the dictionary must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                    'EXP needed': n, 'title': s, 'domain': s}
                    where z is an integer more than or equal to 0, n is an integer more than 0, and s is a string
    :return: dictionary describing a character's coordinates, level, EXP, title and domain

    >>> make_character()
    {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 1, 'EXP': 0, 'EXP needed': 30, 'title': '', 'domain': ''}
    """
    stat_numbers = [1, 1, 1, 0, 30, "", ""]
    stat_names = ["X-coordinate", "Y-coordinate", "Level", "EXP",
                  "EXP needed", "title", "domain"]
    return dict(zip(stat_names, stat_numbers))  # returns a dictionary


def validate_move(board: dict, character: dict, direction: str) -> bool:  # done unit tests!
    """
    Validate if the user's direction of choice will move the character within the board boundaries.

    :param board: a dictionary
    :param character: a dictionary
    :param direction: a string
    :precondition: board must be a dictionary in the form of: {(0, 0): ‘Empty room’, (0, 1): ‘Empty room’, (1, 0): ‘
                    Empty room’, (1, 1): ‘Empty room’}
    :precondition: board's keys are tuples that contain a set of coordinates and the values are string descriptions
    :precondition: character is a dictionary in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                    'EXP needed': n, 'title': s, 'domain': s} where z is an integer more than or equal to 0,
                    n is an integer more than 0, and s is a string
    :precondition: character's keys are a string description of the integer or string values
    :precondition: direction must be a string of either "up", "down", "left", or "right"
    :postcondition: set the board boundaries by evaluating the highest integer in board's key's tuples
    :postcondition: evaluates if the direction will move the character past the board boundaries
    :postcondition: the values of character's "X-coordinate" and "Y-coordinate" are unmodified
    :return: True if direction is valid, else False

    >>> character_starting_position = make_character()
    >>> hypothetical_direction = 'down'
    >>> hypothetical_board = {(0, 0): 'an empty room', (0, 1): 'a doll room', (1, 0): 'a doll room',\
                                (1, 1): 'The Final Destination'}
    >>> validate_move(hypothetical_board, character_starting_position, hypothetical_direction)
    False
    """
    x_axis_lower_boundary = 0  # changes and becomes the lower boundary
    x_axis_upper_boundary = 0  # stays 0 becomes the upper boundary
    y_axis_right_boundary = 0  # changes, becomes the rightward boundary
    y_axis_left_boundary = 0  # stays 0, becomes the leftward boundary
    for coordinates in board.keys():
        if coordinates[0] > x_axis_lower_boundary:
            x_axis_lower_boundary = coordinates[0]
        if coordinates[1] > y_axis_right_boundary:
            y_axis_right_boundary = coordinates[1]

    if direction == 'up' and character['X-coordinate'] > x_axis_upper_boundary + 1:
        return True
    elif direction == 'down' and character['X-coordinate'] < x_axis_lower_boundary - 1:
        return True
    elif direction == 'left' and character['Y-coordinate'] > y_axis_left_boundary + 1:
        return True
    elif direction == 'right' and character['Y-coordinate'] < y_axis_right_boundary - 1:
        return True
    else:
        return False


def level_system(character: dict, enemy: dict) -> None:  # cant make doctests because no return statement
    """
    Increase character's 'EXP' value based on the enemy.

    :param character: a dictionary
    :param enemy: a dictionary
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                    'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                    z is an integer more than or equal to 0 and s is a string
    :precondition: character's  keys are a string description of its value pair
    :precondition: enemy is a dictionary whose keys are a string description of the values
    :precondition: enemy must be in the form of {"Name": s, "Level": n, "HP": n, "ATK": n,"EXP given": n}
                        where s in a string and n is an integer more than 0
    :postcondition: add 'EXP given' value from enemy to the 'EXP' value in character
    :postcondition: call the gained_level() function when the 'EXP' value is more or equal to the 'EXP needed' value

    """
    print("\033[1;33;40m")  # adds colors
    print(f"you gained {enemy['EXP given']} EXP!\n ")
    character["EXP"] += enemy["EXP given"]  # character's EXP increases by  the enemy's EXP give

    if character["EXP"] >= character["EXP needed"]:  # leveling up grants a new title, increased stats, and healing
        gained_level(character)

    print(f"Your Current Level is {character['Level']}...."
          f"You have {character['EXP']} /{character['EXP needed']} EXP needed for the next level")
    print("\033[0m")  # unit tests done!


def gained_level(character: dict) -> None:  # unit tests done!
    """
    Increase certain statistics in character.

    :param character: a dictionary
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                    'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                    z is an integer more than or equal to 0 and s is a string
    :precondition: character's  keys are a string description of its value pair
    :postcondition: increase character's 'Level' value by 1
    :postcondition: increase specific statistics in character based on the 'Level' value
    :postcondition: set 'Current HP' and 'Current Mana" values equal to 'HP cap' and 'Mana cap'
    """
    character["Level"] += 1
    for stat_names, stat_numbers in character.items():
        if stat_names in ("HP cap", "Mana cap", "ATK", "DEF"):  # certain stats increase after leveling up
            character[stat_names] += character["Level"] * 50
    character["EXP"] -= character["EXP needed"]  # the left over exp goes towards the next level.
    character["EXP needed"] *= 2  # doubles the EXP needed to get to the next level
    character["Current HP"] = character["HP cap"]  # HP and Mana get fully restored after leveling up
    character["Current Mana"] = character["Mana cap"]

    print("You gained a level!")
    print("You gained a new title!")
    print("HP and Mana restored!")


def upgrade_title(character: dict, class_titles: list) -> None:  # unit tests done!
    """
    Update character's 'title' value.

    :param character:
    :param class_titles:
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                    'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                    z is an integer more than or equal to 0 and s is a string
    :precondition: character's  keys are a string description of its value pair
    :precondition: class_titles is a list whose elements are strings describing class titles
    :postcondition: changes character's 'title' value based on character's 'Level' value
    """
    if character["Level"] < 5:
        character["title"] = class_titles[character["Level"] - 1]  # The class titles change based on level
    else:  # the title value is level value integer corresponding to the index of the class_titles list
        character["title"] = class_titles[-1]  # after level 5, the title stays the same


def display_map(character: dict, map_of_board: list) -> None:  # unit tests done!
    """
    Print map_of_board.

    :param character: a dictionary
    :param map_of_board: a list
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                    'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                    z is an integer more than or equal to 0 and s is a string
    :precondition: character's  keys are a string description of its value pair
    :precondition: map_of_board must be a 2-D list in the form of: [['  |  ', '_____', '_____', '  |  '], ['  |  ', '|___|', '|___|', '  |  '], ['  |  ', '|___|', '|___|', '  |  '], ['  |  ', '_____', '_____', '  |  ']]
    :precondition: map_of_board elements are lists whose elements are ASCII characters
    :postcondition: the elements of map_of_board are unmodified
    :postcondition: the key-value pairs of character are unmodified
    :postcondition: prints on map_of_board
    :postcondition: prints a statement notifying the user that the boss is near

    """
    coordinates = (character["X-coordinate"], character["Y-coordinate"])
    close_to_boss = range(len(map_of_board) - 5, len(map_of_board))
    print("\033[1;37;40m")
    print(('\n'.join(map(''.join, map_of_board))))  # prints the 2d list of map_of_board
    if coordinates[0] in close_to_boss and coordinates[1] in close_to_boss:  # this message prints if the boss is close
        print(f"Howard: \'My ducky senses are tingly... Something strong is near."
              f"L-Lets proceed with caution.\'")


def describe_current_location(board: dict, character: dict) -> None:  # unit tests done!
    """
    Print the string description of the character's current position on the map and cooridnates.

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board must be a dictionary in the form of: {(0, 0): ‘Empty room’, (0, 1): ‘Empty room’, (1, 0):
                    ‘Empty room’, (1, 1): ‘Empty room’}
    :precondition: board's keys are tuples that contain coordinates and the values are string descriptions
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                    'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                    z is an integer more than or equal to 0 and s is a string
    :precondition: character's keys are a string description of its value pair
    :postcondition: prints the value of board's key that matches the values of character's 'X-coordinate' and
                'Y-coordinate'
    :postcondition: the values of board are unmodified

    >>> test_character = {"name": "Test Character", 'title': "s", 'domain': "s", 'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
    >>> test_board = {(0, 0): 'an empty room', (0, 1): 'an empty room', (1, 0): 'an empty room',\
                        (1, 1): 'The Final Destination'}
    >>> describe_current_location(test_board, test_character)
    \033[1;31;40m
    Test Character, s, is in an empty room \033[1;37;40m[coordinates: (0, 1)]
    \033[1;31;0m

    """
    coordinates = (character["X-coordinate"], character["Y-coordinate"])
    current_room = board[coordinates]
    current_coordinates = str(coordinates)
    print("\033[1;31;40m")
    print(f"{character['name']}, {character['title']}, is in {current_room} "
          f"\033[1;37;40m[coordinates: {current_coordinates}]")
    print("\033[1;31;0m")


def move_character(character: dict, direction: str) -> None:  # unit tests done
    """
    Move character based on the direction.

    :param character: a dictionary
    :param direction: a string
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                    'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                    z is an integer more than or equal to 0 and s is a string
    :precondition: character's keys are a string description of its value pair
    :precondition: direction must be a string of either "up", "down", "left", or "right"
    :postcondition: add or subtract 1 to the values of keys, 'Y-coordinate' or 'X-coordinate', based on direction

    >>> default_character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
    >>> direction_down = 'down'
    >>> move_character(default_character, direction_down)
    >>> default_character == {'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 5}
    True
    """

    if direction == 'up':
        character['X-coordinate'] -= 1
    elif direction == "down":
        character['X-coordinate'] += 1
    elif direction == 'left':
        character['Y-coordinate'] -= 1
    elif direction == "right":
        character['Y-coordinate'] += 1


def generate_foe(character: dict) -> dict:  # cant make a doctest because it uses a function from the random module
    """
    Generate a dictionary describing a foe.

    :param character: a dictionary
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                    'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                    z is an integer more than or equal to 0 and s is a string
    :precondition: character's keys are a string description of the integer or string values
    :postcondition: create a dictionary whose keys are a string description of the values
    :postcondition: the dictionary must be in the form of {"Name": s, "Level": n, "HP": n, "ATK": n,"EXP given": n}
                        where s in a string and n is an integer more than 0
    :return: dictionary describing a foe
    """
    level = character["Level"]
    random_foe = random.randint(1, 12)  # each enemy has a 25% chance of being chosen
    if random_foe in range(1, 4):
        foe = {"Name": "Hydra Agent"}
    elif random_foe in range(4, 7):
        foe = {"Name": "Dark Elf"}
    elif random_foe in range(7, 10):
        foe = {"Name": "Frost Giant"}
    else:
        foe = {"Name": "Kree"}
    foe.update({'class': 'enemy', "Level": level + 1, "HP": 80 + (level + 1) * 10, "ATK": 100 + (level + 1) * 10,
                "EXP given": 10 + (level + 1) * 5})
    return foe  # Unit tests done!


def check_for_foes():  # cant make a doctest because it uses a function from the random module. #unit tests done!
    """
    Provide a 20% chance that an enemy will attack you.

    :postcondition: generate a random number between 1 - 10 inclusive
    :postcondition: call the fight_or_run function if the random number is 1 or 2
    :return: fight_or_run function
    """
    chance_of_foe = random.randint(1, 10)
    if chance_of_foe in range(1, 3):  # 20% of encountering a foe
        print("Howard: 'Quack! Look out, an enemy is attacking!")
        return fight_or_run()  # cant implement function annotation because it returns a function
    else:
        print("Howard: 'quack! I dont see any enemies here...")


def fight_or_run() -> bool:  # cant make doctests because the function uses an input function. #done unit test!
    """
    Prompt the user to fight or run from the enemy.

    :postcondition: ask the user to input 'y' or 'n' if the user wants to fight an enemy
    :postcondition: return the fight_or_run function if input is not 'y' or 'n'
    :return: True if input is 'y', False if input is 'n', else fight_or_run function if input isn't 'y' or 'n'
    """
    fight = str(input("Would you like to fight? [y/n]"
                      "\n>>> "))
    if fight.lower() == "y":
        print("Howard: HECK YEAH!! WE GONNA MESS YOU UP!")
        return True
    elif fight.lower() == "n":
        print("You scream \"Bawk Bawk!\" as you run away.")
        return False
    else:
        print("Howard: Are you daft?! That is not a valid response!")
        return fight_or_run()


def create_skills() -> dict:  # creates skills
    """
    Return a dictionary describing skills available in combat.

    :postcondition: returns a dictionary in the form of: {"1": 'Punch', "2": 'Kick', "9": "RUN AWAY!"}
                    whose keys are string numbers to string values describing a move
    :return: a dictionary describing the numbered choices of skills available in combat.

    >>> create_skills()
    {'1': 'Punch', '2': 'Kick', '9': 'RUN AWAY!'}
    """
    return {"1": 'Punch', "2": 'Kick', "9": "RUN AWAY!"}  # creates default skills for all classes


def upgrade_skills(skills: dict, character: dict) -> None:  # unit tests done
    """
    Update skills depending on character's 'domain' and 'Level' value.

    :param skills: a dictionary
    :param character: a dictionary
    :precondition: skills must dictionary in the form of: {"1": 'Punch', "2": 'Kick', "9": "RUN AWAY!"}
    :precondition: skills' keys are string numbers to string values describing a move
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                    'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                    z is an integer more than or equal to 0 and s is a string
    :precondition: character's keys are a string description of the integer or string values
    :postcondition: evaluate the "domain" and "Level" values of character and update skills based on those values

    >>> test_character =  {'X-coordinate': 4, 'Y-coordinate': 4, 'Level': 2, 'EXP': 0, 'EXP needed': 30, 'title': "House of Iron", 'domain': "House of Iron"}
    >>> test_skills = {"1": 'Punch', "2": 'Kick', "9": "RUN AWAY!"}
    >>> upgrade_skills(test_skills, test_character)
    >>> test_skills == {"1": 'Punch', "2": 'Omega Beam', "3": "Micro Rockets", "9": "RUN AWAY!"}
    True
    """
    level = character["Level"]
    if "9" in skills.keys():
        skills.pop("9")  # this removes "Run Away! in the skills list
    if character["domain"] == "House of Iron" and level > 1:  # need to be more than level 1 to get new skills
        if level <= 3:  # gets more abilities as you level up
            skills.update({"3": "Micro Rockets", "2": 'Omega Beam'}) if level == 2 \
                else skills.update(
                {"1": 'Scorched Earth', "4": "Ultimate Attack: Unibeam Blast"})  # you get ultimate ability at level 3

    elif character["domain"] == "Asgardian Republic" and level > 1:
        if level <= 3:
            skills.update({"2": "Throw Mjolnir", "3": 'Crashing Thunder'}) if level == 2 else skills.update(
                {"1": 'Stormbreaker and Mjolnir Combo', "4": "Ultimate Ability: Legacy of Odinson"})

    elif character["domain"] == "Kingdom of Wakanda" and level > 1:
        if level <= 3:
            skills.update({"3": "Vibranium Burst", "2": 'King\'s Mercy'}) if level == 2 else skills.update(
                {"1": 'Kimoyo Missile', "4": "Ultimate Ability: Panther Goddess Bast"})

    elif character["domain"] == "Temple of Vishanti" and level > 1:
        if level <= 3:
            skills.update(
                {"2": 'Sacred Sword Of Vishanti', "3": "Crimson Bands Of Cyttorak"}) if level == 2 else skills.update(
                {"1": 'Icy Tendrils Of Ikthalon', "4": "Ultimate Ability: Use Time Stone"})

    skills.update({"9": "RUN AWAY!"})  # adds the skills at the end, so that the menu always shows this option last


def enemy_alive(enemy: dict) -> bool:  # unit tests done
    """
    Check if enemy is alive.

    :param enemy: a dictionary
    :precondition: enemy is a dictionary whose keys are string descriptions of the values
    :precondition: enemy must be in the form of {"Name": s, "Level": n, "HP": n, "ATK": n,"EXP given": n}
                        where s in a string and n is an integer more than 0
    :postcondition: evaluates enemy's 'HP' value
    :returns: True if the character's "Current HP" value is more than 0, else False

    >>> foe_test = {"Name": "Kree", 'class': 'enemy', "Level": 2, "HP": 120, "ATK": 120, "EXP given": 15}
    >>> enemy_alive(foe_test)
    True
    """
    return enemy["HP"] > 0


def describe_battle(character: dict,
                    enemy: dict) -> None:  # shows the current stats of the hero and enemy  # unit tests done!
    """
    print a description of the current stats of character and enemy.

    :param character: a dictionary
    :param enemy: a dictionary
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                z is an integer more than or equal to 0 and s is a string
    :precondition: character's keys are a string description of the integer or string values
    :precondition: enemy is a dictionary whose keys are string descriptions of the values
    :precondition: enemy must be in the form of {"Name": s, "Level": n, "HP": n, "ATK": n,"EXP given": n}
                        where s in a string and n is an integer more than 0
    :postcondition: print the enemy values of 'Name', 'HP', and 'Level'
    :postcondition: print the character values of 'name', 'Current HP', 'HP cap' 'Level', 'Current Mana' and 'Mana cap'

    >>> test_character =  { 'HP cap': 160, 'Mana cap': 80, "name" : "test character", 'Current HP': 160, 'Current Mana': 80, 'ATK': 160, 'DEF': 140, 'X-coordinate': 4, 'Y-coordinate': 4, 'Level': 2, 'EXP': 0, 'EXP needed': 30, 'title': "House of Iron", 'domain': "House of Iron"}
    >>> test_enemy = {"Name": "God Emperor Doom", 'class': 'boss', "Level": 8, "HP": 800, "ATK": 500, "EXP given": 50}
    >>> describe_battle(test_character, test_enemy)
    ------------------------------------------------------------
    God Emperor Doom                        test character
    Level: 8                                Level: 2
    Foe HP: 800                             HP: 160/160  MANA: 80/80
    ------------------------------------------------------------
    """
    enemy_level = enemy['Level']
    enemy_hp = enemy['HP']
    print(f"{'-' * 60}\n"  # prints  ------------------------------------------------------------
          f"{enemy['Name']}{' ' * (40 - len(enemy['Name']))}{character['name']}"  # the code  {' ' * (40 - len(enemy['Name']))} makes the white spacing consistent
          f"\nLevel: {enemy_level}{' ' * (40 - len(f'Level: {enemy_level}'))}Level: {character['Level']}"
          f"\nFoe HP: {enemy_hp}{' ' * (40 - len(f'Foe HP: {enemy_hp}'))}HP: {int(round(character['Current HP']))}/{character['HP cap']}  "
          f"MANA: {character['Current Mana']}/{character['Mana cap']}\n"
          f"{'-' * 60}")  # prints  ------------------------------------------------------------


def choose_skill(skills: dict, enemy: dict) -> str:  # cant make doctests due to the input function. Unit tests done!
    """
    Return the user's skill of choice.

    :param skills: a dictionary
    :param enemy: a dictionary
    :precondition: skills must dictionary in the form of: {"1": 'Punch', "2": 'Kick', "9": "RUN AWAY!"}
    :precondition: skills' keys are string numbers to string values describing a move
    :precondition: enemy is a dictionary whose keys are string descriptions of the values
    :precondition: enemy must be in the form of {"Name": s, "Level": n, "HP": n, "ATK": n,"EXP given": n}
                        where s in a string and n is an integer more than 0
    :postcondition: prompts the user to choose from a list of skills
    :postcondition: calls back the choose_skill function if the user inputs are invalid
    :postcondition: prevents the user from choosing "RUN AWAY!" if the enemy is the boss
    :return: string number or "RUNAWAY!" if you try and run from an enemy,, else choose_skill function
    """
    print("What skill do you use?")
    numbers = itertools.cycle(skills.values())  # prints a list of available skills
    names = itertools.cycle(skills.keys())
    for moves in range(len(skills)):
        numbered_choice = next(names)
        fight_move = next(numbers)
        print(f"[{numbered_choice}]: {fight_move}")

    numbered_choice = str(input(
        "\nPlease enter a number!"
        "\n>>> "))

    if numbered_choice in skills.keys() and skills[numbered_choice] != "RUN AWAY!":
        print(f"You choose to {skills[numbered_choice]}....")
        return numbered_choice

    elif numbered_choice in skills.keys() and skills[numbered_choice] == "RUN AWAY!":
        print("You try and run away!")
        if enemy['class'] == 'boss':
            print("You cant escape a boss fight!")  # you cant run from a boss fight, and removes the option if you try.
            skills.pop("9")
            return choose_skill(skills, enemy)  # returns the function if you run from a boss
        else:
            return skills[numbered_choice]  # returns "RUN AWAY"! if you run from a regular enemy

    else:
        print("That is an invalid number!"
              "\nPlease pick again\n")
        return choose_skill(skills, enemy)  # returns the function with invalid inputs


def validate_skill(character: dict, skill: str) -> bool:
    """
    Validate the user's skill of choice.

    :param character: a dictionary
    :param skill: a str
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                z is an integer more than or equal to 0 and s is a string
    :precondition: character's keys are a string description of the integer or string values
    :precondition: skills must dictionary in the form of: {"1": 'Punch', "2": 'Kick', "9": "RUN AWAY!"}
    :precondition: skills' keys are string numbers to string values describing a move
    :postcondition: calculate the mana cost of the skill by evaluating character's 'Level' and skill of choice
    :postcondition: evaluate if the character "Current Mana" is more than the mana cost of the skill
    :return: True if skill is valid, else False

    >>> test_skill = "4"
    >>> test_character = {'Current HP': 160, 'Current Mana': 80, 'ATK': 160, 'DEF': 140, 'title': 'Panther', 'domain': 'Kingdom of Wakanda', 'HP cap': 160, 'Mana cap': 80, "Level" : 5}
    >>> validate_skill(test_character, test_skill)
    True
    """
    if character["Current Mana"] >= 15 * character["Level"]:  # all skills can be cast
        return True
    elif character["Current Mana"] <= 15 * character["Level"] and skill == "1" or skill == "2":
        return True  # some skills can be cast with no mana
    elif skill == "3" and character["Current Mana"] >= 10 * character["Level"]:
        return True
    elif skill == "4" and character["Current Mana"] >= 15 * character["Level"]:
        return True
    else:
        print("Nuh-uh-uh! You ain't go no more mana!"
              "\nTry another ability!")
        return False


def basic_attack(character: dict, enemy: dict, skill: str,
                 skills: dict) -> None:  # cant make doctests because the function uses the random module
    """
    Calculates the damage a basic attack does to an enemy.

    :param character: a dictionary
    :param skills: a dictionary
    :param skill: a string
    :param enemy: a dictionary
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                z is an integer more than or equal to 0 and s is a string
    :precondition: character's keys are a string description of the integer or string values
    :precondition: skills must dictionary in the form of: {"1": 'Punch', "2": 'Kick', "9": "RUN AWAY!"}
    :precondition: skills' keys are string numbers to string values describing a move
    :precondition: skill is a string number representing the user's choice of skill
    :precondition: enemy is a dictionary whose keys are string descriptions of the values
    :precondition: enemy must be in the form of {"Name": s, "Level": n, "HP": n, "ATK": n,"EXP given": n}
                        where s in a string and n is an integer more than 0
    :postcondition: calculate 'damage_dealt' by evaluating character's 'ATK' and 'Level' values and a random integer
    :postcondition: subtracts  enemy's 'HP' value by 'damage_dealt
    :postcondition: print a statement describing the damage dealt and the mana cost

    """
    mana_cost = 0
    damage_amplifier = random.randint(1, character["Level"] + 3)
    damage_dealt = character["ATK"] / (3 * damage_amplifier)  # damage calculator
    enemy['HP'] -= int(round(damage_dealt))
    if damage_amplifier in range(3, 6):
        print("Howard: Its not very effective....")
    else:
        print("Howard: Its super effective!")
    print(f"\n{skills[skill]} dealt {int(round(damage_dealt))} damage to {enemy['Name']}"
          f"\nYou lost {mana_cost} Mana")


def strong_attack(character: dict, enemy: dict, skill: str,
                  skills: dict) -> None:  # cant make doctests because the function uses the random module. # unit tests done
    """
    Calculates the damage a strong attack does to an enemy.

    :param character: a dictionary
    :param skills: a dictionary
    :param skill: a string
    :param enemy: a dictionary
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                z is an integer more than or equal to 0 and s is a string
    :precondition: character's keys are a string description of the integer or string values
    :precondition: skills must dictionary in the form of: {"1": 'Punch', "2": 'Kick', "9": "RUN AWAY!"}
    :precondition: skills' keys are string numbers to string values describing a move
    :precondition: skill is a string number representing the user's choice of skill
    :precondition: enemy is a dictionary whose keys are string descriptions of the values
    :precondition: enemy must be in the form of {"Name": s, "Level": n, "HP": n, "ATK": n,"EXP given": n}
                        where s in a string and n is an integer more than 0
    :postcondition: calculate 'damage_dealt' by evaluating character's 'ATK' and 'Level' values and a random integer
    :postcondition: subtracts  enemy's 'HP' value by 'damage_dealt
    :postcondition: print a statement describing the damage dealt and the mana cost
    :postcondition: character's 'Level' value has to be more than or equal to 2

    """
    mana_cost = 10 * character["Level"]
    character["Current Mana"] -= mana_cost
    damage_amplifier = random.randint(1, character["Level"] + 2)
    damage_dealt = character["ATK"] / (2 * damage_amplifier)  # damage calculator
    enemy['HP'] -= int(round(damage_dealt))
    if damage_amplifier in range(3, 6):
        print("Howard: Do you know how to aim?! Barely hit em....")
    else:
        print("Howard: Direct HIT!! Its super effective!")

    print(
        f"\n{skills[skill]} dealt {int(round(damage_dealt))} damage to {enemy['Name']}"
        f"\nYou lost {mana_cost} Mana")


def ultimate_ability(character: dict, enemy: dict, skill: str,
                     skills: dict) -> None:  # cant make doctests because the function uses the random module
    """
    Calculates the damage an ultimate ability attack does to an enemy.

    :param character: a dictionary
    :param skills: a dictionary
    :param skill: a string
    :param enemy: a dictionary
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                z is an integer more than or equal to 0 and s is a string
    :precondition: character's keys are a string description of the integer or string values
    :precondition: skills must dictionary in the form of: {"1": 'Punch', "2": 'Kick', "9": "RUN AWAY!"}
    :precondition: skills' keys are string numbers to string values describing a move
    :precondition: skill is a string number representing the user's choice of skill
    :precondition: enemy is a dictionary whose keys are string descriptions of the values
    :precondition: enemy must be in the form of {"Name": s, "Level": n, "HP": n, "ATK": n,"EXP given": n}
                        where s in a string and n is an integer more than 0
    :postcondition: calculate 'damage_dealt' by evaluating character's 'ATK' and 'Level' values and a random integer
    :postcondition: subtracts  enemy's 'HP' value by 'damage_dealt
    :postcondition: print a statement describing the damage dealt and the mana cost
    :postcondition: character's 'Level' value has to be more than or equal to 3

    """
    mana_cost = 15 * character["Level"]
    character["Current Mana"] -= mana_cost
    damage_amplifier = (random.randint(1, character["Level"] - 1))
    damage_dealt = character["ATK"] / damage_amplifier  # damage calculator
    enemy['HP'] -= int(round(damage_dealt))
    print(f"You used {skills[skill]}!"
          f"\n{skills[skill]} was super effective! {int(round(damage_dealt))} damage was dealt to {enemy['Name']} "
          f"\nYou lost {mana_cost} Mana")  # unit tests done


def hero_battle_phase(character: dict, enemy: dict, skill: str,
                      skills: dict) -> None:  # cant make doctests because the function calls functions that uses the random module
    """
    Calls the skill chosen by the user.

    :param character: a dictionary
    :param skills: a dictionary
    :param skill: a string
    :param enemy: a dictionary
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                z is an integer more than or equal to 0 and s is a string
    :precondition: character's keys are a string description of the integer or string values
    :precondition: skills must dictionary in the form of: {"1": 'Punch', "2": 'Kick', "9": "RUN AWAY!"}
    :precondition: skills' keys are string numbers to string values describing a move
    :precondition: skill is a string number representing the user's choice of skill
    :precondition: enemy is a dictionary whose keys are string descriptions of the values
    :precondition: enemy must be in the form of {"Name": s, "Level": n, "HP": n, "ATK": n,"EXP given": n}
                        where s in a string and n is an integer more than 0
    :postcondition: evaluates the skill chosen by the user
    :postcondition: subtracts enemy's 'HP' value by 'damage_dealt
    :postcondition: print a statement if the enemy 'HP' value is equal to or less than 0

    """
    if skill == "1" or skill == "2":  # skills in the 1 and 2 options take no mana but are weaker
        basic_attack(character, enemy, skill, skills)
    elif skill == "3" and character["Current Mana"] >= 10 * character["Level"]:
        strong_attack(character, enemy, skill, skills)
    elif skill == "4" and character["Current Mana"] >= 15 * character["Level"]:  # strongest ability
        ultimate_ability(character, enemy, skill, skills)
    if enemy['HP'] <= 0:  # print statement notifying the user if the enemy is dead
        print(f"You killed {enemy['Name']}")


def enemy_battle_phase(character: dict,  # unit tests done
                       enemy: dict) -> None:  # cant make doctests because the function uses the random module
    """
    Calculates the damage done by the enemy.

    :param character: a dictionary
    :param enemy: a dictionary
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                z is an integer more than or equal to 0 and s is a string
    :precondition: character's keys are a string description of the integer or string values
    :precondition: enemy is a dictionary whose keys are string descriptions of the values
    :precondition: enemy must be in the form of {"Name": s, "Level": n, "HP": n, "ATK": n,"EXP given": n}
                        where s in a string and n is an integer more than 0

    """
    damage_taken = round((enemy['ATK'] * (4 * random.randint(2, enemy['Level'] + 3)) / character[
        "DEF"]))  # damage calculator
    print(f"{enemy['Name']}  attacked you for {damage_taken} damage!")
    character["Current HP"] -= damage_taken


def is_alive(character: dict) -> None:  # unit tests done
    """
    Check if character is alive.

    :param character: a dictionary
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                z is an integer more than or equal to 0 and s is a string
    :precondition: character's keys are a string description of the integer or string values
    :postcondition: evaluates character's 'Current HP' value
    :returns: True if character's "Current HP" value is more than 0, else False

    >>> character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 1}
    >>> is_alive(character_test)
    True
    """
    return character["Current HP"] > 0


def encounter_boss(character: dict, board: dict, boss: dict) -> bool:  # unit test done
    """
    Check if character is in the lower right corner of board.

    :param boss: a dictionary
    :param board: a dictionary
    :param character: a dictionary
    :precondition: board must be a dictionary in the form of: {(0, 0): ‘Empty room’, (0, 1): ‘Empty room’, (1, 0): ‘
                    Empty room’, (1, 1): ‘Empty room’}
    :precondition: board's keys are tuples that contain a set of coordinates and the values are string descriptions
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                z is an integer more than or equal to 0 and s is a string
    :precondition: character's keys are a string description of the integer or string value
    :precondition: boss must be a dictionary in the form of {"Name": S, 'class': 'S, "Level": N, "HP": N, "ATK": N, "EXP given": N},
                  where S is a string and N is an integer more than 0
    :precondition: boss' keys are a string description of its integer or string values
    :postcondition: evaluate boundaries of the board
    :postcondition: evaluate the values of character's "X-coordinate" and "Y-coordinate"
    :return: True if character's coordinates are in the lower right corner of the board, else False

    >>> test_boss = {"Name": "Galactus Ultron", 'class': 'boss', "Level": 8, "HP": 700, "ATK": 700, "EXP given": 50}
    >>> test_character = {'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 5}
    >>> test_board = make_board(7, 7)
    >>> encounter_boss(test_character, test_board, test_boss)
    False
    """
    y_axis_right_edge = 0
    x_axis_lower_edge = 0
    current_coordinates = (character['X-coordinate'], character['Y-coordinate'])
    for coordinates in board.keys():
        if coordinates[0] > x_axis_lower_edge:
            x_axis_lower_edge = coordinates[0]
        if coordinates[1] > y_axis_right_edge:
            y_axis_right_edge = coordinates[1]

    if current_coordinates == (
            x_axis_lower_edge - 1,
            y_axis_right_edge - 1):  # checks if the character is in the bottom right corner of the map

        print("\033[1;31;40m")
        print(f"You made it to {board[current_coordinates]}..."
              f"You see {boss['Name']} standing silently."
              f"Howard: \"BOSS BATTLE TIME!\"")
        print(r"""
   __________                      __________         __    __  .__          
   \______   \ ____  ______ ______ \______   \_____ _/  |__/  |_|  |   ____    
    |    |  _//  _ \/  ___//  ___/  |    |  _/\__  \\   __\   __\  | _/ __ \ 
    |    |   (  <_> )___ \ \___ \   |    |   \ / __ \|  |  |  | |  |_\  ___/         'You wont be able to run away..                                                                                  
    |______  /\____/____  >____  >  |______  /(____  /__|  |__| |____/\___  >         just try it.'
           \/           \/     \/          \/      \/                     \/ 
        """)

        return True
    else:
        return False


def generate_boss() -> dict:  # cant make doctests because the function uses the random module. Unit Tests Done
    """
    Generate a random boss.

    :postcondition: generate a random number between 1 - 9 inclusive
    :postcondition: depending on the random number, generate a dictionary describing a boss
    :postcondition: the dictionary must be in the form of {"Name": S, 'class': 'S, "Level": N, "HP": N, "ATK": N, "EXP given": N},
                  where S is a string and N is an integer more than 0.
    :return: a dictionary describing a boss
    """
    random_boss = random.randint(1, 9)  # each boss has a 33% chance of being picked
    if random_boss in range(1, 4):
        boss = {"Name": "Galactus Ultron", 'class': 'boss', "Level": 7, "HP": 600, "ATK": 600, "EXP given": 50}
    elif random_boss in range(4, 7):
        boss = {"Name": "Astral Regulator Thanos", 'class': 'boss', "Level": 7, "HP": 900, "ATK": 300, "EXP given": 50}
    else:
        boss = {"Name": "God Emperor Doom", 'class': 'boss', "Level": 7, "HP": 800, "ATK": 400, "EXP given": 50}
    return boss


def boss_dead(boss: dict) -> bool:  # unit tests done
    """
    Check if boss is dead.

    :param boss: a dictionary
    :precondition: boss must be a dictionary in the form of {"Name": S, 'class': 'S, "Level": N, "HP": N, "ATK": N, "EXP given": N},
                  where S is a string and N is an integer more than 0
    :precondition: boss' keys are a string description of its integer or string values
    :postcondition: evaluates boss' "HP" value
    :return: True if boss' 'HP' value is less than or equal to 0, else False

    >>> test_boss = {"HP": 1}
    >>> boss_dead(test_boss)
    False
    """
    return boss["HP"] <= 0


def safe_zone(
        character: dict) -> None:  # cant make doctests because the function uses the random module. Unit Tests done
    """
    Restore
    :param character: a dictionary
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                z is an integer more than or equal to 0 and s is a string
    :precondition: character's keys are a string description of the integer or string values
    :postcondition: generate a random number between 1 - 10 inclusive
    :postcondition: if the random number is between 1 - 5 inclusive, increase the character's 'Current HP' and
                    "Current Mana" values based on character's "Level' value
    :postcondition: if "Current HP" becomes  more than "HP cap", set "Current HP" equal to "HP cap"
    :postcondition: if "Current mana" becomes  more than "Mana cap", set "Current Mana" equal to "Mana cap"

    """
    max_hp = character["HP cap"]
    max_mana = character["Mana cap"]
    hp = character["Current HP"]
    mana = character["Current Mana"]
    duck_juice = random.randint(1, 10)
    if duck_juice in range(1, 6) and (hp < max_hp or mana < max_mana):  # 50% chance of getting a safe room to heal
        print("\033[1;34;40m")
        print(f"""( ̲̅:̲̅:̲̅:̲̅[̲̅ ̲̅]̲̅:̲̅:̲̅:̲̅)   ( ̲̅:̲̅:̲̅:̲̅[̲̅ ̲̅]̲̅:̲̅:̲̅:̲̅)   ( ̲̅:̲̅:̲̅:̲̅[̲̅ ̲̅]̲̅:̲̅:̲̅:̲̅)                
                ,~~.
               (  6 )-_,      \'quack! Hey, {character['name']}, {character['title']}! 
          (\___ )=='-'         Do folk from {character['domain']} get sick or something?! You dont look so good\'
            \ .   ) )         \'Here, have some of my Secret Duck Juice! quack!\'
             \ `-' /    
             ~'`~'`~'`~'`~      
                                 """)

        hp += 10 * character["Level"]
        mana += 10 * character["Level"]
        print(f"You drink the Secret Duck Juice. You suddenly crave bread crumbs. "
              f"you gained {10 * character['Level']} HP and {10 * character['Level']} Mana."
              f"\n( ̲̅:̲̅:̲̅:̲̅[̲̅ ̲̅]̲̅:̲̅:̲̅:̲̅)   ( ̲̅:̲̅:̲̅:̲̅[̲̅ ̲̅]̲̅:̲̅:̲̅:̲̅)   ( ̲̅:̲̅:̲̅:̲̅[̲̅ ̲̅]̲̅:̲̅:̲̅:̲̅)")
        print("\033[0m")
        character["Current HP"] = hp if hp <= max_hp else max_hp  # prevents the current hp from going over hp cap
        character["Current Mana"] = mana if mana <= max_mana else max_mana
        # prevents the current mana from going over mana cap


def describe_current_status(character: dict, skills: dict) -> None:  # done unit test
    """
    Print a statement describing the current status of the character.

    :param character: a dictionary
    :param skills: a dictionary
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                z is an integer more than or equal to 0 and s is a string
    :precondition: character's keys are a string description of the integer or string values
    :precondition: skills must dictionary in the form of: {"1": 'Punch', "2": 'Kick', "9": "RUN AWAY!"}
    :precondition: skills' keys are string numbers to string values describing a move
    :postcondition: prints a statement describing the current stats of character
    :postcondition: prints a statement describing the skills the character can use in combat

    >>> test_character = {'name': 'TChalla', 'EXP': 0, 'EXP needed':60, 'Current HP': 220, 'Current Mana': 100, 'ATK': 140, 'DEF': 80, 'title': 'Frog of Thunder', 'domain': 'Asgardian Republic', 'HP cap': 220, 'Mana cap': 100, "Level" : 1}
    >>> default_skills =  {'1': 'Punch', '2': 'Kick', '9': 'RUN AWAY!'}
    >>> describe_current_status(test_character, default_skills)
    \033[1;32;40mTChalla, Frog of Thunder, from the Asgardian Republic, Level: 1
    HP: 220/220   Mana:100/100  ATK: 140  DEF: 80  EXP:  0/60  Abilities: Punch, Kick, RUN AWAY!
    """
    print(f"\033[1;32;40m"
          f"{character['name']}, {character['title']}, from the {character['domain']}, Level: {character['Level']}"
          f"\nHP: {int(round(character['Current HP']))}/{character['HP cap']}   Mana:{character['Current Mana']}/{character['Mana cap']}  "
          f"ATK: {character['ATK']}  DEF: {character['DEF']}  EXP:  {character['EXP']}/{character['EXP needed']}"
          f"  Abilities: {', '.join(skills.values())}")


def run_away(character: dict, enemy: dict) -> None:  # cant make doctests because the function uses the random module
    """
    Provide a 20% chance to take damage if you run away.

    :param character: a dictionary
    :param enemy: a dictionary
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                z is an integer more than or equal to 0 and s is a string
    :precondition: character's keys are a string description of the integer or string values
    :precondition: enemy is a dictionary whose keys are string descriptions of the values
    :precondition: enemy must be in the form of {"Name": s, "Level": n, "HP": n, "ATK": n,"EXP given": n}
                        where s in a string and n is an integer more than 0
    :postcondition: provide a random number from 1 - 10 inclusive as you run away
    :postcondition: calculates damage taken based on enemy's "ATK' and "Level' values
    :postcondition: subtracts damage taken from character's "Current HP' value if the random number is 1 or 2
    """
    print("You run away!")
    damage_chance = random.randint(1, 10)
    if damage_chance in range(1, 3):  # 20% chance of taking damage if you run away
        damage_taken = (enemy['ATK'] * random.randint(1, enemy['Level']) / character[
            "DEF"])  # damage calculator
        character["Current HP"] -= round(damage_taken)
        print(f"{enemy['Name']} deals {round(damage_taken)} damage you as you run away!\n")  # done unit test


def enemy_flee(enemy: dict) -> bool:  # cant make doctests because the function uses the random module  # done unit test
    """
    Provide a 20% chance to allow the enemy to flee.

    :param enemy: a dictionary
    :precondition: enemy is a dictionary whose keys are string descriptions of the values
    :precondition: enemy must be in the form of {"Name": s, "Level": n, "HP": n, "ATK": n,"EXP given": n}
                        where s in a string and n is an integer more than 0
    :postcondition: provide a random number from 1 - 10 inclusive
    :postcondition: the enemy flees if the random number is 1 or 2
    :return: True if the random number is 1 or 2, else False
    """
    if enemy['class'] == 'enemy':  # if the enemy is not a boss, it will have a 20% chance to run away.
        flee_chance = random.randint(1, 10)
        if flee_chance in range(1, 3):
            print(f"{enemy['Name']} runs away!")
            return True  # done unit test
        else:
            return False
    else:
        print(f"{enemy['Name']}: \'Prepare to die!\'")  # if the enemy is a boss, it will print a statement


def battle_phase(character: dict, enemy: dict, skills: dict, list_of_class_titles: list) -> None:
    """
    Drive the main battle phase loop.

    :param character: a dictionary
    :param enemy: a dictionary
    :param skills: a a dictionary
    :param list_of_class_titles: a list
    :precondition: character must be in the form of {'X-coordinate': n, 'Y-coordinate': n, 'Level': n, 'EXP': z,
                'EXP needed': n, 'title': s, 'domain': s} where n is an integer more than 0,
                z is an integer more than or equal to 0 and s is a string
    :precondition: character's keys are a string description of the integer or string values
    :precondition: skills must dictionary in the form of: {"1": 'Punch', "2": 'Kick', "9": "RUN AWAY!"}
    :precondition: skills' keys are string numbers to string values describing a move
    :precondition: enemy is a dictionary whose keys are string descriptions of the values
    :precondition: enemy must be in the form of {"Name": s, "Level": n, "HP": n, "ATK": n,"EXP given": n}
                        where s in a string and n is an integer more than 0
    :postcondition: evaluates the skill chosen by the user
    :precondition: list_of_class_titles must be a list whose elements are strings describing class titles
    """
    while enemy_alive(enemy) and is_alive(character):
        describe_battle(character, enemy)  # prints a statement describing the stats of the foe and the character
        skill = choose_skill(skills, enemy)  # prompt the user for a skill of their choice
        if skill == "RUN AWAY!":  # ends the battle phase if the skill of choice is 'RUN AWAY'!
            run_away(character, enemy)  # provides a 20% chance for the character to take damage if they choose to flee
            is_alive(character)  # checks if character is still alive after taking run away damage
            break  # break out of the battle phase loop
        valid_skill = validate_skill(character, skill)  # checks if the user has enough mana to cast certain skills
        if valid_skill:  # the following functions are called if the skill is valid
            hero_battle_phase(character, enemy, skill, skills)  # damages the user based on the skill
            if enemy_alive(enemy) is True:  # checks if the enemy alive,
                does_enemy_flee = enemy_flee(enemy)  # proves the enemy a 20% chance to be able to flee
                if does_enemy_flee:  # stops the battle_phase function if enemy flees
                    break
                enemy_battle_phase(character, enemy)  # deals damage to the character if the enemy does not flee
                is_alive(character)  # checks if the character is still alive
            else:  # the following functions are called if the enemy is slain
                level_system(character, enemy)  # gains exp based on the enemy
                upgrade_title(character, list_of_class_titles)  # update the character's title based on level


def game():
    """
    Drive the main game loop.

    """
    rows = MIN_NUM_OF_ROWS  # rows is 27
    columns = MIN_NUM_OF_COLUMNS  # columns is 27
    board = make_board(rows, columns)  # makes the board
    character = make_character()  # initializes the character
    title_page()  # prints the title page
    create_name(character)  # prints a narrative and prompts the user to input a name
    context_info()  # prints more narratives
    class_title = choose_class(character)  # returns a class based on the user choice
    add_class_stats(character, class_title)  # updates the character with stats unique to the domain/class
    start_mission()  # prints a narrative and prompts the user to press enter
    skills = create_skills()  # returns a dictionary of skills usable in combat, including a run away option
    list_of_class_titles = list_of_titles(character)  # return a list of titles unique to the character's domain/class
    boss = generate_boss()  # generate a random boss
    upgrade_title(character, list_of_class_titles)  # update the character's title based on level
    map_of_board = make_map(rows, columns)  # make a map of the board
    set_characters(character, board, map_of_board)  # places ascii art, the character, and the boss on the map
    achieved_goal = False  # set the achieved goal to False
    while not achieved_goal and is_alive(
            character):  # the game is active as long as achieved goal is false and the character is alive
        upgrade_skills(skills, character)  # update skills based on level
        describe_current_status(character, skills)  # prints a statement about the character's stats and skills
        display_map(character, map_of_board)  # prints the map, including the location of the user and the boss
        describe_current_location(board, character)  # prints a narrative about the current room the user is in
        direction = get_user_choice()  # prompts the user for a direction, up down, left, right, and quit
        if direction == "quit":  # if the direction is quit, the game ends
            break
        valid_move = validate_move(board, character,  # validates if the direction input is feasible
                                   direction)  # prevents the user from going past the board/map boundaries
        if valid_move:
            move_character(character, direction)  # moves the character based on the direction
            boss_battle = encounter_boss(character, board,
                                         boss)  # checks if you enter the boss by going to the bottom right corner of the map
            set_characters(character, board,
                           map_of_board)  # sets the characters on the again, since move_character changes the characters coordinates
            there_is_a_challenger = check_for_foes()  # proves a 20% chance to encounter a foe
            if there_is_a_challenger or boss_battle:
                enemy = boss if boss_battle else generate_foe(
                    character)  # the enemy is either a regular enemy or a boss
                battle_phase(character, enemy, skills, list_of_class_titles)  # goes fights the enemy
            achieved_goal = boss_dead(
                boss)  # achieved_goal is True if the boss is dead, resulting in the user winning the game.
            safe_zone(character)  # 50% while you have low HP to get healed.
        else:
            print(
                "A strange force is blocking you.... you cant go here.")  # prints a statement notifying the user of an invalid direction choice
    if is_alive(character) is False:  # prints a statement acknowledging your loss
        print("GAME OVER"
              "\nYOU DIED")
    elif boss_dead(boss) is True:  # prints a statement celebrating your win
        print(f"CONGRATULATIONS! YOU beat {boss['Name']}! YOU WIN!")
    else:
        print("You quit The GAME!")  # prints a statement if you quit the game


def main():
    """
    Drive the program.
    """

    game()


if __name__ == "__main__":
    main()
