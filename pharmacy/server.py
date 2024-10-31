from flask import Flask, send_from_directory, jsonify, request
import os

app = Flask(__name__)

# Serve index.html from the pharmacy directory
@app.route('/')
def index():
    return send_from_directory('pharmacy', 'pindex.html')

# Serve static images from the 'images' folder
@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('images', filename)

# Endpoint to handle medicine order submissions
@app.route('/submit_order', methods=['POST'])
def submit_order():
    # Retrieve order details from the request
    data = request.json
    name = data.get('name')
    address = data.get('address')
    phone = data.get('phone')
    order_summary = data.get('order_summary')
    total_bill = data.get('total_bill')

    # Print the submitted details to the console for confirmation
    print("Received Order Details:")
    print(f"Name: {name}")
    print(f"Address: {address}")
    print(f"Phone: {phone}")
    print(f"Order Summary: {order_summary}")
    print(f"Total Bill: Rs {total_bill}")

    # Response message to be sent back to the client
    response_message = (
        f"<h2>Order Summary:</h2>"
        f"<p>{order_summary}</p>"
        f"<p>Total Bill: Rs {total_bill}</p>"
        f"<p>Customer Name: {name}</p>"
        f"<p>Address: {address}</p>"
        f"<p>Phone: {phone}</p>"
    )

    return jsonify({"message": response_message})

# Example endpoint to get available medicines (dummy data)
@app.route('/api/medicines', methods=['GET'])
def get_medicines():
    # In a real application, this data would come from a database
    medicines = [
        {"id": 1, "name": "Paracetamol", "price": 10},
        {"id": 2, "name": "Ibuprofen", "price": 20},
        {"id": 3, "name": "Amoxicillin", "price": 30},
    ]
    return jsonify(medicines)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
