#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    real_no = 0
    for i in range(0,  x):
        try:
            if type(my_list[i]) == int:
                print("{}".format(my_list[i]), end="")
                real_no += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (real_no)
