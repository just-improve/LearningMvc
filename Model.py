class Model:
    def __init__(self):
        self.value = ''

    def calculate(self, caption):
        print(f'button {caption}  clicked in model')
        if caption == 'C':
            self.value = ''

        elif caption == '+/-':
            self.value = self.value + caption

        elif isinstance(caption, int):
            self.value += str(caption)

        return self.value
