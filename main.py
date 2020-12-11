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


def broadcast(ip_data, mask_data):
    result = []
    for i in range(IP_PARTS_COUNT):
        result.append(str(int(ip_data[i]) & int(mask_data[i])))  # & - and (перемножение)
    return result


while True:
    src_ip = input('ip адрес: ').split('.')  # Ввод ip
    src_mask = input('Mask: ').split('.')  # Ввод маски

    if not validate_ip(src_ip) or not validate_ip(src_mask):  # Проверка ввода 4 значений
        print('error')
        continue

    print('-' * 62)
    print_result('ip: ', src_ip)
    print_result('mask: ', src_mask)
    print_result('network: ', calc_network(src_ip, src_mask))
    print_result('wildcard: ', calc_wildcard(src_mask))
    print_result('broadcast: ', broadcast(src_ip, src_mask))
    print('-' * 62)

# 192.168.99.54
# 255.255.255.0
