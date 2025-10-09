from flask import Flask, jsonify, request
import tempfile
import model.factorbedrock as factorbedrock
import os

ALLOWED_EXTENSIONS = {'pdf', 'txt', 'jpg', 'png', 'jpeg'}

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/extract', methods=['POST'])
def extract():
    structure = request.form.get('structure')

    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        file.save(temp_file.name)
        temp_file.close()

        result = factorbedrock.extract_data_from_pdf(temp_file.name, structure)

        os.remove(temp_file.name)
        return jsonify({'result': result}), 200
    else:
        return jsonify({'error': 'File type not allowed'}), 400

if __name__ == '__main__':
    app.run()
