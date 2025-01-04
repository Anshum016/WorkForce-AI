from flask import Flask, render_template, request, jsonify
from agent import get_agent_response
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/start')
def start():
    return render_template('start.html')

@app.route('/afterstart')
def afterstart():
    return render_template('afterstart.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        symbols = data.get('symbols', ['TSLA', 'NVDA'])  # Default symbols if none provided
        query = f"Get analyst recommendations and fundamentals for {', '.join(symbols)}"
        response = get_agent_response(query)
        return jsonify({'success': True, 'data': response})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/check')
def check_templates():
    templates_path = os.path.join(os.getcwd(), "templates")
    if os.path.exists(templates_path):
        return f"Templates folder found. Contents: {os.listdir(templates_path)}"
    else:
        return "Templates folder not found!"

if __name__ == '__main__':
    app.run(debug=True)
    from app import app

# This is important for Vercel
if __name__ == '__main__':
    app.run()