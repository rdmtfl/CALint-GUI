from flask import Flask, render_template, jsonify
import datetime
import os

app = Flask(__name__)

# configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'py', 'txt'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024 # 16MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# create dir if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
              filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# main endpoint
@app.route('/')
def index():
    return render_template('index.html')

# data endpoint
@app.route('/data', methods=['POST'])
def receive_data():
    # Simulate processing the received data
    response = {
        'message': 'data received successfully',
        'timestamp': datetime.datetime.now().isoformat()
    }
    return jsonify(response)

# health endpoint
@app.route('/health', methods=['GET', 'POST'])
def health_check():
    return jsonify({'status': 'healthy', 'timestamp': datetime.datetime.now().isoformat()})

if __name__ == "__main__":
    app.run(debug=True)