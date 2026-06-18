import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Lỗi nhập liệu")
        msg.setText(message)
        msg.exec_()

    def validate_inputs(self, text, key_str):
        if not text.strip():
            self.show_error("LỖI: Văn bản không được để trống!")
            return False
        try:
            key = int(key_str.strip())
        except ValueError:
            self.show_error("LỖI: Khóa K phải là một số nguyên!")
            return False
        if key < 1 or key > 25:
            self.show_error("LỖI: Khóa K phải nằm trong khoảng từ 1 đến 25!")
            return False
        return True

    def call_api_encrypt(self):
        plain_text = self.ui.txt_plain_text.toPlainText()
        key_str = self.ui.txt_key.toPlainText()
        if not self.validate_inputs(plain_text, key_str):
            return

        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {"plain_text": plain_text, "key": key_str}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher.setPlainText(data["encrypted_message"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                data = response.json()
                self.show_error(f"Lỗi từ server: {data.get('error', 'Không xác định')}")

        except requests.exceptions.RequestException as e:
            self.show_error(f"Không thể kết nối tới server:\n{str(e)}")

    def call_api_decrypt(self):
        cipher_text = self.ui.txt_cipher.toPlainText()
        key_str = self.ui.txt_key.toPlainText()
        if not self.validate_inputs(cipher_text, key_str):
            return

        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {"cipher_text": cipher_text, "key": key_str}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setPlainText(data["decrypted_message"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                data = response.json()
                self.show_error(f"Lỗi từ server: {data.get('error', 'Không xác định')}")

        except requests.exceptions.RequestException as e:
            self.show_error(f"Không thể kết nối tới server:\n{str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())