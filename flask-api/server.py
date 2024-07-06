# buatlah sebuah aplikasi flask yang terdiri dari beberapa kondisi berikut:
# 1. POST API dengan
#    - route: /sensor/data
#    - 2 buah data dummy (temperature, humidity, timestamp)
#    - simpan data tersebut ke dalam sebuah list dan tampilkan pesan "Data received!"
# 2. GET API dengan
#    - route: /sensor/data
#    - response: tampilkan seluruh data yang telah disimpan

from flask import Flask, request, jsonify

app = Flask(__name__)

data = [
    {
        'temperature': 25,
        'humidity': 80,
        'timestamp': '2021-01-01 12:00:00'
    },
    {
        'temperature': 26,
        'humidity': 85,
        'timestamp': '2021-01-01 12:01:00'
    }
]

@app.route('/sensor/data', methods=['POST'])
def post_data():
    temperature = request.json['temperature']
    humidity = request.json['humidity']
    timestamp = request.json['timestamp']
    data.append({
        'temperature': temperature,
        'humidity': humidity,
        'timestamp': timestamp
    })
    return 'Data received!', 200

@app.route('/sensor/data', methods=['GET'])
def get_data():
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)


