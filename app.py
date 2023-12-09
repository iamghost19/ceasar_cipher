from flask import Flask, render_template, request

app = Flask(__name__)

# Fungsi Caesar Cipher
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            shifted = ord(char) + shift_amount
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        text = request.form['text']
        shift = int(request.form['shift'])
        operation = request.form['operation']
        
        if operation == 'encrypt':
            shift_direction = request.form['shift_direction']
            if shift_direction == 'right':
                result = caesar_cipher(text, shift)
            elif shift_direction == 'left':
                result = caesar_cipher(text, -shift)  # Dekripsi dengan pergeseran negatif

        elif operation == 'decrypt':
            shift_direction = request.form['shift_direction']
            if shift_direction == 'right':
                result = caesar_cipher(text, -shift)  # Dekripsi dengan pergeseran negatif
            elif shift_direction == 'left':
                result = caesar_cipher(text, shift)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
