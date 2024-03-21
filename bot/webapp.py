# webapp.py
from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def webapp_index():
    user_data = request.args.get('user_data', default=None, type=str)
    return render_template('index.html', user_data=user_data)

@app.route('/get_level')
def get_level():
    user_data = request.args.get('user_data', default=None, type=str)
    if user_data:
        user_data = user_data.replace('\'', '\"')
        user_data = json.loads(user_data)

        user_level = user_data.get('user-lvl', None)
        if user_level:
            return jsonify(level=user_level)

    return jsonify(error=True)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)