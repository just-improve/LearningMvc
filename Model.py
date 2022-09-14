class Model:
    def __init__(self):
        self.value = ''
        self.previous_value = ''
        self.operator = ''

    def calculate(self, caption):
        print(f'button {caption}  clicked in model')
        if caption == 'C':
            self.previous_value = ''
            self.value = ''
            self.operator = ''

        elif caption == '+/-':
            self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value

        elif caption == '%':
            pass

        elif caption == '=':
            self.value = str(self._evaluate())

        elif caption == '.':
            if not caption in self.value:
                self.value += caption

        elif isinstance(caption, int):
            self.value += str(caption)

        else:
            if self.value:
                self.operator = caption
                self.previous_value = self.value
                self.value=''

        return self.value

    def _evaluate(self):
        return eval(self.previous_value+self.operator+self.value)

    def return_label(self, label):
        return label
