from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def hello_world():
    # Return a simple "Hello, World!" message
    return 'Hello, World!'

# Run the app
if __name__ == '__main__':
    app.run(debug=True)