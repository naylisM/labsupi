import sys
import random

def gen_random_list(l_len, min_rn, max_rn):
    return random.sample(range(min_rn, max_rn), l_len)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('Incorrect input!\nWhen starting the program, you should specify the array length (int, positive), minimum and maximum random numbers (int).\n\nExample of program launch:\npython zadanie1_variant12.py 7 10 20')
    else:
        list_length = int(sys.argv[1])
        min_random_number = int(sys.argv[2])
        max_random_number = int(sys.argv[3])
        my_list = gen_random_list(list_length, min_random_number, max_random_number)
        print_list(my_list)