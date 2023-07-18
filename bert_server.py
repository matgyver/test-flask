from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process_json', methods=['POST'])
def process_json():
    data = request.get_json()  # Get JSON data from the request

    # Print the received JSON data
    print("Received JSON data:", data)

    # Process the JSON data
    # You can access specific fields using data['field_name']

    # Example response
    response = {'status': 'success', 'message': 'JSON data received'}
    return jsonify(response)

if __name__ == '__main__':
    app.run()
