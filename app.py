# app.py
from flask import Flask, render_template, request, send_file
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_excel():
    # Get file from the form
    uploaded_file = request.files['file']
    output_filename = request.form['output_filename']

    # Read Excel file
    df = pd.read_excel(uploaded_file)

    # Rearrange columns and add new columns
    df = df.rename(columns={'EMP CODE': 'Emp Code', 'NAME': 'Emp Name', 'DESIGNATION CODE': 'DesignationId', 'PF DAYS': 'Paid Days', 'ΤΟΤΑL': 'OT Days', 'OT HRS':'OT Hrs'})
    df['Weekly offs'] = 0
    df['Absent'] = 0
    df['Total Days'] = 0
    df['Night Attandance'] = 0
    df['KM'] = 0
    df['IsCL'] = 0
    df['CLDays'] = 0
    df['Availed Leave'] = 0
    df['Arrear_Amt'] = 0
    df['Sno'] = range(1, len(df) + 1)
    df['EmpCode'] = 'MS00' + df['Emp Code'].astype(str)

    # Reorder columns
    new_order = ['Sno', 'EmpCode', 'Emp Name', 'DesignationId', 'Paid Days', 'OT Days', 'Weekly offs', 'Absent', 'Total Days', 'Night Attandance', 'OT Hrs', 'KM', 'IsCL', 'CLDays', 'Availed Leave', 'Arrear_Amt']
    df = df[new_order]

    # Save the processed DataFrame to a new Excel file
    output_path = f"output/{output_filename}.xlsx"
    df.to_excel(output_path, index=False)

    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
