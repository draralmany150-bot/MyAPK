from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        layout.add_widget(Label(
            text="مرحباً بك في تطبيقي",
            font_size=26
        ))

        button = Button(
            text="اختبار التطبيق",
            font_size=22
        )
        button.bind(on_press=self.test)
        layout.add_widget(button)

        return layout

    def test(self, instance):
        instance.text = "التطبيق يعمل بنجاح!"

MyApp().run()
