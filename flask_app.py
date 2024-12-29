from flask import Flask, render_template, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-script', methods=['GET'])
def run_script():
    try:
        # Call the Selenium script
        os.system('python selenium_script.py')  # Ensure 'selenium_script.py' is in the correct path
        return "Script executed successfully. Check the database for results!"
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
