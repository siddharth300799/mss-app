import pandas as pd
import streamlit as st

def process_excel(uploaded_file, output_filename):
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

    return output_path

def main():
    st.title("Excel Processor")

    uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])
    if uploaded_file is not None:
        output_filename = st.text_input("Enter output filename (without extension):")

        if st.button("Process"):
            output_path = process_excel(uploaded_file, output_filename)
            st.success(f"File processed successfully. [Download processed file]({output_path})")

if __name__ == '__main__':
    main()
