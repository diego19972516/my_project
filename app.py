from flask import Flask, render_template, request
from knn import classify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify_data():
    if request.method == 'POST':
        x = int(request.form['inputX'])
        y = int(request.form['inputY'])
        result = classify(x, y)
        return render_template('result.html', Clasificar_x=result['Clasificar_x'], Clasificar_y=result['Clasificar_y'], result=result)

if __name__ == '__main__':
    app.run(debug=True)
