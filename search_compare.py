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


def sequential_search(a_list, item):
    var1 = ct()

    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    var2 = ct()
    var = var2 - var1
    return found, var


def ordered_sequential_search(a_list, item):
    var1 = ct()

    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    var2 = ct()
    var = var2 - var1
    return found, var


def binary_search_iterative(a_list, item):
    var1 = ct()

    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    var2 = ct()
    var = var2 - var1
    return found, var


def binary_search_recursive(a_list, item):
    var1 = ct()

    def _binary_search_recursive(a_list, item):
        if len(a_list) == 0:
            return False
        else:
            midpoint = len(a_list) // 2
            if a_list[midpoint] == item:
                return True
            else:
                if item < a_list[midpoint]:
                    return _binary_search_recursive(a_list[:midpoint], item)
                else:
                    return _binary_search_recursive(a_list[midpoint + 1:], item)

    found = _binary_search_recursive(a_list, item)
    var2 = ct()
    var = var2 - var1
    return found, var


def benchmark_results(funcs, n_num, n_ls, target):
    d = dict()
    for i in range(len(funcs)):
        name = funcs[i].__name__
        d[name.replace('_', ' ').title()] = [funcs[i]]

    for _, v in d.items():
        for _ in range(len(n_num)):
            v.append(0)

    e = 0
    for n in n_num:
        e += 1
        for _ in range(n_ls):
            a_list = get_me_random_list(n)
            a_list.sort()
            for k, v in d.items():
                _, var = v[0](a_list, target)
                d[k][e] += var

    for e in range(e):
        print('%s lists of %s elements:' % (n_ls, n_num[e]))
        for k, v in d.items():
            print('Average time it took %s to run: %10.7f seconds'
                  % (k, v[e + 1] / n_ls))
        print('')


def main():
    algor = [
        sequential_search
        , ordered_sequential_search
        , binary_search_iterative
        , binary_search_recursive
    ]
    list_sizes = 500, 1000, 5000
    num_per_size = 100
    search_target = 99999999

    benchmark_results(algor, list_sizes, num_per_size, search_target)


if __name__ == "__main__":
    """Main entry point"""
    main()