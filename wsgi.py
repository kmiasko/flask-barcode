from flask import Flask, request, make_response, render_template, redirect
from lib.barcode_generator import generate_barcode

application = app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/generuj', methods=['POST'])
def barcode():
    barcode = ''
    if request.method == 'POST':
        barcode = request.form.get('barcode', '')
        if barcode and len(barcode) == 16 and int(barcode):
            resp = make_response(generate_barcode(barcode))
            resp.content_type = "image/svg+xml"
            return resp
        else:
            return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
