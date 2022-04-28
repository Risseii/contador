from flask import Flask,render_template,request,redirect,session
app = Flask(__name__)

app.secret_key = "llave super secreta"

@app.route('/')
def counter():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 1
    return render_template('index.html')

@app.route('/destroy_session')
def eliminate():
    session.clear()
    return redirect('/')

@app.route('/double')
def counter2():
    if "count" not in session: 
        session["count"] = 0
    else:
        session["count"] += 2
    return render_template('index.html')

@app.route('/suma',methods = ['POST'])
def suma():
    print(request.form)
    session['suma'] = int(request.form["cuentac1"]) + session["count"]
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)