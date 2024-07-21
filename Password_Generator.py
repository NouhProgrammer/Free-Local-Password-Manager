class Generator:
    @classmethod
    def generate(self):
        import random
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = random.randint(8, 12)
        nr_numbers = random.randint(2, 5)
        nr_symbols = random.randint(2, 5)

        list_char = [letters[random.randint(0,51)]]
        while len(list_char) < (nr_letters-nr_numbers-nr_symbols):
          list_char.append(letters[random.randint(0,51)])
        while len(list_char) < (nr_letters-nr_numbers):
          list_char.append(numbers[random.randint(0,9)])
        while len(list_char) < (nr_letters):
          list_char.append(symbols[random.randint(0,8)])

        random.shuffle(list_char)
        password = ''.join(list_char)
        return password