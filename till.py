import kivy
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button


class TillApp(App):
    pass


class MainBox(BoxLayout):
    pass


class TopBox(BoxLayout):
    pass


class MiddleBox(BoxLayout):
    pass


class LeftBox(BoxLayout):
    info_from_numbers = StringProperty("")


class NumbersGrid(GridLayout):
    def pressing_numbers(self, button_instance):
        # Access the text of the button that was pressed
        button_text = button_instance.text
        # Assign the numbers collection to the LeftBox class
        self.parent.info_from_numbers += button_text

    def up_button(self, button_instance):
        pass

    def down_button(self, button_instance):
        pass

    def clr_button(self, button_instance):
        self.parent.info_from_numbers = ""

    def esc_button(self, button_instance):
        pass

    def x_button(self, button_instance):
        pass

    def user_button(self, button_instance):
        pass

    def order_button(self, button_instance):
        pass

    def enter_button(self, button_instance):
        pass


class RightBox(BoxLayout):
    pass

class ProductsGrid(GridLayout):
    def pressing_product(self, button):
        app_root = self.parent.parent.parent  # As ProductsGrid is inside RightBox, which is inside the root widget (MainBox)
        left_box = app_root.ids.left_box  # Access the LeftBox using its ID
        left_box.ids.product_label.text = button.text  # Set the label text to the button's text


class RightButtonsBox(BoxLayout):
    pass


class OptionsGrid(GridLayout):
    pass


class BottomBox(BoxLayout):
    pass

"""
class ProductMenus(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(16):
            b2 = Button(text="product menus")
            self.add_widget(b2)

"""

TillApp().run()


