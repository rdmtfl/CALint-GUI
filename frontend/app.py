from flask import Flask, render_template, jsonify
import datetime

app = Flask(__name__)

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