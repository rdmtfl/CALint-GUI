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


def create_caling_config(directory_path: str) -> str:
    # json file structure
    config_calint = {
        "roots": ["calint"],
        "main": ["calint.main", 0],
        "frameworks": ["calint.frameworks", 1],
        "adapters": ["calint.adapters", 2],
        "use_cases": ["calint.use_cases", 3],
        "entities": ["calint.entities", 4]
    }

    try:
        # convert to path
        Path(directory_path).mkdir(parents=True, exist_ok=True)
        dir_path = Path(directory_path) / 'calint.json'

        # write json file        
        with open(dir_path, 'w', encoding='utf-8') as f:
            json.dump(config_calint, f, indent=4)

    except Exception as e:
        return {
            "sucess": False,
            "error": str(e),
            "message": "Failed to create calint configuration file"
        }


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
        os.chdir(app.config['UPLOAD_FOLDER'] + '/import-linter-example-main') # testing only
        #os.chdir(app.config['UPLOAD_FOLDER'] + file_path)

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

@app.route('/analyze/directory', methods=['POST'])
def analyze_directory():
    """
    Analyze a directory structure using import-linter with config file
    """

    # check if post request has zip project
    if 'directory' not in request.files:
        return jsonify({'error': 'No directory archive provided'}), 400
    
    # get dir and conf files
    directory_file = request.files['directory']
    config_file = request.files.get('config')
    
    # create temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        try:
            # extract and save dir files
            if directory_file.filename.endswith('.zip'):
                import zipfile
                zip_path = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded.zip')
                directory_file.save(zip_path)
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(app.config['UPLOAD_FOLDER'])
                analysis_path = temp_dir
            else:
                return jsonify({'error': 'Not a zip file'}), 400

            # save config file
            config_path = None
            if config_file and allowed_file(config_file.filename):
                config_filename = werkzeug.utils.secure_filename(config_file.filename)
                config_path = os.path.join(app.config['UPLOAD_FOLDER'], config_filename)
                config_file.save(config_path)

            # run import-linter
            result = run_import_linter(analysis_path, config_path)
            
            return jsonify(result)

        # err - general    
        except Exception as e:
            return jsonify({
                'success': False,
                'output': '',
                'error': f'Error processing directory: {str(e)}',
                'returncode': -1
            })


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