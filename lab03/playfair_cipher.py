import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from ui.playfair import Ui_MainWindow 
import requests

class PlayfairApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Kết nối sự kiện click của nút bấm với hàm xử lý
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        # Đổi URL API sang playfair
        url = "http://127.0.0.1:5000/api/playfair/encrypt"
        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                print("Dữ liệu API trả về:", data)
                self.ui.txt_cipher.setPlainText(data["encrypted_text"])
                
                if "matrix" in data:
                    self.display_matrix(data["matrix"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print(f"Error while calling API: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def call_api_decrypt(self):
        # Đổi URL API sang playfair
        url = "http://127.0.0.1:5000/api/playfair/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipher.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setPlainText(data["decrypted_text"])

                # Cập nhật ma trận lên bảng nếu API có trả về
                if "matrix" in data:
                    self.display_matrix(data["matrix"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print(f"Error while calling API: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    # --- Hàm hỗ trợ hiển thị ma trận khóa 5x5 lên giao diện ---
    def display_matrix(self, matrix):
        """
        Giả sử API trả về matrix là một mảng 2 chiều 5x5.
        Ví dụ: [['P', 'L', 'A', 'Y', 'F'], ['I', 'R', 'B', 'C', 'D'], ...]
        """
        for row in range(5):
            for col in range(5):
                # Tạo item cho từng ô và đưa vào bảng
                item = QTableWidgetItem(str(matrix[row][col]))
                self.ui.table_playfair.setItem(row, col, item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlayfairApp()
    window.show()
    sys.exit(app.exec_())