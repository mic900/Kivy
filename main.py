from kivy.base import runTouchApp
from kivy.core import text
from kivy.core.text import markup
from kivy.lang import Builder
from kivy.uix.behaviors import button
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd import images_path
from PIL import Image 


#########  ------------------------------- B o x l a y o u t ----------------------------------
# runTouchApp(Builder.load_string('''
# BoxLayout:
#     orientation: 'vertical'
#     padding:20
#     spacing:10

#     Button:
#         text:"b1"
#     Button:
#         text:"b2"
#         color:"orange"
#     Button:
#         text:"b3"
#         color:"blue"
# '''))
#########----------------------------------------------------------------------------    
#        ---------------------------------FLOAT LAYOUT                               
# runTouchApp(Builder.load_string('''
# <Button>:
#     font_size:30
#     size_hint: 0.2,0.3

# FloatLayout:
#     Button:
#         text:'f1'
#         pos_hint:{'top':1,'right':1}

#     Button:
#         text:'f2'
#         pos_hint:{'x':0,'left':1}
# '''))
#-------------------------------------------------------------------------------
####==================================Anchor Layout=======================================
# runTouchApp(Builder.load_string('''
# AnchorLayout:
#     anchor_x:'left'
#     anchor_y:
#     Button:
#         text:'outside'
#         size_hint:0.6,0.6

#     Button:
#         text:'in'
#         size_hint:0.1,0.1


# '''))
#----------------------------------------------------------------------------------
#================================ Grid Layout=====================================
# runTouchApp(Builder.load_string('''
# GridLayout:
#     cols:2
#     spacing:8
#     padding:100

#     Button:
#         text:'h1'
#     Button:
#         text:'h2'
#     Button:
#         text:'h3'
#     Button:
#         text:'h4'
#     Button:
#         text:'h5'
#     Button:
#         text:'h6'    
# '''))
#----------------------------------------------------------------------------------
#=======================  RelativeLayout   ================================
# runTouchApp(Builder.load_string('''
# RelativeLayout:
#     Button:
#         text:'r1'
#         size_hint:.2,.3
#         pos:20,40
#     Button:
#         text:'r2'    
#         size_hint:.2,.3
#         pos:40,80
#     Button:
#         text:'r3'
#         size_hint:.2,.3
#         pos:80,100

# '''))
#--------------------------------------------------------------------------------
#=======================================Stack Layout=====================
# runTouchApp(Builder.load_string('''
# StackLayout:
#     orientation:'lr-bt'
    

#     Button:
#         text:'one'
#         size_hint: .2,.2
#     Button:
#         text:'two'
#         size_hint: .2,.2
#     Button:
#         text:'three'
#         size_hint: .2,.2    
#     Button:
#         text:'four'
#         size_hint: .2,.2
#     Button:
#         text:'five'
#         size_hint: .2,.2
# '''))

#--------------------------------------------------------------------------------------
#==================================== Page Layout======================================
# runTouchApp(Builder.load_string('''
# PageLayout:
#     Label:
#         text:'page one'
#     Button:
#         text:'page two'
#     Label:
#         text:'page three'

# '''))
#=========================================================Label with stile============================
# class titl(App):
#     def build(self):
#         return Label(text='[color=3333ff][sup]hello[/sup][/color] mik!', markup=True,
#         font_size='20dp'  )
#         markup=True

# if __name__=='__main__':
#     titl().run()

#[color=333ff]word[/color]
#[sub][/sub]
#[sup][/sup]                  most important is insidr label'markup=True'
#==================================================================
#-----------------------------------------------------------------------------------------------
#-------------------------------------------Actiion Bar -----------------------------




class Launch(FloatLayout):
    im = Image.open(r"pi.jpg") 
    def __init__(self, **kwargs):
        super(Launch, self).__init__(**kwargs)

    def say_hello(self): 
        return self.im.show() 



class MyApp(App):


    def build(self):
        return Launch()



if __name__ == '__main__':
    MyApp().run()

     




