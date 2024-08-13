count_of_tickets = int(input("Введите количество билетов: "))
age_list = [int(input("Введите возраст посетителя: ")) for i in range(count_of_tickets)]
price_list = []
for i in range(len(age_list)):
    if age_list[i] < 18:
        price = 0
    elif 18 <= age_list[i] <= 25:
        price = 990
    else:
        price = 1390
    price_list.append(price)
sum_price = sum(price_list)
if count_of_tickets > 3:
    sum_price -= sum_price / 10
print(f"Сумма к оплате: {int(sum_price)} руб.")
