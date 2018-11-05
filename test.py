#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.core.audio import SoundLoader

energy = 100
hours = 4


class Hello(FloatLayout):
    def __init__(self, **kwargs):
        super(Hello, self).__init__(**kwargs)

        self.name_label = Label(
            text="CatchPhrase Pt-Br",
            size_hint=(.1, .15),
            pos_hint={'x': .45, 'y': .9}
        )
        self.main_label = Label(
            text="Clique em Começar",
            size_hint=(1, .55),
            pos_hint={'x': 0, 'y': .35}
        )

        # Main Buttons
        self.pass_button = Button(
            text="Acertou?! Clique aqui!",
            size_hint=(.3, .1),
            pos_hint={'x': .35, 'y': .2},
            on_press=self.next_word
        )
        self.start_button = Button(
            text="Começar",
            size_hint=(.3, .1),
            pos_hint={'x': .35, 'y': .7},
            on_press=self.start_sound
        )
        self.add_widget(self.main_label)
        self.add_widget(self.pass_button)
        self.add_widget(self.name_label)
        self.add_widget(self.start_button)
        with open('./pt_BR.txt', encoding='latin-1') as f:
            self.words = f.readlines()

    def next_word(self, event):
        index = random.randint(0, len(self.words))
        self.main_label.text = self.words[index].strip().split('/')[0]

    def start_sound(self, event):
        self.timer = SoundLoader.load('./cartoon001.wav')
        self.timer.play()


class app1(App):
    def build(self):
        return Hello()


if __name__ == "__main__":
    app1().run()
