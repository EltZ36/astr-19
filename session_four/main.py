class fish:

    def __init__(self):
        self.arms = 0.0
        self.legs = 0.0
        self.eyes = 2
        self.tail = True
        self.furry = False

    def print(self):
        print(f"A fish has {self.arms} arms.")
        print(f"A fish has {self.legs} legs.")
        print(f"A fish has {self.eyes} eyes.")
        print(f"It is {self.tail} that a fish has a tail.")
        print(f"It is {self.furry} that a fish is furry.")


def main():
    dave = fish()
    dave.print()

if (__name__ == "__main__"):
    main()