# .../Dev/character_creation_module/main.py
from random import randint

DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80

class Character:
    RANGE_VALUE_ATTACK = (1, 3)
    # Новая переменная класса — диапазон значения защиты.
    RANGE_VALUE_DEFENCE = (1, 5)
    # Вот они — две новые константы.
    SPECIAL_BUFF = 15
    SPECIAL_SKILL = 'Удача'
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'
    # Объявляем конструктор класса.
    def __init__(self, name):
        self.name = name
    
   # Объявляем метод атаки
    def attack(self):
        # Вместо диапазона записана переменная класса.
        # Оператор * распаковывает передаваемый кортеж.
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')
    
    # Объявляем метод защиты.
    def defence(self):
        # Вычисляем значение защиты в переменной value_defence.
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона.')
    
    # Объявляем метод специального умения.
    def special(self):
        # Здесь описано тело метода special().
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    # Новый метод базового класса.
    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'

class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'

class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'

class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'

def choice_char_class(char_name: str) -> Character:

    game_classes = {'warrior:': Warrior, 'mage': Mage, 'healer': Healer}

    approve_choice: str  = None

    while approve_choice != 'y':
      selected_class = input('Введи название персонажа, '
                             'за которого хочешь играть: Воитель — warrior, '
                             'Маг — mage, Лекарь — healer: ')
      char_class: Character = game_classes[selected_class](char_name)

      print(char_class)
      approve_choice = input()
      return char_class

def start_training(character):

    commands = {'attack': char_class.attack(),
                'defence': char_class.defence(),
                'special': char_class.special()}
    print(Character)
    print('Потренируйся управлять своими навыками.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd in char_class:
            print(char_class[cmd]())
    return 'Тренировка окончена.'

warrior = Warrior('Кодослав')
print(warrior)
print(warrior.attack())