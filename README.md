# 计算器
完成软件工程作业专用

演示视频为演示视频.mp4

同时上传百度网盘：演示视频.mp4
链接: https://pan.baidu.com/s/1xDQB_Qib_obzBCKVMCcLkQ 提取码: 7nkt

夸克网盘：
链接：https://pan.quark.cn/s/8a10c7681cd6

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

# 版本1.1
修复加法器网页端不能在运算的到结果后恢复“计算”按钮显示的bug，原因为将局部参数当做全局参数调用。
为项目代码加入报错机制，以适应错误信息输入时及时应对，防止系统由于接收错误信息而崩溃。
在python代码中，引用try语句判断：

 try:
 
        num1 = float(num1)
        
        num2 = float(num2)
        
    except ValueError:
    
        return jsonify({'error': '输入必须是数字'}), 400
        
在HTML代码中，结合try和if语句：

try {

        const num1 = parseFloat(document.getElementById('num1').value);
        
        const num2 = parseFloat(document.getElementById('num2').value);
        
        
        if (isNaN(num1) || isNaN(num2)) 
        
        {
        
            throw new Error('请输入有效的数字');
            
        }

  在接收信息时，如果出现通信异常，则显示:
  
    if (!response.ok) 
    
    {
    
            throw new Error(`服务器错误: ${response.status}`);
            
    }


# 版本1.2
新增接口乘法。
针对python代码：

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

将返回值进行统一处理，改为result

HTML代码：新增按键乘法：

<button type="button" id="multiplyButton"
    
    class="group relative w-full flex justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-lg 
    
    text-white bg-gradient-to-r from-accent to-secondary hover:from-accent/90 hover:to-secondary/90 focus:outline-none focus:ring-2 
    
    focus:ring-offset-2 focus:ring-primary transition-all duration-300 transform hover:-translate-y-1">
    
    <span class="absolute inset-y-0 left-0 flex items-center pl-3">
    
        <i class="fa fa-times-circle group-hover:translate-x-1 transition-transform duration-300"></i>
        
    </span>
    
    乘法计算
    
</button>

# 版本1.3

原始版本对于新设备会出现URL不适配的问题，现对其进行修复工作。
连接问题修复：
问题1：后端服务器未启动或端口冲突
原因：如果 Flask 服务器没有运行，或者运行在不同的端口上，前端请求会失败

对app.py进行以下修改：

    from flask import Flask, render_template, request, jsonify

    from flask_cors import CORS  # 新增导入

    app = Flask(__name__)

    CORS(app)  # 启用 CORS

问题2：前端请求 URL 错误
原因：JavaScript 代码中请求的 URL 可能与后端路由不匹配。
确保前端代码中的 URL 与后端路由一致，代码修改如下：
    
    # 修改 performCalculation 函数中的 URL
    
    fetch(`http://localhost:5000${url}`, { ... })

调整后的代码：
    
    from flask import Flask, render_template, request, jsonify
    
    from flask_cors import CORS  # 新增导入
    
    app = Flask(__name__)
    
    CORS(app)  # 启用 CORS
    
    @app.route('/')
    
    def index():
        
        return render_template('index.html')
    
    @app.route('/add', methods=['POST'])
   
    def add_numbers():
        
        data = request.get_json()
        
        num1 = data.get('num1', 0)
        
        num2 = data.get('num2', 0)
        
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
        
        try:
            num1 = float(num1)
            
            num2 = float(num2)
        
        except ValueError:
            
            return jsonify({'error': '输入必须是数字'}), 400
        
        result = num1 * num2
        
        return jsonify({'result': result})
    
    if __name__ == '__main__':
       
        app.run(debug=True)



