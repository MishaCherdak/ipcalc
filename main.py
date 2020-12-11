IP_PARTS_COUNT = 4  # Константа кол-во частей в адресе


def bit_not(n):  # Инвертирование побитово (для wildcard)
    return 255 - n


def ip_to_string(ip_data):  # Получение строки из ip
    return '.'.join(ip_data)


def ip_to_bin_string(ip_data):  # Перевод ip в двоичную
    result = []
    for v in ip_data:  # Цикл для перебора 4 значений (i = значение)
        result.append("{0:08b}".format(int(v)))  # Добавляем полученные 8-октетные значения в список вывода
    return ip_to_string(result)  # Вызов функции ip_to_string


def calc_network(ip_data, mask_data):  # network
    result = []
    for i in range(IP_PARTS_COUNT):
        result.append(str(int(ip_data[i]) & int(mask_data[i])))  # & - and (перемножение)
    return result


def calc_wildcard(mask_data):  # Функция обратной маски (wildcard)
    result = []
    for v in mask_data:
        result.append(str(bit_not(int(v))))  # Вызов функции bit_not
    return result


def print_result(caption, result):  # Красивый вывод {значение} (двоичный)
    print(f'{caption}: ', end='')
    print('{0} = {1}'.format(ip_to_string(result), ip_to_bin_string(result)))


def validate_ip(ip_data):  # ПроверОЧКА
    if len(ip_data) != IP_PARTS_COUNT:  # Проверка 4 значений
        return False

    for v in ip_data:
        if not v.isdigit() or (int(v) not in range(0, 256)):  # Проверка, что это чилсо и оно в диапозоне
            return False

    return True


def prefix_mask(mask_data):    # Подсчет маски подсети
    result = 0
    mask = ip_to_bin_string(mask_data).replace('.', '')    # Просто из маски убираем (.) и считаем 1
    for v in mask:
        if int(v) == 1:
            result += 1
    return result


while True:
    src_ip = input('ip адрес: ').split('.')  # Ввод ip
    src_mask = input('Mask: ').split('.')  # Ввод маски

    if not validate_ip(src_ip) or not validate_ip(src_mask):  # Проверка ввода 4 значений
        print('error')
        continue

    print_result('IP адрес: ', src_ip)
    print_result('Маска подсети: ', src_mask)
    print('Префикс маски подсети:', prefix_mask(src_mask))
    print_result('IP адрес сети: ', calc_network(src_ip, src_mask))
    print_result('Обратная маска подсети: ', calc_wildcard(src_mask))
    print('COMPLETE')

# 192.168.99.54
# 255.255.255.0
