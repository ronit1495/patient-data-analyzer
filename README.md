# Clinical Analysis Recommendation System
## Overview
The Clinical Analysis Recommendation System is a Python application that utilizes the OpenAI GPT API to generate clinical analysis recommendations based on patient data. The application takes input data from an Excel spreadsheet containing patient information such as PatientID, Name, Age, Gender, Ethnicity, Medical History, Medications, Allergies, Lab Results, Diagnosis, Procedures, Visit Date, and Physician Notes. It then sends this data to the OpenAI GPT API, which generates clinical analysis recommendations based on the provided information.

## Features

* Read patient data from an Excel spreadsheet
* Send patient data to the OpenAI GPT API
* Receive clinical analysis recommendations from the API
* Display clinical analysis recommendations for each patient

## Prerequisites
Before running the application, make sure you have the following installed:

* Python 3.x
* pandas library (pip install pandas)
* requests library (pip install requests)

## Usage

1. Clone the repository to your local machine:

2. Navigate to the project directory:
    ```
    cd clinical-analysis-recommendation
    ```
3. Set up your OpenAI API key as an environment variable in your .zshrc file:
    ```
    export OPENAI_API_KEY="your-api-key"
    ```
4. Run the application:
    ```
    python main.py
    ```
6. Follow the prompts to enter the path to the Excel file containing patient data.

## Configuration
OpenAI API Key: You need to obtain an API key from OpenAI and set it as an environment variable named OPENAI_API_KEY. This key is required to authenticate requests to the OpenAI GPT API.
## Contributing
Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository
2. Create a new branch (git checkout -b feature/yourfeature)
3. Make your changes
4. Commit your changes (git commit -am 'Add new feature')
5. Push to the branch (git push origin feature/yourfeature)
6. Create a new Pull Request
