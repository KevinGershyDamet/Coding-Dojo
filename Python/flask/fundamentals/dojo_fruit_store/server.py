from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    total_frutas = int(request.form['apple']) + int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['blackberry'])
    from datetime import datetime
    momento = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return render_template("checkout.html", respuestas = request.form, total_frutas = total_frutas, momento = momento)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    