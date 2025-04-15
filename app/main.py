from flask import Flask, jsonify, request
from datetime import datetime, timezone

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    
    # Returns current UTC timestamp and client IP in JSON format.

    return jsonify({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "ip": request.headers.get('X-Forwarded-For', request.remote_addr)
    })

if __name__ == '__main__':
    # Run the app on 0.0.0.0 to be accessible inside Docker
    app.run(host='0.0.0.0', port=8080)