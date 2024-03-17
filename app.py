from flask import Flask, request, jsonify, render_template
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def download_video():
    if request.method == 'POST':
        url = request.form.get('url')
        try:
            download_folder = os.path.expanduser("~\Downloads")
            YouTube(url).streams.first().download(output_path=download_folder)
            return jsonify({'message': 'Video downloaded successfully'}), 200
        except Exception as e:
            return jsonify({'message': 'An error occurred', 'error': str(e)}), 400
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)