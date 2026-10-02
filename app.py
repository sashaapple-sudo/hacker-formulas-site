from flask import Flask, render_template

app = Flask(__name__)

# Материалы к урокам
lessons_materials = [
    {"title": "Презентация: Алгоритмы и блок-схемы", "link": "/static/files/lessons/presentation_algorithms.pptx", "desc": "Теория + примеры для 8–9 классов"},
    {"title": "Карточки: Циклы в Python", "link": "/static/files/lessons/task_loops.pdf", "desc": "Практические задания с разбором"},
]

# Подготовка к ОГЭ
oge_materials = [
    {"task_num": "1", "title": "Системы счисления: перевод и сравнение", "link": "/static/files/oge/task1.pdf", "desc": "Перевод между двоичной, восьмеричной, шестнадцатеричной и десятичной системами. Сравнение чисел."},
    {"task_num": "2", "title": "Логические операции и таблицы истинности", "link": "/static/files/oge/task2.pdf", "desc": "Конъюнкция, дизъюнкция, отрицание. Построение таблиц истинности."},
    {"task_num": "3", "title": "Анализ алгоритмов и условий", "link": "/static/files/oge/task3.pdf", "desc": "Чтение псевдокода, понимание условий и ветвлений."},
    {"task_num": "4", "title": "Графы и поиск путей", "link": "/static/files/oge/task4.pdf", "desc": "Построение путей, поиск кратчайшего маршрута по графу."},
    {"task_num": "5", "title": "Исполнители: Робот, Чертежник", "link": "/static/files/oge/task5.pdf", "desc": "Команды, циклы, условия для исполнителей."},
    {"task_num": "6", "title": "Python: базовые конструкции", "link": "/static/files/oge/task6.pdf", "desc": "Переменные, ввод/вывод, простые условия и циклы."},
    {"task_num": "7", "title": "IP-адреса и маски подсети", "link": "/static/files/oge/task7.pdf", "desc": "Восстановление IP-адреса, работа с масками."},
    {"task_num": "8", "title": "Поисковые запросы и круги Эйлера", "link": "/static/files/oge/task8.pdf", "desc": "Логические операции в поисковых запросах. Решение через круги Эйлера."},
    {"task_num": "9", "title": "Схемы дорог и подсчёт путей", "link": "/static/files/oge/task9.pdf", "desc": "Подсчёт количества путей из одной точки в другую."},
    {"task_num": "10", "title": "Сравнение чисел в разных системах счисления", "link": "/static/files/oge/task10.pdf", "desc": "Практические задания на сравнение и упорядочивание чисел."},
    {"task_num": "11", "title": "Файловая система и поиск по маске", "link": "/static/files/oge/task11.pdf", "desc": "Маски файлов, поиск по шаблонам и расширениям."},
    {"task_num": "12", "title": "Электронные таблицы: формулы и диаграммы", "link": "/static/files/oge/task12.xlsx", "desc": "Работа с формулами, фильтрами, построение диаграмм."},
    {"task_num": "13", "title": "13.1Создание презентации и 13.2 Создание текстового документа (шаблон и требования)", "link": "/static/files/oge/task13.pptx", "desc": "Шаблон презентации, требования к оформлению и содержанию."},
    {"task_num": "14", "title": "Excel: обработка данных и сводные таблицы", "link": "/static/files/oge/task14.xlsx", "desc": "Фильтрация, сортировка, сводные таблицы и анализ данных."},
    {"task_num": "15", "title": "Программирование: сложные условия и циклы", "link": "/static/files/oge/task15.pdf", "desc": "Вложенные циклы, сложные условия, оптимизация кода."}
]

# Подготовка к ЕГЭ
ege_materials = [
    {"title": "Советы: Как решать задачу №27", "link": "/static/files/ege/tips_task27.pdf", "desc": "Стратегия, частые ошибки, шаблоны кода"},
    {"title": "Шаблон: Решение задачи №24 на строки", "link": "/static/files/ege/template_code.py", "desc": "Готовый скелет программы с комментариями"},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/materials")
def materials():
    return render_template("materials.html", materials=lessons_materials)

@app.route("/oge")
def oge():
    return render_template("oge.html", materials=oge_materials)

@app.route("/ege")
def ege():
    return render_template("ege.html", materials=ege_materials)

@app.route('/formulas')
def formulas():
    return render_template('formulas.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

