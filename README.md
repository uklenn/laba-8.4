# Лабораторная работа №8.4. Библиотеки

## Практическое задание

1.   Научите Анфису отвечать на вопрос «Анфиса, как дела?» случайным образом.
Напишите функцию how_are_you(), она должна вернуть случайный элемент из списка answers. Добавьте в список свои варианты ответов: ничего не сломается, а работать станет интереснее.


2.  Научите Анфису сообщать пользователю, сколько времени шёл его любимый сериал.
Дата выхода первой серии - 17 апреля 2011 года.
Дата выхода последней серии - 15 апреля 2019 года.



3. Напишите код, который рассчитает, сколько времени у вас ушло на вводный курс по бэкенд-разработке.
Вспомните, в какой день и во сколько вы начали проходить курс. Запишите этот момент времени (полностью, с часами и минутами) в переменную start_moment. В переменную current_moment запишите текущий момент времени. Затем вычислите разницу двух этих моментов, запишите её в переменную total_time, и напечатайте её.



4.  Напишите функцию, которая по названию города скажет, сколько там сейчас времени.
Мы заготовили словарь UTC_OFFSET, где для каждого города записана его поправка к UTC в часах.

5. В код добавлен словарь DATABASE, в нём хранятся данные о том, кто из друзей где живёт.
Напишите код функции what_time(), которая по имени друга скажет, сколько у него сейчас времени.
На вход функция должна получить имя друга, а вернуть — текущее время в его городе.

6. Сделайте так, чтобы функция what_time() возвращала время в формате часы:минуты.


7. Примените все полученные в этой теме знания, чтобы научить Анфису отвечать на вопросы про друзей, сколько у них сейчас времени:

    Артём, который час?
    Антон, который час?

Примеры таких запросов уже добавлены в список queries в функции runner().

Измените функцию process_friend(), чтобы она обрабатывала ещё один запрос, а именно query == 'который час?'

Если город друга есть в базе UTC_OFFSET, вызовите функцию what_time() и, подставив полученный результат, верните ответ в формате Там сейчас 19:28.

Если город отсутствует в базе UTC_OFFSET, то верните сообщение об ошибке <не могу определить время в городе {название}>.



