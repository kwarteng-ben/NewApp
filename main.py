from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import random

quotes = [
    "Believe in yourself.",
    "Keep moving forward.",
    "Dream big, work hard.",
    "Stay positive, work hard, make it happen."
]

class QuotesApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=20)
        self.label = Label(text=random.choice(quotes), font_size=24)
        self.button = Button(text="New Quote", size_hint=(1, 0.3), on_press=self.new_quote)

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button)
        return self.layout

    def new_quote(self, instance):
        self.label.text = random.choice(quotes)

if __name__ == "__main__":
    QuotesApp().run()
