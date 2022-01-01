from transitions.extensions import GraphMachine

from utils import send_text_message,send_button_message, send_image_url
import random

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "主場"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "歌曲推薦"
	
    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "介紹"
   
    def is_going_to_state4(self, event):
        text = event.message.text
        return text.lower() == "24"

    def is_going_to_state5(self, event):
        text = event.message.text
        return text.lower() == "32"

    def is_going_to_state6(self, event):
        text = event.message.text
        return text.lower() == "77"

    def is_going_to_state7(self, event):
        text = event.message.text
        return text.lower() == "64"

    def is_going_to_state8(self, event):
        text = event.message.text
        return text.lower() == "68"

    def is_going_to_state9(self, event):
        text = event.message.text
        return text.lower() == "39"

    def is_going_to_state10(self, event):
        text = event.message.text
        return text.lower() == "31"

    def is_going_to_state11(self, event):
        text = event.message.text
        return text.lower() == "5"

    def is_going_to_state12(self, event):
        text = event.message.text
        return text.lower() == "66"

    def is_going_to_state13(self, event):
        text = event.message.text
        return text.lower() == "12"
    def is_going_to_state14(self, event):
        text = event.message.text
        return text.lower() == "幫助"
    def is_going_to_state15(self, event):
        text = event.message.text
        return text.lower() == "fsm"
    def is_going_to_state16(self, event):
        text = event.message.text
        return text.lower() == "6"
    def is_going_to_state17(self, event):
        text = event.message.text
        return text.lower() == "ug"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "台南市立棒球場")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")
        music = ['https://www.youtube.com/watch?v=_NGQfFCFUn4', 'https://www.youtube.com/watch?v=GJ63esXbY-M&list=RDGJ63esXbY-M&start_radio=1', 'https://www.youtube.com/watch?v=hxQLe6nlUcA', 'https://www.youtube.com/watch?v=MPbUaIZAaeA', 'https://www.youtube.com/watch?v=pE49WK-oNjU', 'https://www.youtube.com/watch?v=L3_4OXQVNgc']
        reply_token = event.reply_token
        send_text_message(reply_token, music[random.randint(0,5)])
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")

    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_text_message(reply_token, "這是介紹台灣元老級球隊[統一獅]的互動式聊天機器人")
        self.go_back()

    def on_exit_state3(self):
        print("Leaving state3")

    
    def on_enter_state4(self, event):
        print("I'm entering state4")

        reply_token = event.reply_token
        send_image_url(reply_token, "https://cdn2.ettoday.net/images/5257/d5257051.jpg"+"https://attach.setn.com/newsimages/2021/04/01/3092474-PH.jpg")
        self.go_back()

    def on_exit_state4(self):
        print("Leaving state4")

    def on_enter_state5(self, event):
        print("I'm entering state5")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://youtu.be/gr2DjP6y1-k")
        self.go_back()

    def on_exit_state5(self):
        print("Leaving state5")

    def on_enter_state6(self, event):
        print("I'm entering state5")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://instagram.com/feichi1124?utm_medium=copy_link")
        self.go_back()

    def on_exit_state6(self):
        print("Leaving state6")

    def on_enter_state7(self, event):
        print("I'm entering state5")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://youtu.be/eZ9poBAcJUU")
        self.go_back()


    def on_exit_state7(self):
        print("Leaving state7")

    def on_enter_state8(self, event):
        print("I'm entering state8")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=GrAchTdepsU")
        self.go_back()

    def on_exit_state8(self):
        print("Leaving state8")

    def on_enter_state9(self, event):
        print("I'm entering state9")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=brTYTuromPY")
        self.go_back()

    def on_exit_state9(self):
        print("Leaving state9")

    def on_enter_state10(self, event):
        print("I'm entering state10")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=AN_R4pR1hck")
        self.go_back()

    def on_exit_state10(self):
        print("Leaving state10")

    def on_enter_state11(self, event):
        print("I'm entering state11")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=tcYodQoapMg")
        self.go_back()

    def on_exit_state11(self):
        print("Leaving state11")

    def on_enter_state12(self, event):
        print("I'm entering state12")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=gdZLi9oWNZg")
        self.go_back()

    def on_exit_state12(self):
        print("Leaving state12")

    def on_enter_state13(self, event):
        print("I'm entering state13")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://youtu.be/W1VnkIFKiFc")
        self.go_back()

    def on_exit_state13(self):
        print("Leaving state13")

    def on_enter_state14(self, event):
        print("I'm entering state14")
        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入以下可行指令 : 主場 歌曲推薦 介紹 24 32 77 64 68 39 31 5 66 12 幫助 fsm 6 ug")
        
        self.go_back()

    def on_exit_state14(self):
        print("Leaving state14")

    def on_enter_state15(self, event):
        print("I'm entering state15")
        reply_token = event.reply_token
        send_image_url(reply_token, "https://img.onl/XEYT6V")
        
        self.go_back()

    def on_exit_state15(self):
        print("Leaving state15")

    def on_enter_state16(self, event):
        print("I'm entering state16")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.instagram.com/p/CVeyJ6Ajr43/?utm_source=ig_web_copy_link")
        self.go_back()

    def on_exit_state16(self):
        print("Leaving state16")

    def on_enter_state17(self, event):
        print("I'm entering state17")

        reply_token = event.reply_token
        send_text_message(reply_token, "good bye my boy")
        self.go_back()

    def on_exit_state17(self):
        print("Leaving state17")