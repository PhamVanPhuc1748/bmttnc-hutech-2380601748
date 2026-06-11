import re

from cipher.playfair import PlayFairCipher
from cipher.railfence import RailFenceCipher
from cipher.vigenere import VigenereCipher
from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
app = Flask(__name__)


def json_error(message, status_code=400):
    return jsonify({'error': message}), status_code


def require_non_empty_text(value, field_name):
    if value is None or not str(value).strip():
        return f'{field_name} không được để trống'
    return None


def require_alpha_text(value, field_name, allow_space=False):
    pattern = r'^[A-Za-z ]+$' if allow_space else r'^[A-Za-z]+$'
    if value is None or not str(value).strip():
        return f'{field_name} không được để trống'
    if not re.fullmatch(pattern, str(value)):
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

caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods = ["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    error = require_non_empty_text(plain_text, 'plain_text')
    if error:
        return json_error(error)

    key, error = require_int_in_range(data.get('key'), 'key', 1, 25)
    if error:
        return json_error(error)

    encrypt_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypt_text})

@app.route("/api/caesar/decrypt", methods = ["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    error = require_non_empty_text(cipher_text, 'cipher_text')
    if error:
        return json_error(error)

    key, error = require_int_in_range(data.get('key'), 'key', 1, 25)
    if error:
        return json_error(error)

    decrypt_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypt_text})

vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods = ['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    error = require_non_empty_text(plain_text, 'plain_text')
    if error:
        return json_error(error)

    error = require_alpha_text(key, 'key')
    if error:
        return json_error(error)

    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods = ['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    error = require_non_empty_text(cipher_text, 'cipher_text')
    if error:
        return json_error(error)

    error = require_alpha_text(key, 'key')
    if error:
        return json_error(error)

    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods = ['POST'])
def encrypt():
    data = request.json
    plain_text = data['plain_text']
    error = require_non_empty_text(plain_text, 'plain_text')
    if error:
        return json_error(error)

    key, error = require_int_in_range(data.get('key'), 'key', 2, 20)
    if error:
        return json_error(error)

    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods = ['POST'])
def decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    error = require_non_empty_text(cipher_text, 'cipher_text')
    if error:
        return json_error(error)

    key, error = require_int_in_range(data.get('key'), 'key', 2, 20)
    if error:
        return json_error(error)

    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# PLAYFAIR CIPHER ALGORITHM
playfair_cipher = PlayFairCipher()

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.json
    key = data['key']
    error = require_alpha_text(key, 'key')
    if error:
        return json_error(error)

    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    error = require_alpha_text(plain_text, 'plain_text')
    if error:
        return json_error(error)

    error = require_alpha_text(key, 'key')
    if error:
        return json_error(error)

    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({
        'encrypted_text': encrypted_text,
        'matrix': playfair_matrix
        })

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    error = require_alpha_text(cipher_text, 'cipher_text')
    if error:
        return json_error(error)

    error = require_alpha_text(key, 'key')
    if error:
        return json_error(error)

    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({
        'decrypted_text': decrypted_text,
        'matrix': playfair_matrix
    })

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)
     