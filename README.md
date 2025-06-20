# 计算器
完成软件工程作业专用

演示视频为演示视频.mp4

# 版本1.0
完成基本功能和接口对接，html文件将py文件作为api进行调用，在网页中调用py文件完成计算功能，返回计算结果到网页进行显示。
接口说明：
python文件接口：

@app.route('/')

def index():

    return render_template('index.html')
    
返回 index.html 页面，用于展示加法计算器的前端界面

@app.route('/add', methods=['POST'])

def add_numbers():

    data = request.get_json()
    
...

    return jsonify({'sum': result})
    
接收两个数字，将它们进行处理并返回结果。
前端HTML文件接口：

const response = await fetch('/add', {

                method: 'POST',
                
                headers: {
                
                    'Content-Type': 'application/json'
                    
                },
                
                body: JSON.stringify({
                
                    num1: num1,
                    
                    num2: num2
                    
                })
                
            });
            
使用 fetch API 向 /add 接口发送 POST 请求，将用户输入的数字作为 JSON 数据发送。
const data = await response.json();
将python文件回传的结果加载，以便后续显示结果。

