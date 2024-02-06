from flask import Flask, render_template
import yaml
# jinja2 (thymeleaf)
# flask 내에 자동으로 설치가 됨!

app = Flask(__name__)

# YAML 파일에서 설정 값을 읽어오기
with open('config.yml') as file:
    config = yaml.safe_load(file)

# 읽어온 설정 값을 앱에 적용하기
app.config.update(config)
myName = '소경학'
myId = 'godnes628'
myPassword = 'gyeonghak123'
password = '123123soso!'
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', test=app.config.get('name')['gyeonghak'])

if __name__ == '__main__':
    app.run(debug=True)