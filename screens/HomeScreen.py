from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from screens.get_theme import *
from kivymd.toast import toast
import smtplib,random
from screens import enc_dcr
from email.message import EmailMessage
from kivymd.app import MDApp
import threading
from kivy.clock import Clock


Home_screen_helper='''
<HomeScreen>:

    canvas.before:
        Color:
            rgba: root.theme_color
        Rectangle:
            size: self.size
            pos:  self.pos

    MDFloatLayout:
        MDLabel:
            text: f"[b]{root.theme_greet}[/b]"
            markup: True
            font_style: "H2"
            pos_hint: {'center_x':0.5,'y':0.4}
            halign: 'center'
            valign: 'middle'

        MDTextField:
            id: name
            mode: 'rectangle'
            hint_text: 'Name'
            icon_left: 'account'
            text_color_normal: 1,1,1,1
            text_color_focus: root.theme_text
            helper_text:'Write your first name!'
            helper_text_mode: 'on_focus'
            helper_text_color_focus: root.theme_text
            size_hint_y: None
            size_hint_x: 0.7
            pos_hint: {'center_x':0.5,'center_y': 0.7}
            height: 1
            icon_left_color_normal: 1, 1, 1, 1
            icon_left_color_focus: root.theme_text

        MDTextField:
            id: email
            mode: 'rectangle'
            fill_color: root.theme_color
            hint_text: 'Email'
            icon_left: 'email'
            text_color_normal: 1,1,1,1
            text_color_focus: root.theme_text
            helper_text:'Write your email!'
            helper_text_mode: 'on_focus'
            helper_text_color_focus: root.theme_text
            size_hint_y: None
            size_hint_x: 0.7
            pos_hint: {'center_x':0.5,'center_y': 0.57}
            height: 1
            icon_left_color_normal: 1, 1, 1, 1
            icon_left_color_focus: root.theme_text

        MDTextField:
            id: otp
            mode: 'rectangle'
            fill_color: root.theme_color
            hint_text: 'OTP'
            text_color_normal: 1,1,1,1
            text_color_focus: root.theme_text
            helper_text:'Enter OTP'
            icon_left: 'shield-key'
            size_hint_y: None
            size_hint_x: 0.3
            pos_hint: {'center_x':0.3,'center_y': 0.45}
            height: 1
            icon_left_color_normal: 1, 1, 1, 1
            icon_left_color_focus: root.theme_text
            on_text: root.check_otp()

        MDRaisedButton:
            id: send_button
            style: 'elevated'
            text: 'Send OTP '
            theme_bg_color: 'Custom'
            md_bg_color: root.theme_color
            pos_hint: {'center_x':0.6,'center_y':0.45}
            on_release: root.send_otp()

        MDLabel:
            id: reset_text
            text: f"Resend OTP in {root.count} seconds!"
            pos_hint: {'center_x':0.3,'center_y':12}
            halign: 'center'

        
'''
Builder.load_string(Home_screen_helper)

with open('/home/ayanabbas/Documents/Documents/Code/Python/ClarityForge/assets/app_pass.txt') as f:
    key=f.read()
key=str(enc_dcr.main_decrypt(key))
class HomeScreen(MDScreen):
    theme_color= theme()[0]
    theme_text= theme()[1]
    theme_greet= theme()[2]

    count=90
    def wait(self,tim=90):
        self.count=tim
        Clock.schedule_interval(self.update,1)

    def update(self,dt):
        if self.count>0:
            self.count-=1
            self.ids.reset_text.text=f"Resend OTP in {self.count} seconds!"
        else:
            self.ids.reset_text.pos_hint={'center_x':0.3,'center_y':12}
            Clock.unschedule(self.update)
            self.ids.send_button.disabled = False

    def check_otp(self):
        otp=self.ids.otp.text
        if len(otp)==6:
            try:
                if str(otp)==str(MDApp.get_running_app.number):
                    toast('Email Verified Successfully!')
                    print('Email Verified Successfully!')
                    if self.ids.send_button:
                        self.ids.send_button.disabled=True
                        self.ids.otp.disabled=True
                    self.ids.reset_text.pos_hint={'center_x':0.3,'center_y':12}
                    return
                toast('OTP incorrect!')
                print('OTP incorrect!')
            except:
                self.ids.send_button.disabled=False
                print("Trial mode")

    def send(self):
        print("Sending email")
        MDApp.get_running_app.number=random.randint(100000,999999)
        msg=EmailMessage()
        msg['Subject']=f'{MDApp.get_running_app.number} is your OTP!'
        msg['From']='ilovenothing007@gmail.com'
        msg['To']=self.ids.email.text
        msg.set_content(f'''Hello! {self.ids.name.text}, here is your OTP!
                        
Thanks for using ClarityForge, developed by Mojiz Abbas and team.Your OTP for registration is 
{MDApp.get_running_app.number}.

Regards,
Team ClarityForge''')

        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login('ilovenothing007@gmail.com',key)
            smtp.send_message(msg)
    def send_otp(self):
        self.ids.reset_text.pos_hint={'center_x':0.3,'center_y':0.35}
        self.wait(tim=60)
        self.ids.send_button.disabled=True
        t=threading.Thread(target=self.send).start()
        toast("OTP send to your email!")
        print("Send OTP pressed!")