from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to this flask course bestk course</h1></html>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=="POST":
        name=request.form['fname']
        return f"Hello {name}"
    else:
        return render_template('form.html')
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    return render_template('result.html',result=res)


if __name__=="__main__":
    app.run(debug=True)