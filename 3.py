import datetime as dt

# Запишите момент времени, когда вы начали проходить курс (например, 1 января 2023 года, в 10:00 утра).
start_moment = dt.datetime(2023, 1, 1, 10, 0)

# Запишите текущий момент времени.
current_moment = dt.datetime.now()

# Вычислите разницу двух этих моментов.
total_time = current_moment - start_moment

# Напечатайте разницу.
print(total_time)