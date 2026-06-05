from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.playfair import PlayfairCipher
from cipher.railfence import RailFenceCipher
from cipher.vigenere import VigeneraCipher

app = Flask(__name__)

# Khởi tạo các class mã hóa
caesar_cipher = CaesarCipher()
playfair_cipher = PlayfairCipher()
railfence_cipher = RailFenceCipher()
vigenere_cipher = VigeneraCipher()

# ==========================================
# GIAO DIỆN (UI ROUTES)
# ==========================================
@app.route("/")
def home(): return render_template('index.html')

@app.route("/caesar")
def caesar(): return render_template('caesar.html')

@app.route("/playfair")
def playfair(): return render_template('playfair.html')

@app.route("/railfence")
def railfence(): return render_template('railfence.html')

@app.route("/vigenere")
def vigenere(): return render_template('vigenere.html')

# ==========================================
# XỬ LÝ CAESAR
# ==========================================
@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    return caesar_cipher.encrypt_text(text, key)

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    return caesar_cipher.decrypt_text(text, key)

# ==========================================
# XỬ LÝ PLAYFAIR
# ==========================================
@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    matrix = playfair_cipher.create_playfair_matrix(key)
    return playfair_cipher.playfair_encrypt(text, matrix)

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    matrix = playfair_cipher.create_playfair_matrix(key)
    return playfair_cipher.playfair_decrypt(text, matrix)

# ==========================================
# XỬ LÝ RAIL FENCE
# ==========================================
@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    return railfence_cipher.rail_fence_encrypt(text, key)

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    return railfence_cipher.rail_fence_decrypt(text, key)

# ==========================================
# XỬ LÝ VIGENERE
# ==========================================
@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    return vigenere_cipher.vigenere_encrypt(text, key)

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    return vigenere_cipher.vigenere_decrypt(text, key)

if __name__ == "__main__":
    # Cổng 5050 như huynh đã chọn
    app.run(host="0.0.0.0", port=5050, debug=True)