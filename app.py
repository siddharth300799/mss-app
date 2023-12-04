# app.py
import streamlit as st
import pandas as pd

def process_excel(file):
    df = pd.read_excel(file)

    # Placeholder for your data processing logic
    # Replace this with your actual logic for renaming columns, adding new columns, etc.

    # Renaming columns
    df = df.rename(columns={'EMP CODE': 'Emp Code', 'NAME': 'Emp Name', 'DESIGNATION CODE': 'DesignationId', 'PF DAYS': 'Paid Days', 'ΤΟΤΑL': 'Total'})

    # Adding new columns
    df['Weekly offs'] = ''
    df['Absent'] = ''
    df['Total Days'] = ''
    df['Night Attandance'] = ''
    df['OT Days'] = ''
    df['OT Hrs'] = ''
    df['KM'] = ''
    df['IsCL'] = ''
    df['CLDays'] = ''
    df['Availed Leave'] = ''
    df['Arrear_Amt'] = ''
    df['Sno'] = range(1, len(df) + 1)
    df['EmpCode'] = 'MS00' + df['Emp Code'].astype(str)

    # Reordering columns
    new_order = ['Sno', 'EmpCode', 'Emp Name', 'DesignationId', 'Paid Days', 'OT Days', 'Weekly offs', 'Absent', 'Total Days', 'Night Attandance', 'OT Hrs', 'KM', 'IsCL', 'CLDays', 'Availed Leave', 'Arrear_Amt']
    df = df[new_order]

    # Save the processed DataFrame to a new Excel file
    output_path = "output/output_file.xlsx"
    df.to_excel(output_path, index=False)

    return output_path

def main():
    st.title("Excel Processor")

    uploaded_file = st.file_uploader("Choose Excel file:", type=["xls", "xlsx"])
    if uploaded_file:
        output_filename = st.text_input("Output File Name:")
        if st.button("Process and Download"):
            output_path = process_excel(uploaded_file)
            st.success("File processed successfully!")

            # Provide a link to download the processed file
            st.markdown(f"Download your file [here](sandbox:/mnt/data/{output_path})")

if __name__ == "__main__":
    main()
