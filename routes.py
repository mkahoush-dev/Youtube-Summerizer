from flask import Flask, render_template, request, redirect, url_for
import Summarize
app = Flask(__name__)
ur = ''
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        u = []
        global ur
        ur = request.form["ur"]
        return redirect(url_for("url", url=u))
    else:
        return render_template('index.html')
@app.route('/<url>')
def url(url):
    global ur
    text = Summarize.transcribe(ur)
    return render_template('youtube.html', variable=text)

# https://www.youtube.com/watch?v=RmTxvkhzFPo
if __name__ == '__main__':
    app.run(debug=True)
