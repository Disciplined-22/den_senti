from flask import Flask, render_template, request, redirect, url_for, send_file
from main import extract_data_from_url
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    custom_title_selector = 'h1'  # Example: 'h1.title'
    custom_text_div_class = 'td-post-content'  # Example: 'content'

    def generate_assign_id(num):
        return f"{num:01d}"

    def generate_assign_counter():
        i = 1
        def counter():
            nonlocal i
            result = generate_assign_id(i)
            i += 1
            return result
        return counter

    counter_func = generate_assign_counter()

    url = request.form['url']
    classes_to_try = request.form['classes_to_try'].split(',')
    assign_id_2 = counter_func()

    extract_data_from_url(url, classes_to_try, assign_id_2, title_selector=custom_title_selector)

    return redirect(url_for('result'))



@app.route('/download')
def download():
    excel_path = 'files/output_1/Output Data Structure.xlsx'  # Ensure this matches the actual file name
    return send_file(excel_path, as_attachment=True)



 


@app.route('/result')
def result():
    excel_path = 'files/output_1/Output Data Structure.xlsx'  # Ensure this matches the actual file name
    try:
        if excel_path:
            if os.path.exists(excel_path):
                df = pd.read_excel(excel_path)
                return render_template('result.html', excel_path=excel_path, df=df)
            else:
                print("Excel file does not exist")
                
    except Exception as e:
        print("Error occurred:", e)
        



if __name__ == '__main__':
    app.run(debug=True)
