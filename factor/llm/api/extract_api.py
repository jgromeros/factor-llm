import factor.llm_model.factorbedrock as factorbedrock
import factor.util.file_utils as file_utils
from flask import Blueprint, Flask, jsonify, request
import os
import tempfile

extract_api = Blueprint('extract_api', __name__)

@extract_api.route('/extract', methods=['POST'])
def extract():
    structure = request.form.get('structure')

    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and file_utils.allowed_file(file.filename):
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        file.save(temp_file.name)
        temp_file.close()

        result = factorbedrock.extract_data_from_pdf(temp_file.name, structure)

        os.remove(temp_file.name)
        return jsonify({'result': result}), 200
    else:
        return jsonify({'error': 'File type not allowed'}), 400
