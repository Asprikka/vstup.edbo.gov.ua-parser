from abit_parser import AbitParser
from faculty import Faculty


# мені було впадло робити якийсь нормальний інтерфейс, тому тут все захардкоджено.
# змінюйте окремі частини коду під свої потреби, і запускайте програму з-під IDE (PyCharm, VS 2019, VS Code тощо)

# змінити перелік факультетів на пошук:    main.py -> faculties  (поточний файл)
# змінити фільтри пошуку по таблиці заяв:  data_table.py -> def apply_show_info_filters(row)

# щодо "фільтрів пошуку по таблиці заяв" - за замовчуванням відображаються абітурієнти, що є:
# -- із _балом_ не менше 194.0;
# -- зі _статусом_ "допущено", "зареєстровано" або "заява надійшла з сайту";
# -- мають _пріоритети_ 1 або 2.

# перелік можливих _статусів_: app_status.py


# Приклад добавлення факультету в список пошуку

# https://vstup.edbo.gov.ua/offer/969296/
# 969296 - offer_code
# 'ФКНК (КНУ)' - name (довільне найменування; не впливає на пошук)
# Faculty(name='ФКНК (КНУ)', offer_code='969296')

faculties = [Faculty('ФКНК (КНУ)', '969296'),
             Faculty('ФІОТ (КПІ)', '986240'),
             Faculty('ФІТ (КНУ)', '992277'),
             Faculty('ФПМ (КПІ)', '986241'),
             Faculty('ІАТЕ/ТЕФ (КПІ)', '986219')]

parser = AbitParser(faculties)

parser.set_webdriver()
parser.parse_faculties()

print('\nshowing table...\n')

for i in range(len(faculties)):
    parser.show_table(i)

# для парсингу https://vstup.edbo.gov.ua використано модулі: BeautifulSoup4 та Selenium
