from flask import Flask, render_template, send_from_directory
import subprocess
import os
from datetime import datetime
import pytz

app = Flask(__name__)

def get_top_output():
    try:
        result = subprocess.run(['top', '-b', '-n', '1'], capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/')
def home():
    return "Flask is running! <a href='/htop'>Go to htop endpoint</a>"

@app.route('/htop')
def htop():
    name = "Piyush Agrawal"
    username = os.getenv('USER', 'codespace')
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')
    top_output = get_top_output()
    
    return render_template('htop.html', 
                         name=name,
                         user=username,
                         server_time=server_time,
                         top_output=top_output)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                              'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)