import re

from flask import Flask, render_template, request

# Import các class xử lý mã hóa
from cipher.caesar import CaesarCipher
from cipher.playfair import PlayFairCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher

app = Flask(__name__)


def render_validation_error(message, status_code=400):
    return render_template('error.html', error_message=message), status_code


def require_non_empty_text(value, field_name):
    if value is None or not value.strip():
        return f'{field_name} không được để trống'
    return None


def require_alpha_text(value, field_name, allow_space=False):
    pattern = r'^[A-Za-z ]+$' if allow_space else r'^[A-Za-z]+$'
    if value is None or not value.strip():
        return f'{field_name} không được để trống'
    if not re.fullmatch(pattern, value):
        suffix = 'chữ cái và khoảng trắng' if allow_space else 'chỉ chứa chữ cái'
        return f'{field_name} phải {suffix}'
    return None


def require_int_in_range(value, field_name, min_value, max_value):
    try:
        number = int(value)
    except (TypeError, ValueError):
        return None, f'{field_name} phải là số nguyên'

    if number < min_value or number > max_value:
        return None, f'{field_name} phải nằm trong khoảng {min_value} đến {max_value}'

    return number, None

# ==================== HOME PAGE ====================
@app.route("/")
def home():
    return render_template('index.html')

# ==================== CAESAR CIPHER ====================
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    error = require_non_empty_text(text, 'Văn bản gốc')
    if error:
        return render_validation_error(error)

    key, error = require_int_in_range(request.form.get('inputKeyPlain'), 'Khóa Caesar', 1, 25)
    if error:
        return render_validation_error(error)

    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    
    return render_template('result.html', 
                           cipher_type="Caesar Cipher",
                           action_type="Encryption",
                           input_text=text, 
                           key=key, 
                           output_text=encrypted_text)

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    error = require_non_empty_text(text, 'Văn bản mã hóa')
    if error:
        return render_validation_error(error)

    key, error = require_int_in_range(request.form.get('inputKeyCipher'), 'Khóa Caesar', 1, 25)
    if error:
        return render_validation_error(error)

    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    
    return render_template('result.html', 
                           cipher_type="Caesar Cipher",
                           action_type="Decryption",
                           input_text=text, 
                           key=key, 
                           output_text=decrypted_text)

# ==================== PLAYFAIR CIPHER ====================
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/encrypt_playfair", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain'] 

    error = require_alpha_text(text, 'Văn bản gốc Playfair')
    if error:
        return render_validation_error(error)

    error = require_alpha_text(key, 'Khóa Playfair')
    if error:
        return render_validation_error(error)
    
    Playfair = PlayFairCipher()
    matrix = Playfair.create_playfair_matrix(key)
    encrypted_text = Playfair.playfair_encrypt(text, matrix)
    
    return render_template('result.html', 
                           cipher_type="Playfair Cipher",
                           action_type="Encryption",
                           input_text=text, 
                           key=key, 
                           output_text=encrypted_text,
                           matrix=matrix) # Thêm dòng này để gửi ma trận sang web

@app.route("/decrypt_playfair", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']

    error = require_alpha_text(text, 'Văn bản mã hóa Playfair')
    if error:
        return render_validation_error(error)

    error = require_alpha_text(key, 'Khóa Playfair')
    if error:
        return render_validation_error(error)
    
    Playfair = PlayFairCipher()
    matrix = Playfair.create_playfair_matrix(key)
    decrypted_text = Playfair.playfair_decrypt(text, matrix)
    
    return render_template('result.html', 
                           cipher_type="Playfair Cipher",
                           action_type="Decryption",
                           input_text=text, 
                           key=key, 
                           output_text=decrypted_text,
                           matrix=matrix)

# ==================== VIGENERE CIPHER ====================
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/encrypt_vigenere", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']

    error = require_non_empty_text(text, 'Văn bản gốc')
    if error:
        return render_validation_error(error)

    error = require_alpha_text(key, 'Khóa Vigenère')
    if error:
        return render_validation_error(error)

    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.vigenere_encrypt(text, key)
    
    return render_template('result.html', 
                           cipher_type="Vigenère Cipher",
                           action_type="Encryption",
                           input_text=text, 
                           key=key, 
                           output_text=encrypted_text)

@app.route("/decrypt_vigenere", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']

    error = require_non_empty_text(text, 'Văn bản mã hóa')
    if error:
        return render_validation_error(error)

    error = require_alpha_text(key, 'Khóa Vigenère')
    if error:
        return render_validation_error(error)

    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.vigenere_decrypt(text, key)
    
    return render_template('result.html', 
                           cipher_type="Vigenère Cipher",
                           action_type="Decryption",
                           input_text=text, 
                           key=key, 
                           output_text=decrypted_text)

# ==================== RAIL FENCE CIPHER ====================
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/encrypt_railfence", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    error = require_non_empty_text(text, 'Văn bản gốc')
    if error:
        return render_validation_error(error)

    key, error = require_int_in_range(request.form.get('inputKeyPlain'), 'Khóa Rail Fence', 2, 100)
    if error:
        return render_validation_error(error)

    if key >= len(text):
        return render_validation_error("Số đường ray (Khóa) phải nhỏ hơn độ dài của văn bản để mã hóa có hiệu lực.")

    RailFence = RailFenceCipher()
    encrypted_text = RailFence.rail_fence_encrypt(text, key)
    
    return render_template('result.html', 
                           cipher_type="Rail Fence Cipher",
                           action_type="Encryption",
                           input_text=text, 
                           key=key, 
                           output_text=encrypted_text)

@app.route("/decrypt_railfence", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    error = require_non_empty_text(text, 'Văn bản mã hóa')
    if error:
        return render_validation_error(error)

    key, error = require_int_in_range(request.form.get('inputKeyCipher'), 'Khóa Rail Fence', 2, 100)
    if error:
        return render_validation_error(error)

    if key >= len(text):
        return render_validation_error("Số đường ray (Khóa) phải nhỏ hơn độ dài của bản mã để giải mã có hiệu lực.")

    RailFence = RailFenceCipher()
    decrypted_text = RailFence.rail_fence_decrypt(text, key)
    
    return render_template('result.html', 
                           cipher_type="Rail Fence Cipher",
                           action_type="Decryption",
                           input_text=text, 
                           key=key, 
                           output_text=decrypted_text)

# ==================== MAIN ====================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)