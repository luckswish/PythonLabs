money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months_count = 0
month_budget = money_capital

while month_budget - spend > 0:
    month_budget += (salary - spend)
    if months_count != 0:
        spend *= (1 + increase)
    months_count += 1

print("Количество месяцев, которое можно протянуть без долгов:", months_count)
