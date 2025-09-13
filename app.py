# app.py
from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define a function to perform your Python logic
def get_data_from_python():
    """
    This is where your Python logic goes.
    It returns data that will be used in the HTML.
    """
    a = 2000
    b = 21
    result = a + b
    return f"a = {a}<br>b = {b}<br>a + b = {result}"

# Define a route to handle requests to the homepage
@app.route('/')
def home():
    # Call your Python function to get the data
    python_output = get_data_from_python()
    
    # Render the HTML template and pass the data to it
    return render_template('index.html', python_data=python_output)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
