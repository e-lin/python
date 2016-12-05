#
# Factory Pattern
# Reference:
# http://blog.jobbole.com/62023/
#

class Button():
    html = ""
    def get_html(self):
        return self.html

class Image(Button):
    html = "<img alt="" />"

class Input(Button):
    html = "<input type=\"text\" \>"

class Flash(Button):
    html = "<...>"


#factory method pattern
class ButtonFactory():
    def create_button(self, typ):
        targetclass = typ.capitalize()
        return globals()[targetclass]()

def main():
    button_obj = ButtonFactory()
    buttons = ['image', 'Input', 'flash']

    for b in buttons:
        print button_obj.create_button(b).get_html()

#print 'image'.capitalize()
#print globals()
main()
