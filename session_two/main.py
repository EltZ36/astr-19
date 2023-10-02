def numbers_output():
    int_x = 3
    int_y = 5
    float_x = 3.0
    float_y = 5.0 

    float_sum = float_x + float_y
    int_diff = int_x - int_y
    float_product = float_x / float_y

    print(float_sum)
    print(type(float_sum))
    print(int_diff)
    print(type(int_diff))
    print(float_product)
    print(type(float_product))

    return None

def main():
    numbers_output()
    return None

if(__name__ == '__main__'):
    main()