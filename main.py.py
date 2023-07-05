from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.picker import MDTimePicker
import datetime
from kivy.core.window import Window

KV =""" 
MDFloatLayout:
    md_Bg_color: 1, 1, 1, 1
    MDLabel:
        text: 'Cronometro'
        font_size: "30sp"
        pos_hint: {"center_y": .935}
        halign: "center"
        bold: True
    MDIconButton:
        icon: "plus"
        pos_hint:{"center_x": .87, "center_y": .14}
        md_bg_color: 0, 0, 0, 1
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
    MDLabel:
        id: cronometro_tiempo
        text: "00:00:00"
        post_hint: {"center_y": .5}
        halign: "center" 
        font_size: "30sp"  
        bold: True
    MDRaisedButton:
        text: "Stop"
        pos_hint: {"center_x": .2, "center_y": .4}
        on_release:
            app.stop_timer()
    MDRaisedButton:
        text: "Inicio"
        pos_hint: {"center_x": .8, "center_y": .4}
        on_release:
            app.start_timer()
    MDRaisedButton:
        text: "Pausa"
        pos_hint: {"center_x": .5, "center_y": .4}
        on_release:
            app.pause_timer()


"""

class Cronometro(MDApp):

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Red'
        self.paused = False
        self.time = datetime.datetime(1, 1, 1)
        
        
        
        return Builder.load_string(KV)
    
    def update_time(self, nap):
        if not self.paused:
            self.time = self.time + datetime.timedelta(seconds=1)
            
            self.root.ids.cronometro_tiempo.text = str(self.time.strftime("%H:%M:%S"))
    
    def stop_timer(self):
        self.paused = True
        self.time = datetime.datetime(1, 1, 1)
        self.root.ids.cronometro_tiempo.text = str("00:00:00")
        Clock.unschedule(self.update_time)
    
    def start_timer(self):
        self.paused = False
        Clock.schedule_interval(self.update_time, 1)
    
    def pause_timer(self):
        self.paused = True
        Clock.unschedule(self.update_time)

Cronometro().run()