
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

class AdventureGame(App):

    def build(self):
        self.score = 0
        self.stage = 0

        self.root_layout = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=18
        )

        Window.clearcolor = (0.04, 0.05, 0.12, 1)

        self.title = Label(
            text="[b]PYTHON ADVENTURE[/b]",
            markup=True,
            font_size=30,
            color=(0.2, 0.8, 1, 1),
            size_hint=(1, 0.25)
        )

        self.story = Label(
            text="Welcome, Adventurer!\n\n"
                 "Your mysterious journey begins.\n"
                 "Are you ready?",
            font_size=19,
            halign="center"
        )

        self.score_label = Label(
            text="SCORE: 0",
            font_size=18,
            size_hint=(1, 0.15)
        )

        self.root_layout.add_widget(self.title)
        self.root_layout.add_widget(self.story)
        self.root_layout.add_widget(self.score_label)

        self.buttons = []

        for i in range(2):
            btn = Button(
                text="",
                font_size=18,
                size_hint=(1, 0.2),
                background_normal="",
                background_color=(0.1, 0.35, 0.65, 1)
            )
            btn.bind(on_press=self.choose)
            self.root_layout.add_widget(btn)
            self.buttons.append(btn)

        self.show_start()
        return self.root_layout

    def show_start(self):
        self.stage = 0
        self.story.text = (
            "You are standing before a mysterious forest.\n\n"
            "What will you do?"
        )
        self.set_buttons("Enter the forest", "Go home")

    def set_buttons(self, first, second):
        self.buttons[0].text = first
        self.buttons[1].text = second

    def choose(self, instance):
        choice = instance.text

        if self.stage == 0:
            if choice == "Enter the forest":
                self.score += 10
                self.stage = 1
                self.story.text = (
                    "You discovered a treasure chest!\n\n"
                    "What next?"
                )
                self.set_buttons("Open chest", "Walk away")
            else:
                self.finish("Adventure cancelled!")

        elif self.stage == 1:
            if choice == "Open chest":
                self.score += 20
                self.finish("Amazing! You found the treasure!")
            else:
                self.finish("You missed the treasure!")

    def finish(self, message):
        self.stage = 2
        self.story.text = (
            message + "\n\n"
            "Your adventure is complete!"
        )
        self.score_label.text = f"SCORE: {self.score}"
        self.set_buttons("Play again", "Exit")

    def on_restart(self, instance):
        self.score = 0
        self.score_label.text = "SCORE: 0"
        self.show_start()

    def on_exit(self, instance):
        App.get_running_app().stop()

    def choose(self, instance):
        choice = instance.text

        if self.stage == 2:
            if choice == "Play again":
                self.on_restart(instance)
            else:
                self.on_exit(instance)
            return

        if self.stage == 0:
            if choice == "Enter the forest":
                self.score += 10
                self.stage = 1
                self.story.text = (
                    "You discovered a treasure chest!\n\n"
                    "What next?"
                )
                self.set_buttons("Open chest", "Walk away")
            else:
                self.finish("Adventure cancelled!")

        elif self.stage == 1:
            if choice == "Open chest":
                self.score += 20
                self.finish("Amazing! You found the treasure!")
            else:
                self.finish("You missed the treasure!")

        self.score_label.text = f"SCORE: {self.score}"


if __name__ == "__main__":
    AdventureGame().run()
                       
