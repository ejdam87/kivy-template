from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainScreen(GridLayout):

    def __init__(self, **kwargs):

        super(MainScreen, self).__init__(**kwargs)

        self.cols = 1
        self.add_widget(Label(text='This template was created by Ejdam'))


        self.add_widget(Label(text='Text entry'))
        inpt = TextInput(multiline=False)
        self.add_widget(inpt)

        button = Button(text='Button text', font_size=14)
        button.bind(on_press=self.increment_clicks)

        self.add_widget(button)

        self.clicks = 0

        self.counter_show = Label(text=f"You clicked: {self.clicks} times")
        self.add_widget(self.counter_show)

    def increment_clicks(self, instance: Button):

        self.clicks += 1
        self.counter_show.text = f"You clicked: {self.clicks} times" 




class TemplateApp(App):

    def build(self):
        return MainScreen()


if __name__ == '__main__':
    TemplateApp().run()
