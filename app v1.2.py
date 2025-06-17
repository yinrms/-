from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    num1 = data.get('num1', 0)
    num2 = data.get('num2', 0)
    
    # 验证输入是否为数字
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return jsonify({'error': '输入必须是数字'}), 400
    
    result = num1 + num2
    return jsonify({'result': result})

@app.route('/multiply', methods=['POST'])
def multiply_numbers():
    data = request.get_json()
    num1 = data.get('num1', 0)
    num2 = data.get('num2', 0)
    
    # 验证输入是否为数字
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return jsonify({'error': '输入必须是数字'}), 400
    
    result = num1 * num2
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)    
