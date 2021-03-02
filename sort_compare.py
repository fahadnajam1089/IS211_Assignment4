import argparse
# other imports go here
from time \
    import perf_counter as ct
import random


def get_me_random_list(n):
    """Generate list of n elements in random order

    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def insertion_sort(a_list):
    var1 = ct()

    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value

    var2 = ct()
    var = var2 - var1
    return var


def shell_sort(a_list):
    var1 = ct()

    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count //= 2

    var2 = ct()
    var = var2 - var1
    return var


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position -= gap
        a_list[position] = current_value


def python_sort(a_list):
    var1 = ct()

    a_list.sort()

    var2 = ct()
    var = var2 - var1
    return var


def benchmark_results(funcs, n_num, n_ls):
    d = dict()
    for n in range(len(funcs)):
        name = funcs[n].__name__
        d[name.replace('_', ' ').title()] = [funcs[n]]

    for _, v in d.items():
        for _ in range(len(n_num)):
            v.append(0)

    b = 0
    for n in n_num:
        b += 1
        for _ in range(n_ls):
            a_list = get_me_random_list(n)
            for k, v in d.items():
                var = v[0](a_list)
                d[k][b] += var

    for b in range(b):
        print('%s lists of %s elements:' % (n_ls, n_num[b]))
        for k, v in d.items():
            print('%s took %10.7f seconds to run, on average'
                  % (k, v[b + 1] / n_ls))
        print('')


def main():
    algor = [
        insertion_sort
        , shell_sort
        , python_sort
    ]
    list_sizes = 500, 1000, 5000
    num_per_size = 100

    benchmark_results(algor, list_sizes, num_per_size)


if __name__ == "__main__":
    """Main entry point"""
    main()