from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the appointment form
@app.route('/')
def appointment_form():
    return render_template('appointment.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_appointment():
    # Get form data
    name = request.form.get('name')
    gender = request.form.get('gender')
    age = request.form.get('age')
    blood_group = request.form.get('bloodGroup')
    dob = request.form.get('dob')
    problem = request.form.get('problem')
    phone = request.form.get('phone')
    whatsapp = request.form.get('whatsapp')
    address = request.form.get('address')

    # Here you can add code to save this data to a database or send an email, etc.

    # Redirect to appointment confirmation page
    return redirect(url_for('submission_success'))

# Route for the success page
@app.route('/success')
def submission_success():
    return render_template('success.html')

if __name__ == '__main__':
    # Run the application
    app.run(host='0.0.0.0', port=10000)
