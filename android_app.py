
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView
from kivymd.uix.card import MDCard

# إنشاء الشاشة الرئيسية
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # التخطيط الرئيسي
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)

        # عنوان التطبيق
        title = MDLabel(
            text="تطبيقي الحديث",
            halign="center",
            theme_text_color="Primary",
            font_style="H4",
            size_hint_y=None,
            height=80
        )
        layout.add_widget(title)

        # حقل إدخال النص
        self.text_input = MDTextField(
            hint_text="أدخل النص هنا",
            size_hint_y=None,
            height=50,
            font_size=16
        )
        layout.add_widget(self.text_input)

        # زر المعالجة
        process_button = MDRaisedButton(
            text="معالجة النص",
            size_hint_y=None,
            height=50,
            font_size=16,
            on_release=self.process_text
        )
        layout.add_widget(process_button)

        # بطاقة عرض النتيجة
        result_card = MDCard(
            orientation='vertical',
            padding=10,
            spacing=10,
            size_hint_y=None,
            height=200,
            radius=[10, 10, 10, 10],
            elevation=3
        )

        # عنوان النتيجة
        result_title = MDLabel(
            text="النتيجة:",
            theme_text_color="Secondary",
            font_style="Subtitle1",
            size_hint_y=None,
            height=30
        )
        result_card.add_widget(result_title)

        # نص النتيجة
        self.result_text = MDLabel(
            text="",
            theme_text_color="Primary",
            size_hint_y=None,
            height=120,
            text_size=(None, 120)
        )
        result_card.add_widget(self.result_text)

        # إضافة البطاقة إلى التخطيط الرئيسي
        layout.add_widget(result_card)

        # إضافة التخطيط إلى الشاشة
        self.add_widget(layout)

    def معالجة_النص(self, instance):
        input_text = self.text_input.text
        self.result_text.text = f"تم معالجة النص: {input_text.upper()}"

# إنشاء مدير الشاشات
class MyApp(App):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        return sm

# تشغيل التطبيق
if __name__ == '__main__':
    MyApp().run()
