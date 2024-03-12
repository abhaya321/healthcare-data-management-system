from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_patient', methods=['POST'])
def add_patient():
    # Receive data from the frontend form
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    condition = request.form['condition']

    # Process the data (save to database, etc.)
    # For now, let's just return the received data
    return "Patient record added successfully: Name - {}, Age - {}, Gender - {}, Condition - {}".format(name, age, gender, condition)

@app.route('/search_patient', methods=['POST'])
def search_patient():
    # Receive data from the frontend form
    name = request.form['name']

    # Process the data (search in database, etc.)
    # For now, let's just return the received name
    return "Searching for patient with name: {}".format(name)

if __name__ == '__main__':
    app.run(debug=True)
