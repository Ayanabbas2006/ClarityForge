from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from screens.HomeScreen import HomeScreen
#from screens.add_ritual import AddRitualScreen


class ClarityForge(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette="Blue"
        
        sm=MDScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        #sm.add_widget(AddRitualScreen(name='add_ritual'))
        sm.current='home'
        return sm
    
if __name__ == '__main__':
    ClarityForge().run()