balance.py
def weight_num(max_weight):
    """

    :param max_weight: 1 <= max_weight <= 100
    :return: required number of weight
    """
    weight_list = []
    quit, remain = divmod(max_weight, 3)
    weight_list.append(remain)
    while quit >= 3:
        quit, remain = divmod(quit, 3)
        weight_list.append(remain)

        if quit < 3:
            weight_list.append(quit)

            print(f'必要な分銅の数は{len(weight_list)}個です。')


if __name__ == '__main__':

    n = 100
    weight_num(n)