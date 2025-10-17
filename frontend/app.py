import os
import subprocess
import tempfile
import json
from flask import Flask, request, jsonify, render_template, send_file
import werkzeug
import pathlib

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

def run_import_linter(file_path, config_path=None):
    """
    Run import-linter on the specified directory
    """
    
    try:

        if not os.path.exists(file_path):
            return {
                'success': False,
                'output': '',
                'error': f'File or directory does not exist: {file_path}',
                'returncode': -1
            }

        # cd into uploads/projectdir
        os.chdir(app.config['UPLOAD_FOLDER'] + file_path)

        # build command
        cmd = ['lint-imports']
        
        # run import-linter
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30  # 30 second timeout
        )


        # returl results
        return {
            'success': result.returncode == 0,
            'output': result.stdout,
            'error': result.stderr,
            'returncode': result.returncode
        }
        
    # err - timeout    
    except subprocess.TimeoutExpired:
        return {
            'success': False,
            'output': '',
            'error': 'import-linter analysis timed out after 30 seconds',
            'returncode': -1
        }
        
    # err - general
    except Exception as e:
        return {
            'success': False,
            'output': '',
            'error': f'Error running import-linter: {str(e)}',
            'returncode': -1
        }


# main endpoint
@app.route('/')
def index():
    return render_template('index.html')


# health endpoint
@app.route('/health', methods=['GET', 'POST'])
def health_check():
    return jsonify({'status': 'healthy', 'timestamp': datetime.datetime.now().isoformat()})

if __name__ == "__main__":
    app.run(debug=True)