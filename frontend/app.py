from flask import Flask, render_template, jsonify
import datetime

app = Flask(__name__)

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