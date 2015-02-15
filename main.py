from kivy.app import App
from kivy.uix.button import Button


class Team812(App):
    """
    Team812 app base class
    """

    def build(self):
        return Button(text='Hello from Team 812')


if __name__ == '__main__':
    app = Team812()
    app.run()
