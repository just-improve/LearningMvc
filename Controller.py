from Model import Model
from View import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.main()

    # w tej metodzie przekazać parametry ze wszystkich pól uzupełnionych. Nie wywoływać metody model tylko po prostu zacząć robić pętlę
    def on_button_click(self, caption):
        result = self.model.calculate(caption)
        self.view.value_var.set(result)

    def on_button(self):
        print("button clicked")


if __name__ == '__main__':
    print("if main")
    calculator = Controller()
    calculator.main()
    print("dasdsas")

