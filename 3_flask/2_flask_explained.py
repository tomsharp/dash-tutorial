''' SIMPLE FLASK APP '''


''' import the Class '''
# flask is the framework here, while Flask is a Python class datatype.
from flask import Flask    


''' instantiate the Class'''
# once we import Flask, we need to create an instance of the Flask class for our web app.
# __name__ is a special variable that gets as value the string "__main__" when you’re executing the script.
# using "app" is an arbitrary convention, but be consistent.
app = Flask(__name__)      


''' define a function '''
# This line is a function decorator, mapping the function follows to localhost:5000/my_app
@app.route('/')
def hello_world():
    return 'Hello, World!'


''' execute '''
# This is only true when the script is executed. If it is imported, it will be false.
# Prints out possible Python errors on the web page helping us trace the errors. Only use in Dev, not Prod.
if __name__ == '__main__':  
    app.run()     


# Source: https://pythonhow.com/how-a-flask-app-works/
