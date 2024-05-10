import os
import requests
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
# Define the index route
@app.route('/', methods=['GET', 'POST'])
def index():
   return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
   name = request.form['name']
   file = request.files['file']
   # Check if the file is a ZIP file
   if file and file.filename.endswith('.zip'):
      file_path = os.path.join('upload_folder', f'{name}.zip')
      file.save(file_path)
      url = check_plagiarism(name, file_path)
      print(f'Report URL: {url}')
      parsed_url = 'https://dolos.ugent.be/reports/' + name
      if url:
            return jsonify({'url': url, 'parsed_url': parsed_url})
      else:
            return jsonify({'error': 'An error occurred during the plagiarism check.'})
   else:
      return jsonify({'error': 'Please upload a ZIP file.'})

# Define the check_plagiarism function
def check_plagiarism(name, zipfile_path):
   try:
      response = requests.post(
            'https://dolos.ugent.be/api/reports',
            files={'dataset[zipfile]': open(zipfile_path, 'rb')},
            data={'dataset[name]': name}
      )
      json_data = response.json()
      if 'html_url' in json_data:
            return json_data['html_url']
      else:
            return None
   except Exception as e:
      print(f"Error during plagiarism check: {e}")
      return None

if __name__ == '__main__':
   app.run(debug=True)
