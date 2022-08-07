# vstup.edbo.gov.ua-parser
Парсер сайту https://vstup.edbo.gov.ua/

Збирає та виводить у консоль інформацію про заяви, що подали абітуруєнти на вступ, за вказаними параметрам (факультети, сортування заяв за балом, статусом та пріоритетами)

# мені було впадло робити якийсь нормальний інтерфейс, тому тут все захардкоджено.
# змінюйте окремі частини коду під свої потреби, і запускайте програму з-під IDE (PyCharm, VS 2019, VS Code тощо)

# змінити перелік факультетів на пошук:    main.py -> faculties  (поточний файл)
# змінити фільтри пошуку по таблиці заяв:  data_table.py -> def apply_show_info_filters(row)

# щодо "фільтрів пошуку по таблиці заяв" - за замовчуванням відображаються абітурієнти, що є:
# -- із _балом_ не менше 194.0;
# -- зі _статусом_ "допущено", "зареєстровано" або "заява надійшла з сайту";
# -- мають _пріоритети_ 1 або 2.

# перелік можливих _статусів_: app_status.py
