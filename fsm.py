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
        return text.lower() == "精彩剪輯"
	
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
        return text.lower() == "歌曲推薦"
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
        play = ['https://www.youtube.com/watch?v=iFyheD71V6o', 'https://www.youtube.com/watch?v=r8RONH5c9xQ', 'https://www.youtube.com/watch?v=W-HA3H-rAkU', 'https://www.youtube.com/watch?v=5akZH9FMf7w', 'https://www.youtube.com/watch?v=qYCLA-JLdiw', 'https://www.youtube.com/watch?v=odwYUElukyI','https://www.youtube.com/watch?v=_XTOy1bgCJE','https://www.youtube.com/watch?v=_tr8lIOrXuY','https://www.youtube.com/watch?v=Ou0YKPOdM6M','https://www.youtube.com/watch?v=1flIXnij65w']
        reply_token = event.reply_token
        send_text_message(reply_token, play[random.randint(0,9)])
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
        send_text_message(reply_token, "https://www.youtube.com/watch?v=zdQuBGxpZyc")
        self.go_back()

    def on_exit_state4(self):
        print("Leaving state4")

    def on_enter_state5(self, event):
        print("I'm entering state5")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=dInzAWptnYU")
        self.go_back()

    def on_exit_state5(self):
        print("Leaving state5")

    def on_enter_state6(self, event):
        print("I'm entering state6")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://youtu.be/aOmGchxlap0")
        self.go_back()

    def on_exit_state6(self):
        print("Leaving state6")

    def on_enter_state7(self, event):
        print("I'm entering state7")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=NHTsG0PI7yA")
        self.go_back()


    def on_exit_state7(self):
        print("Leaving state7")

    def on_enter_state8(self, event):
        print("I'm entering state8")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=_I3DqlX1LJI")
        self.go_back()

    def on_exit_state8(self):
        print("Leaving state8")

    def on_enter_state9(self, event):
        print("I'm entering state9")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=FpNvId-mqVA")
        self.go_back()

    def on_exit_state9(self):
        print("Leaving state9")

    def on_enter_state10(self, event):
        print("I'm entering state10")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=1xlaSudqSZY")
        self.go_back()

    def on_exit_state10(self):
        print("Leaving state10")

    def on_enter_state11(self, event):
        print("I'm entering state11")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=VTvwE5lSXRc")
        self.go_back()

    def on_exit_state11(self):
        print("Leaving state11")

    def on_enter_state12(self, event):
        print("I'm entering state12")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=VUwiEmBuROA")
        self.go_back()

    def on_exit_state12(self):
        print("Leaving state12")

    def on_enter_state13(self, event):
        print("I'm entering state13")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/watch?v=Vh_etwp0MOo&t=16s")
        self.go_back()

    def on_exit_state13(self):
        print("Leaving state13")

    def on_enter_state14(self, event):
        print("I'm entering state14")
        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入以下可行指令 : \n主場 \n精彩剪輯 \n介紹 \n24 \n32 \n77 \n64 \n68 \n39 \n31 \n5 \n66 \n12 \n幫助 \nfsm \n歌曲推薦 \nug")
        
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
        music = ['https://www.youtube.com/watch?v=bfHV4tmAhg4','https://www.youtube.com/watch?v=I4Mes83cCYU&list=RDCMUC1tHuRanhZ8i4fEKSNhhNJQ&index=2','https://www.youtube.com/watch?v=gxzBmvQoE6k&list=RDCMUC1tHuRanhZ8i4fEKSNhhNJQ&index=4','https://www.youtube.com/watch?v=AeLWAkbGUhc','https://www.youtube.com/watch?v=UjXLH5byv7U','https://www.youtube.com/watch?v=QzHVkSBylPQ','https://www.youtube.com/watch?v=5UQv4oQttA0','https://www.youtube.com/watch?v=6c2O6qVabhk']
        reply_token = event.reply_token
        send_text_message(reply_token, music[random.randint(0,7)])
        self.go_back()

    def on_exit_state16(self):
        print("Leaving state16")

    def on_enter_state17(self, event):
        print("I'm entering state17 ")
        members = ['https://www.instagram.com/nini.lin_022/?fbclid=IwAR3p_WoOeeyfs4vDEzOAYPH3WtTUPCEwbVzHIUOSBRi9I2wVzmGrz7Medh4', 'https://www.instagram.com/yukiii_min/?utm_medium=copy_link&fbclid=IwAR0CxLE9-9eAryBKgw2tZZK49w4AH_2euOVKxpImMJmTgxSuR4J620gcb_c', 'https://www.instagram.com/___yovia___/?utm_medium=copy_link&fbclid=IwAR3p_WoOeeyfs4vDEzOAYPH3WtTUPCEwbVzHIUOSBRi9I2wVzmGrz7Medh4', 'https://www.instagram.com/djeminatw/?utm_medium=copy_link&fbclid=IwAR0NvafF2j1lhmdZT_FWQxeFVh3FtlsocGLJ3IWjU_X097q9GmqlGYWSd7M', 'https://www.instagram.com/mia_712/?utm_medium=copy_link&fbclid=IwAR34a_2R37LVV3H7WZYqOiikm5O_EIIPFLL7NrlVdtR_bv3odNWd6my4FJk', 'https://www.instagram.com/han.yang830/?utm_medium=copy_link&fbclid=IwAR3p_WoOeeyfs4vDEzOAYPH3WtTUPCEwbVzHIUOSBRi9I2wVzmGrz7Medh4' ,'https://www.instagram.com/wenziofficial/?utm_medium=copy_link&fbclid=IwAR3RAAWR2YIL5ymRDbBA1RbZl0lJsSVpndFOb1h2APYBMo5QlPW2hMr6EMo' ,'https://www.instagram.com/yimanping/?utm_medium=copy_link&fbclid=IwAR10OSBpgX0fD9MelI2a-DFjNeuPZF0Br8r1EB0ain84wzw8wENXFaYHe4c','https://www.instagram.com/jane.duu.88/?utm_medium=copy_link&fbclid=IwAR2bXJM_6_mjjqIuUbJq-L5Yjjhjok4tA-BxrGHXpWxl37pLerG0aASpiyc','https://www.instagram.com/shihshih_sawmah/?utm_medium=copy_link&fbclid=IwAR3dD3Ay8_8e7EVi-ogBcAzVrH3RQXSvy-9K_ey-01JsoQHCtNkB-4WKEwQ','https://www.instagram.com/__seul777/?utm_medium=copy_link&fbclid=IwAR0kW84gVHk3QVlETwBq7iw-hts5SsKBe8Aw83-2_VFwp0JrBTCt7z6czbQ','https://www.instagram.com/joy_lee.91/?utm_medium=copy_link&fbclid=IwAR1rmoj4SPwi-Suj03yO4vGuL-WiyiFq7w3I0Hca9ZthFl1GJ87eyUtZmGo','https://www.instagram.com/rouyi113/?utm_medium=copy_link&fbclid=IwAR3dD3Ay8_8e7EVi-ogBcAzVrH3RQXSvy-9K_ey-01JsoQHCtNkB-4WKEwQ','https://www.instagram.com/_maggie_chen/?utm_medium=copy_link&fbclid=IwAR2A67PJdReCri3vKlIY1Z7nCjmVcVQc7yYWcuJNnWwfOcE2YafCkoxTTlI','https://www.instagram.com/minnieeee106/?utm_medium=copy_link&fbclid=IwAR2N6tGe54v0w36_LEtPjAx6Gjpf0RkZo20GVzWH7CNEaui0mhSkHKeQsTs','https://www.instagram.com/feichi1124/?utm_medium=copy_link&fbclid=IwAR34a_2R37LVV3H7WZYqOiikm5O_EIIPFLL7NrlVdtR_bv3odNWd6my4FJk']
        reply_token = event.reply_token
        send_text_message(reply_token, members[random.randint(0,15)])
        self.go_back()


    def on_exit_state17(self):
        print("Leaving state17")