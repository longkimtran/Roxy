from PyQt5.QtGui import QTextCursor

MACHINE_NAME = "Roxie: "
MACHINE_WAITING_1 = "I'm hearing !"
MACHINE_WAITING_2 = "I'm waiting !"
MACHINE_KNOWING = "Who are you?"
MACHINE_CONTROL_BRIGHTNESS = "How many percent do you want to adjust the brightness, sir?"
MACHINE_TEMPERATURE = "You want to know where the temperature is?"
MACHINE_INFORMATION = "What are you looking for sir?"
MACHINE_ENTERTAINMENT = "How do you want to entertain?"
MACHINE_GAME = "What do you want game?"
MACHINE_HEALTH_CARE = "What do you need me to do sir?"
MACHINE_HEALTH_CARE_BMI = "Please follow step by step, sir!"
MACHINE_HEALTH_CARE_BMI_WEIGHT = "Please Enter your weight(kg), sir!"
MACHINE_HEALTH_CARE_BMI_HEIGHT = "Please Enter your height(meter), sir!"

MACHINE_WAITING_VN = "Tôi đang nghe !"
MACHINE_KNOWING_VN = "Vậy ngài là ai?"
MACHINE_CONTROL_BRIGHTNESS_VN = "Ngài muốn điều chỉnh độ sáng bao nhiêu phần trăm?"
MACHINE_TEMPERATURE_VN = "Ngài muốn nhiệt độ ở đâu?"
MACHINE_INFORMATION_VN = "Ngài muốn tìm gì à?"
MACHINE_ENTERTAINMENT_VN = "Ngài muốn giải trí như thế nào?"
MACHINE_GAME_VN = "Ngài muốn chơi trò chơi gì?"
MACHINE_HEALTH_CARE_VN = "Hôm nay ngài cần gì về sức khỏe?"
MACHINE_HEALTH_CARE_BMI_VN = "Xin vui lòng làm theo từng bước!"
MACHINE_HEALTH_CARE_BMI_WEIGHT_VN = "Vui lòng nhập số cân nặng của ngài(kg)"
MACHINE_HEALTH_CARE_BMI_HEIGHT_VN = "Vui lòng nhập chiều cao của ngài(kg)"

IS_RUNNING = False


def machine_text(self, text):
    print("Roxy: " + text)
    self.uic.Roxy_Talk.insertHtml(
        "<br><div style='text-align: left;border: 2px solid solid black;background-color: #D3D3D3;border-radius: 20%; "
        "padding-right: 10px;margin: 10px 0;'><span style='color: back;margin-top: 20'>" + text + "</span""></div>")
    self.uic.Roxy_Talk.moveCursor(QTextCursor.End)  # auto scroll cursor


def user_text(self, text):
    print("You: " + text)
    self.uic.Roxy_Talk.insertHtml(
        "<br><div style='text-align: right; border: 2px solid solid black;background-color: #FFA07A;border-radius: "
        "10px; "
        "padding: 10px;margin: 10px 0; '><span style='color: blue;margin-right: 20px'>" +
        text + "</span""></div>")
    self.uic.Roxy_Talk.moveCursor(QTextCursor.End)
