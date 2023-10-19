def f(x):
    return x**3 + 8

def main():
    x = 9
    print(f'The result is {f(x)}')
    if(f(x) > 27):
        print("YAY!")

if(__name__ == "__main__"):
    main()