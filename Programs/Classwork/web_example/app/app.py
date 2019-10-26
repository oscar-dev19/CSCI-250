from flask import Flask
from datetime import datetime

app = Flask(__name__) # underlines are called dunder(double underlines)

@app.route('/') #@'s are declerators.
def index():
    return "Hello World!"


@app.route('/date')
def date():
    now = datetime.now() # current date and time
    time = now.strftime("%Y:%H:%M:%S")
    return time


@app.route('/oscar')
def look():
    return "Look Ma! I'm a web dev now!"

@app.route('/lunch')
def eat():
    html = '''
    <html>
        <title> Oscar's Lunch </title>
        <body>
            <h2>I had a beer and a delicous sandwich! :D</h2>
            <img src="https://video-images.vice.com/articles/5d72a63cd412b700085a3d79/lede/1567794750599-GettyImages-684133728.jpeg?crop=1xw:0.84375xh;center,center&resize=700:*"
        </body>
    </html>
    '''
    return html

@app.route('/siraj')
def lame_rap():
    return "Hello World its Siraj heres a pathetic rap song about a paper I plagirized. :)"


if __name__=='__main__':
    app.run()
