# реализуем вывод инфоормации о промежутке времени
# в зависимости от его продолжтельности в секундах.
# зная что, 1 минута это 60 сек., 1 час это 3600 сек.,
#  а в сутках 86400 сек. можно предложить следующий вариант:

duration = int(input('введите число:'))
print("Ваше число", duration)
if duration < 60:
    sek = duration
    print('а)', sek, 'сек.')
elif 3600 > duration >= 60:
    sek = duration % 60
    minute = ((duration % 3600) // 60)
    print('b)', minute, "мин.", sek, "сек.")
elif 86400 > duration >= 3600:
    sek = duration % 60
    minute = ((duration % 3600) // 60)
    hour = duration // 3600
    print('c)', hour, 'час.', minute, "мин.", sek, "сек.")
else:
    sek = duration % 60
    minute = ((duration % 3600) // 60)
    hour = ((duration % 86400) // 3600)
    day = duration // 86400
    print('d)', day, 'дн.', hour, 'час.', minute, "мин.", sek, "сек.")
