from flask import Flask,request,jsonify
from flask_cors import CORS
import util
app=Flask(__name__)
CORS(app)
@app.route('/location_name')
def get_location_name():
    try:
        response = jsonify(util.get_location()) 
    except Exception as e:
        print("Error processing request:", e)
        response = jsonify({'error': 'Invalid input'})
    response.headers.add('Access-Control-Allow-Origin', '*') 
    return response

@app.route('/predict_home_price', methods=['POST'])
def price():
    data = request.get_json()
    print("Received data:", data)
    try:
        total_sqft = float(data.get('total_sqft', 0))
        location = data.get('location', '')
        bhk = int(data.get('bhk', 0))
        bath = int(data.get('bath', 0))
        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
        print("Calculated price:", estimated_price)
        response = jsonify({'price': estimated_price})
    except Exception as e:
        print("Error processing request:", e)
        response = jsonify({'error': 'Invalid input'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__=="__main__":
    util.load_saved_artifects()
    app.run(debug=True)