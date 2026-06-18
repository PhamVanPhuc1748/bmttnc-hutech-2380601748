import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import requests
from ui.vigenere import Ui_MainWindow 

class VigenereApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Kết nối nút bấm
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Lỗi nhập liệu")
        msg.setText(message)
        msg.exec_()

    def validate_inputs(self, text, key):
        import re
        if not text.strip():
            self.show_error("LỖI: Văn bản không được để trống!")
            return False
        if not key.strip():
            self.show_error("LỖI: Từ khóa không được để trống!")
            return False
        if not re.fullmatch(r'[A-Za-z]+', key.strip()):
            self.show_error("LỖI: Từ khóa chỉ được chứa các chữ cái (không có số, khoảng trắng hay ký tự đặc biệt)!")
            return False
        return True

    def call_api_encrypt(self):
        plain_text = self.ui.txt_plain_text.toPlainText()
        key = self.ui.txt_key.toPlainText()
        if not self.validate_inputs(plain_text, key):
            return

        url = "http://127.0.0.1:5000/api/vigenere/encrypt"
        payload = {"plain_text": plain_text, "key": key}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher.setPlainText(data["encrypted_text"])
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
        key = self.ui.txt_key.toPlainText()
        if not self.validate_inputs(cipher_text, key):
            return

        url = "http://127.0.0.1:5000/api/vigenere/decrypt"
        payload = {"cipher_text": cipher_text, "key": key}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setPlainText(data["decrypted_text"])
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
    window = VigenereApp()
    window.show()
    sys.exit(app.exec_())