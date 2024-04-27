import os
import pandas as pd
import requests
import json

def send_data_to_api(patient_data, api_key):
    api_endpoint = "https://api.openai.com/v1/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
        "OpenAI-Organization": "Please Enter Your Organization Name Here",
        "OpenAI-Project": "Please Enter Your Project Name Here"
    }
    data = {
        "model": "gpt-3.5-turbo",  # Specify the model you want to use
        "prompt": json.dumps(patient_data),
        "temperature": 0.7,  # Adjust temperature for diversity
        "max_tokens": 150  # Adjust max_tokens based on desired response length
    }
    response = requests.post(api_endpoint, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.text)
        return None

def main():
    # Read patient data from Excel file
    file_path = input("Enter the path to the Excel file: ")
    api_key = os.environ.get('OPENAI_API_KEY')  # Retrieve API key from environment variable
    if api_key is None:
        print("Error: OPENAI_API_KEY environment variable is not set.")
        return

    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        print("Error reading Excel file:", e)
        return

    # Process each row of the DataFrame
    for index, row in df.iterrows():
        # Create patient data dictionary
        patient_data = {
            "PatientID": row["PatientID"],
            "Name": row["Name"],
            "Age": row["Age"],
            "Gender": row["Gender"],
            "Ethnicity": row["Ethnicity"],
            "MedicalHistory": row["Medical History"],
            "Medications": row["Medications"],
            "Allergies": row["Allergies"],
            "LabResults": row["Lab Results"],
            "Diagnosis": row["Diagnosis"],
            "Procedures": row["Procedures"],
            "VisitDate": row["Visit Date"],
            "PhysicianNotes": row["Physician Notes"]
        }

        # Send patient data to API
        api_response = send_data_to_api(patient_data, api_key)

        if api_response:
            print(f"Patient ID: {row['PatientID']}, Clinical analysis recommendation:")
            print(api_response['choices'][0]['text'])
            print()

if __name__ == "__main__":
    main()
