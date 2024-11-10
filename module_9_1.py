def apply_all_func(int_list, *functions):
    #int_list - список из чисел (int, float)
    #*functions - неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)
    result = {}

    for f in functions:
        result[f.__name__] = f(int_list)
    return result

    def min_arg(int_list):
        return min(int_list)

    def max_arg(arg):
        return max(arg)

    def len_arg(arg):
        return len(arg)

    def sum_arg(arg):
        return sum(arg)

    def sorted_arg(arg):
        return sorted(arg)


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))