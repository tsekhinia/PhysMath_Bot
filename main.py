import telebot
from telebot import types
import time
import json

bot = telebot.TeleBot('TOKEN', parse_mode='html')

with open("PHOTO.json", "r") as d:
    photo_json = d.read()

PHOTO = json.loads(photo_json)

with open("MATH.json", "r") as d:
    math_json = d.read()

MATH = json.loads(math_json)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    math = types.KeyboardButton('Математика')
    phys = types.KeyboardButton('Физика')
    markup.add(math, phys)
    bot.send_message(message.chat.id, f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>')
    bot.send_message(message.chat.id,
                     "Я могу подсказать формулы, теоремы и определения из математики и физики (Модуль физика на "
                     "данный момент составлен на основе кодификатора ЕГЭ по физике, дальше будет расширяться).\n\nДля "
                     "начала выбери, какой предмет тебя интересует, либо напиши тему, которая тебя интересует.",
                     reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    math = types.KeyboardButton('Математика')
    phys = types.KeyboardButton('Физика')
    markup.add(math, phys)
    bot.send_message(message.chat.id,
                     "Я могу подсказать формулы, теоремы и определения из математики и физики (Модуль физика на "
                     "данный момент составлен на основе кодификатора ЕГЭ по физике, дальше будет расширяться).\n\nДля "
                     "начала выбери, какой предмет тебя интересует, либо напиши тему, которая тебя интересует.",
                     reply_markup=markup)


@bot.message_handler()
def some_answer(message):
    global MATH
    global PHOTO
    # print(message)
    match message.text:
        case 'Математика' | '<–– Назад к разделам математики':  # Выбор раздела математики
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(*[types.KeyboardButton(s) for s in MATH.keys()],
                       types.KeyboardButton('<–– Назад к предметам'))
            bot.send_message(message.chat.id, 'Выбери раздел', reply_markup=markup)

        case 'Физика' | '<–– Назад к разделам':  # Выбор раздела физики
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.add(types.KeyboardButton('Механика'),
                       types.KeyboardButton('Молекулярная физика и термодинамика'),
                       types.KeyboardButton('Электродинамика'),
                       types.KeyboardButton('Основы специальной теории относительности'),
                       types.KeyboardButton('Квантовая физика'),
                       types.KeyboardButton('<–– Назад к предметам'))
            bot.send_message(message.chat.id, 'Выбери раздел', reply_markup=markup)

        case '<–– Назад к предметам':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            math = types.KeyboardButton('Математика')
            phys = types.KeyboardButton('Физика')
            markup.add(math, phys)
            bot.send_message(message.chat.id, 'Выбери предмет', reply_markup=markup)

        # Выбор темы в разделе математики
        case 'Алгебра' | '<–– Назад к темам алгебры':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(*[types.KeyboardButton(s) for s in MATH['Алгебра'].keys()],
                       types.KeyboardButton('<–– Назад к разделам математики'))
            bot.send_message(message.chat.id, 'Выбери тему', reply_markup=markup)
        case 'Планиметрия' | '<–– Назад к темам планиметрии':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.add(*[types.KeyboardButton(s) for s in MATH['Планиметрия'].keys()],
                       types.KeyboardButton('<–– Назад к разделам математики'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Стереометрия' | '<–– Назад к темам стереометрии':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.add(*[types.KeyboardButton(s) for s in MATH['Стереометрия'].keys()][:2], row_width=1)
            markup.add(*[types.KeyboardButton(s) for s in MATH['Стереометрия'].keys()][2:],
                       types.KeyboardButton('<–– Назад к разделам математики'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)

        # Выбор подтемы в теме из раздела "Алгебра"
        # case 'Формулы сокращенного умножения':
        #     Отослать пикчу
        case 'Прогрессии':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.add(*[types.KeyboardButton(s) for s in MATH['Алгебра']['Прогрессии']],
                       types.KeyboardButton('<–– Назад к темам алгебры'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Теория вероятностей':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.add(*[types.KeyboardButton(s) for s in MATH['Алгебра']['Теория вероятностей']],
                       types.KeyboardButton('<–– Назад к темам алгебры'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        # case 'Свойства степеней':
        # case 'Свойства логарифмов':
        case 'Тригониметрия':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.add(*[types.KeyboardButton(s) for s in MATH['Алгебра']['Тригониметрия'][:5]])
            markup.add(*[types.KeyboardButton(s) for s in MATH['Алгебра']['Тригониметрия'][5:]],
                       types.KeyboardButton('<–– Назад к темам алгебры'), row_width=1)
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Производные и первообразные':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.add(*[types.KeyboardButton(s) for s in MATH['Алгебра']['Производные и первообразные']],
                       types.KeyboardButton('<–– Назад к темам алгебры'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)

        # Выбор подтемы в теме из раздела "Планиметрия"
        case 'Треугольники и углы. Параллельные прямые':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.add(
                *[types.KeyboardButton(s) for s in MATH['Планиметрия']['Треугольники и углы. Параллельные прямые']],
                types.KeyboardButton('<–– Назад к темам планиметрии'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Средние линии и медианы треугольника':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.add(*[types.KeyboardButton(s) for s in MATH['Планиметрия']['Средние линии и медианы треугольника']],
                       types.KeyboardButton('<–– Назад к темам планиметрии'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Прямоугольный треугольник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(*[types.KeyboardButton(s) for s in MATH['Планиметрия']['Прямоугольный треугольник']],
                       types.KeyboardButton('<–– Назад к темам планиметрии'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Многоугольники':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(*[types.KeyboardButton(s) for s in MATH['Планиметрия']['Многоугольники']],
                       types.KeyboardButton('<–– Назад к темам планиметрии'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Параллелограмм':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(*[types.KeyboardButton(s) for s in MATH['Планиметрия']['Параллелограмм']],
                       types.KeyboardButton('<–– Назад к темам планиметрии'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Правильные многоугольники':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.add(*[types.KeyboardButton(s) for s in MATH['Планиметрия']['Правильные многоугольники']],
                       types.KeyboardButton('<–– Назад к темам планиметрии'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Трапеция':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.add(*[types.KeyboardButton(s) for s in MATH['Планиметрия']['Трапеция']],
                       types.KeyboardButton('<–– Назад к темам планиметрии'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Все о площадях':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.add(*[types.KeyboardButton(s) for s in MATH['Планиметрия']['Все о площадях']],
                       types.KeyboardButton('<–– Назад к темам планиметрии'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Окружность и вписанные четырехугольники':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(
                *[types.KeyboardButton(s) for s in MATH['Планиметрия']['Окружность и вписанные четырехугольники']],
                types.KeyboardButton('<–– Назад к темам планиметрии'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Высота треугольника и ортоцентр':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.add(*[types.KeyboardButton(s) for s in MATH['Планиметрия']['Высота треугольника и ортоцентр']],
                       types.KeyboardButton('<–– Назад к темам планиметрии'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Биссектрисы и инцентр':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(*[types.KeyboardButton(s) for s in MATH['Планиметрия']['Биссектрисы и инцентр']],
                       types.KeyboardButton('<–– Назад к темам планиметрии'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Метод координат':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.add(*[types.KeyboardButton(s) for s in MATH['Планиметрия']['Метод координат']],
                       types.KeyboardButton('<–– Назад к темам планиметрии'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Счетные теоремы планиметрии':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.add(*[types.KeyboardButton(s) for s in MATH['Планиметрия']['Счетные теоремы планиметрии']],
                       types.KeyboardButton('<–– Назад к темам планиметрии'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)

        # Выбор подтемы в теме из раздела "Стереометрия"
        case 'Важнейшие аксиомы стереометрии. Способы задать плоскость':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.add(*[types.KeyboardButton(s) for s in
                         MATH['Стереометрия']['Важнейшие аксиомы стереометрии. Способы задать плоскость']],
                       types.KeyboardButton('<–– Назад к темам стереометрии'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Параллельность. Взаимное расположение объектов в пространстве':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(*[types.KeyboardButton(s) for s in
                         MATH['Стереометрия']['Параллельность. Взаимное расположение объектов в пространстве']],
                       types.KeyboardButton('<–– Назад к темам стереометрии'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Перпендикулярность':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.add(*[types.KeyboardButton(s) for s in MATH['Стереометрия']['Перпендикулярность']],
                       types.KeyboardButton('<–– Назад к темам стереометрии'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Расстояние между объектами':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(*[types.KeyboardButton(s) for s in MATH['Стереометрия']['Расстояние между объектами']],
                       types.KeyboardButton('<–– Назад к темам стереометрии'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Углы между объектами':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(*[types.KeyboardButton(s) for s in MATH['Стереометрия']['Углы между объектами']],
                       types.KeyboardButton('<–– Назад к темам стереометрии'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Сечения':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(*[types.KeyboardButton(s) for s in MATH['Стереометрия']['Сечения']],
                       types.KeyboardButton('<–– Назад к темам стереометрии'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        # case 'Объемы и площади поверхностей фигур':
        # Отправить пикчу

        # Выбор темы в разделе физики
        case 'Механика' | '<–– Назад к темам механики':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(types.KeyboardButton('Кинематика'),
                       types.KeyboardButton('Динамика'),
                       types.KeyboardButton('Статика'),
                       types.KeyboardButton("Законы сохранения в механике"),
                       types.KeyboardButton('Механические колебания и волны'),
                       types.KeyboardButton('<–– Назад к разделам'))
            bot.send_message(message.chat.id, 'Выбери тему', reply_markup=markup)
        case 'Молекулярная физика и термодинамика' | '<–– Назад к темам МКТ и термодинамики':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(types.KeyboardButton('Молекулярная физика'),
                       types.KeyboardButton('Термодинамика'),
                       types.KeyboardButton('<–– Назад к разделам'))
            bot.send_message(message.chat.id, 'Выбери тему', reply_markup=markup)
        case 'Электродинамика' | '<–– Назад к темам Электродинамики':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(types.KeyboardButton('Электрическое поле'),
                       types.KeyboardButton('Законы постоянного тока'),
                       types.KeyboardButton('Магнитное поле'),
                       types.KeyboardButton('Электромагнитная индукция'),
                       types.KeyboardButton('Электромагнитные колебания и волны'),
                       types.KeyboardButton('Оптика'),
                       types.KeyboardButton('<–– Назад к разделам'))
            bot.send_message(message.chat.id, 'Выбери тему', reply_markup=markup)
        case 'Основы специальной теории относительности':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(types.KeyboardButton(
                'Инвариантность модуля скорости света в вакууме. Принцип относительности Эйнштейна'),
                types.KeyboardButton('Энергия свободной частицы. Импульс частицы'),
                types.KeyboardButton('Связь массы и энергии свободной частицы'),
                types.KeyboardButton('Энергия покоя свободной частицы'),
                types.KeyboardButton('<–– Назад к разделам'))
            bot.send_message(message.chat.id, 'Выбери тему', reply_markup=markup)
        case 'Квантовая физика' | '<–– Назад к темам квантовой физики':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(types.KeyboardButton('Корпускулярно-волновой дуализм'),
                       types.KeyboardButton('Физика атома'),
                       types.KeyboardButton('Физика атомного ядра'),
                       types.KeyboardButton('<–– Назад к разделам'))
            bot.send_message(message.chat.id, 'Выбери тему', reply_markup=markup)

        # Выбор подтемы в теме из раздела "Механика"
        case 'Кинематика':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(
                types.KeyboardButton('Механическое движение. Относительность механического движения. Система отсчёта'),
                types.KeyboardButton('Материальная точка. Её радиус-вектор, траектория, перемещение, путь'),
                types.KeyboardButton('Скорость материальной точки. Перемещение и путь на графике u(t)'),
                types.KeyboardButton('Ускорение материальной точки'),
                types.KeyboardButton('Равномерное прямолинейное движение'),
                types.KeyboardButton('Равноускоренное прямолинейное движение. Путь при равноускоренном движении'),
                types.KeyboardButton('Свободное падение. Движение тела, брошенного под углом к горизонту'),
                types.KeyboardButton(
                    'Движение по окружности. Угловая и линейная скорость. Центростремительное ускорение'),
                types.KeyboardButton('<–– Назад к темам механики'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Динамика':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(types.KeyboardButton(
                'Инерциальные системы отсчёта. Первый закон Ньютона. Принцип относительности Галилея'),
                types.KeyboardButton('Масса тела. Плотность вещества'),
                types.KeyboardButton('Сила. Принцип суперпозиции сил'),
                types.KeyboardButton('Второй закон Ньютона'),
                types.KeyboardButton('Третий закон Ньютона'),
                types.KeyboardButton('Закон всемирного тяготения. Сила тяжести. Центр тяжести тела'),
                types.KeyboardButton('Движение небесных тел и их искусственных спутников. Первая космическая скорость'),
                types.KeyboardButton('Вторая космическая скорость'),
                types.KeyboardButton('Сила упругости. Закон Гука'),
                types.KeyboardButton(
                    'Сила трения. Сухое трение. Сила трения скольжения, трения покояю. Коэффициент трения'),
                types.KeyboardButton('Давление'),
                types.KeyboardButton('<–– Назад к темам механики'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Статика':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(types.KeyboardButton('Момент силы'),
                       types.KeyboardButton('Центр масс'),
                       types.KeyboardButton('Условия равновесия твёрдого тела в ИСО'),
                       types.KeyboardButton('Закон Паскаля'),
                       types.KeyboardButton('Давление в жидкости'),
                       types.KeyboardButton('Закон Архимеда. Сила Архимеда. Условие плавания тел.'),
                       types.KeyboardButton('<–– Назад к темам механики'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Законы сохранения в механике':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(types.KeyboardButton('Импульс материальной точки'),
                       types.KeyboardButton('Импульс системы тел'),
                       types.KeyboardButton('Закон сохранения импульса (ЗСИ)'),
                       types.KeyboardButton('Работа силы'),
                       types.KeyboardButton('Мощность силы'),
                       types.KeyboardButton('Кинетическая энергия'),
                       types.KeyboardButton('Потенциальная энергия'),
                       types.KeyboardButton('Закон сохранения механической энергии (ЗСЭ)'),
                       types.KeyboardButton('<–– Назад к темам механики'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Механические колебания и волны':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(types.KeyboardButton('Гармонические колебания. Амплитуда и фаза колебаний'),
                       types.KeyboardButton('Период и частота колебаний. Период малых колебаний'),
                       types.KeyboardButton('Вынужденные колебания. Резонанс. Резонансная кривая'),
                       types.KeyboardButton('Поперечные и продольные волны. Скорость распространения и длина волны'),
                       types.KeyboardButton('Интерференция и дифракция волн'),
                       types.KeyboardButton('Звук. Скорость звука'),
                       types.KeyboardButton('<–– Назад к темам механики'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)

        # Выбор подтемы в теме из раздела "Молекулярная физика и термодинамика"
        case 'Молекулярная физика':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(types.KeyboardButton('Модели строения вещества. Количество вещества'),
                       types.KeyboardButton('Тепловое движение атомов и молекул вещества'),
                       types.KeyboardButton('Взаимодействие частиц вещества'),
                       types.KeyboardButton('Диффузия. Броуновское движение'),
                       types.KeyboardButton('Модель идеального газа в МКТ'),
                       types.KeyboardButton('Основное уравнение МКТ'),
                       types.KeyboardButton('Абсолютная температура'),
                       types.KeyboardButton('Связь температуры газа со средней кинетической энергией молекул'),
                       types.KeyboardButton('Уравнение p = nkT'),
                       types.KeyboardButton('Модель идеального газа в термодинамике. Уравнение Менделеева–Клапейрона'),
                       types.KeyboardButton('Внутренняя энергия идеального одноатомного газа'),
                       types.KeyboardButton('Закон Дальтона для давления смеси разреженных газов'),
                       types.KeyboardButton('Изопроцессы. Объединённый газовый закон'),
                       types.KeyboardButton('Графическое представление изопроцессов на pV-, pT- и VT- диаграммах'),
                       types.KeyboardButton('Насыщенные и ненасыщенные пары'),
                       types.KeyboardButton('Влажность воздуха'),
                       types.KeyboardButton('Испарение и конденсация, кипение жидкости (парообразование)'),
                       types.KeyboardButton('Плавление и кристаллизация'),
                       types.KeyboardButton('Преобразование энергии в фазовых переходах'),
                       types.KeyboardButton('<–– Назад к темам МКТ и термодинамики'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Термодинамика':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(
                types.KeyboardButton('Тепловое равновесие и температура'),
                types.KeyboardButton('Внутренняя энергия'),
                types.KeyboardButton('Теплопередача: конвекция, теплопроводность, излучение'),
                types.KeyboardButton('Количество теплоты. Теплоемность. Удельная теплоёмкость вещества'),
                types.KeyboardButton('Удельная теплота парообразования/плавления/сгорания топлива'),
                types.KeyboardButton('Уравнение теплового баланса'),
                types.KeyboardButton('Работа в термодинамике (работа газа)'),
                types.KeyboardButton('Первый закон термодинамики. Адиабата'),
                types.KeyboardButton('Второй закон термодинамики. Необратимые процессы'),
                types.KeyboardButton('Тепловые машины. КПД'),
                types.KeyboardButton('Цикл Карно (максимальное значение КПД)'),
                types.KeyboardButton('<–– Назад к темам МКТ и термодинамики'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)

        # Выбор подтемы в теме из раздела "Электродинамика"
        case 'Электрическое поле':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(
                types.KeyboardButton('Электризация. Электрический заряд. Закон сохранения электрического заряда'),
                types.KeyboardButton('Взаимодействие зарядов. Закон Кулона (Кулоновская сила)'),
                types.KeyboardButton('Электрическое поле'),
                types.KeyboardButton('Напряжённость электрического поля. Поле точечного заряда. Линии напряжённости'),
                types.KeyboardButton(
                    'Потенциал электростатического поля. Потенциальная энергия заряда в электростатическом поле'),
                types.KeyboardButton('Принцип суперпозиции электрических полей'),
                types.KeyboardButton('Проводники в электростатическом поле. Условие равновесия зарядов'),
                types.KeyboardButton('Диэлектрики в электростатическом поле. Диэлектрическая проницаемость вещества ε'),
                types.KeyboardButton('Конденсатор. Электроёмкость конденсатора. Плоский конденсатор'),
                types.KeyboardButton('Параллельное соединение конденсаторов'),
                types.KeyboardButton('Последовательное соединение конденсаторов'),
                types.KeyboardButton('Энергия заряженного конденсатора'),
                types.KeyboardButton('<–– Назад к темам Электродинамики'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Законы постоянного тока':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(
                types.KeyboardButton('Сила тока'),
                types.KeyboardButton('Условия существования электрического тока. Напряжение и ЭДС'),
                types.KeyboardButton('Закон Ома для участка цепи'),
                types.KeyboardButton('Электрическое сопротивление'),
                types.KeyboardButton('Источники тока. ЭДС источника тока. Внутреннее сопротивление'),
                types.KeyboardButton('Закон Ома для полной (замкнутой) электрической цепи'),
                types.KeyboardButton('Параллельное и последовательное соединение проводников'),
                types.KeyboardButton('Работа электрического тока. Закон Джоуля – Ленца'),
                types.KeyboardButton('Мощность электрического тока. Тепловая мощность. Мощность источника тока'),
                types.KeyboardButton('Механизмы проводимости в различных веществах. Полупроводники'),
                types.KeyboardButton('<–– Назад к темам Электродинамики'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Магнитное поле':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(
                types.KeyboardButton('Механическое взаимодействие магнитов'),
                types.KeyboardButton('Магнитное поле. Вектор магнитной индукции. Принцип суперпозиции магнитных полей'),
                types.KeyboardButton('Линии индукции магнитного поля'),
                types.KeyboardButton('Опыт Эрстеда. Магнитное поле проводника с током'),
                types.KeyboardButton('Сила Ампера'),
                types.KeyboardButton('Сила Лоренца. Движение заряженной частицы в однородном магнитном поле'),
                types.KeyboardButton('<–– Назад к темам Электродинамики'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Электромагнитная индукция':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(
                types.KeyboardButton('Поток вектора магнитной индукции'),
                types.KeyboardButton('Явление электромагнитной индукции. ЭДС индукции'),
                types.KeyboardButton('Закон электромагнитной индукции Фарадея'),
                types.KeyboardButton('ЭДС индукции в прямом движущемся проводнике'),
                types.KeyboardButton('Правило Ленца'),
                types.KeyboardButton('Индуктивность. Самоиндукция. ЭДС самоиндукции'),
                types.KeyboardButton('Энергия магнитного поля катушки с током'),
                types.KeyboardButton('<–– Назад к темам Электродинамики'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Электромагнитные колебания и волны':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(
                types.KeyboardButton('Колебательный контур. Свободные электромагнитные колебания'),
                types.KeyboardButton(
                    'Формула Томсона (период колебаний в LC цепи). Связь амплитуды заряда конденсатора с амплитудой силы тока'),
                types.KeyboardButton('Закон сохранения энергии в идеальном колебательном контуре'),
                types.KeyboardButton('Вынужденные электромагнитные колебания. Резонанс'),
                types.KeyboardButton('Переменный ток'),
                types.KeyboardButton('Свойства электромагнитных волн'),
                types.KeyboardButton('Шкала электромагнитных волн. Электромагнитные волны в технике и быту'),
                types.KeyboardButton('<–– Назад к темам Электродинамики'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Оптика':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(
                types.KeyboardButton('Прямолинейное распространение света в однородной среде'),
                types.KeyboardButton('Законы отражения света'),
                types.KeyboardButton('Построение изображений в плоском зеркале'),
                types.KeyboardButton('Законы преломления света. Показатель преломления'),
                types.KeyboardButton('Полное внутреннее отражение'),
                types.KeyboardButton(
                    'Собирающие и рассеивающие линзы. Фокусное расстояние и оптическая сила тонкой линзы'),
                types.KeyboardButton('Формула тонкой линзы. Линейное увеличение'),
                types.KeyboardButton('Построения в линзах'),
                types.KeyboardButton('Фотоаппарат как оптический прибор. Глаз как оптическая система'),
                types.KeyboardButton('Интерференция света. Когерентные источники. Максимумы и минимумы'),
                types.KeyboardButton('Дифракция света. Дифракционная решётка. Главные максимумы'),
                types.KeyboardButton('Дисперсия света'),
                types.KeyboardButton('<–– Назад к темам Электродинамики'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)

        # Выбор подтемы в теме из раздела "Квантовая физика"
        case 'Корпускулярно-волновой дуализм':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(
                types.KeyboardButton('Гипотеза М. Планка о квантах. Формула Планка'),
                types.KeyboardButton('Фотоны. Энергия фотона. Импульс фотона'),
                types.KeyboardButton('Фотоэффект. Опыты А.Г. Столетова. Законы фотоэффекта'),
                types.KeyboardButton('Уравнение Эйнштейна для фотоэффекта'),
                types.KeyboardButton('Волновые свойства частиц. Волны де Бройля. Корпускулярно-волновой дуализм'),
                types.KeyboardButton('Дифракция электронов на кристаллах'),
                types.KeyboardButton('Давление света'),
                types.KeyboardButton('<–– Назад к темам квантовой физики'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Физика атома':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(
                types.KeyboardButton('Планетарная модель атома'),
                types.KeyboardButton('Постулаты Бора. Переход атома с одного уровня энергии на другой'),
                types.KeyboardButton('Линейчатые спектры. Спектр уровней энергии атома водорода'),
                types.KeyboardButton('Лазер'),
                types.KeyboardButton('<–– Назад к темам квантовой физики'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)
        case 'Физика атомного ядра':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(
                types.KeyboardButton('Нуклонная модель ядра. Заряд ядра. Массовое число. Изотопы'),
                types.KeyboardButton('Энергия связи нуклонов в ядре. Ядерные силы'),
                types.KeyboardButton('Дефект массы ядра'),
                types.KeyboardButton('Радиоактивность. Альфа и Бетта распады. Гамма излучение'),
                types.KeyboardButton('Закон радиоактивного распада'),
                types.KeyboardButton('Ядерные реакции. Деление и синтез ядер'),
                types.KeyboardButton('<–– Назад к темам квантовой физики'))
            bot.send_message(message.chat.id, 'Выбери подтему', reply_markup=markup)

        case _:
            if message.text in PHOTO.keys():  # Отправка скриншота
                if type(PHOTO[message.text]) in (str, int, float):
                    bot.send_photo(message.chat.id,
                                   open(f'/Users/ivan_tsekhin/PycharmProjects/tg_bot/pics/{PHOTO[message.text]}.png',
                                        'rb'))
                else:
                    for i in PHOTO[message.text]:
                        bot.send_photo(message.chat.id,
                                       open(f'/Users/ivan_tsekhin/PycharmProjects/tg_bot/pics/{i}.png', 'rb'))
            else:  # Поиск по слову/словосочетанию
                arr = []
                for topic in PHOTO.keys():
                    a = 0
                    for word in message.text.split():
                        if len(word) > 6:
                            if word.lower()[:-2] in topic.lower():
                                a += 1
                        else:
                            if word.lower()[:-1] in topic.lower():
                                a += 1
                    if a == len(message.text.split()):
                        arr.append(topic)
                if arr:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                    markup.add(*[types.KeyboardButton(s) for s in arr],
                               types.KeyboardButton('<–– Назад к предметам'))
                    bot.send_message(message.chat.id, 'Что из этого вы искали?', reply_markup=markup)
                elif message.text.lower() == 'мгу топ':  # Пасхалка 1
                    bot.send_sticker(message.chat.id,
                                     open('/Users/ivan_tsekhin/PycharmProjects/tg_bot/pics/sticker.webp', 'rb'))
                elif message.text.lower() == 'ты тупой':  # Пасалка 2
                    bot.send_message(message.chat.id, 'Я знаю больше тебя')
                else:
                    file = open('errors.csv', 'a', buffering=1)
                    file.write(
                        f'{message.from_user.id}, {message.from_user.first_name} {message.from_user.last_name}, {time.asctime()}: {message.text}\n')
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    math = types.KeyboardButton('Математика')
                    phys = types.KeyboardButton('Физика')
                    markup.add(math, phys)
                    bot.send_message(message.chat.id, 'Я не нашел подходящей темы, попробуй спросить по-другому или '
                                                      'поищи нужную тему в меню. \n \n/help – посмотреть функционал '
                                                      'бота. \n/start – начать с начала.', reply_markup=markup)


bot.infinity_polling()
