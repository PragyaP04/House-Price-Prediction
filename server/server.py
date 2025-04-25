from flask import Flask, request, jsonify, render_template
import util  # Import the util module

# Configure Flask to serve static files and templates
app = Flask(__name__, static_folder='../static', template_folder='../static')

@app.route('/')
def home():
    return render_template('index.html')  # Serve the HTML file

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    try:
        response = jsonify({
            'locations': util.get_location_names()
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        print("Request received:", request.get_json())  # Debugging log
        data = request.get_json()
        total_sqft = float(data['total_sqft'])
        location = data['location']
        bhk = int(data['bhk'])
        bath = int(data['bath'])

        response = jsonify({
            'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except KeyError as e:
        return jsonify({'error': f'Missing parameter: {str(e)}'}), 400
    except ValueError as e:
        return jsonify({'error': f'Invalid parameter value: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)  # Enable debug mode for better error messages during development