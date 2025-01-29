# ResuMe (Resume Classification)

## Project Description

ResuMe is a web-based application developed as a final project for the Certified Internship and Independent Study Program (MSIB) "Artificial Intelligence 4 Jobs" at Orbit Future Academy. This application utilizes the Naïve Bayes algorithm to classify resumes into specific divisions, assisting Human Resources (HR) teams in the candidate selection process.

## Goals

- Develop practical skills in the field of Artificial Intelligence (AI).
- Implement a resume classification model using an AI-based approach.
- Improve efficiency and accuracy in the candidate selection process.
  
## Technologies Used

- **Python:** The primary programming language.
- Flask: A web framework for building the application.
- Naïve Bayes: The main algorithm for resume classification.
- NLTK: For text preprocessing.
- TF-IDF: For text feature extraction.
- Ngrok: For public network access.

## Key Features

- **Resume Upload:** Users can upload resumes in PDF format.
- **Automatic Classification:** Resumes are categorized into six divisions:
  - Business Development
  - Digital Media
  - Engineering
  - Human Resource
  - Sales
- **Model Evaluation:** Using Confusion Matrix, Precision, Recall, and F1-Score.
- **Web-Based Interface:** A user-friendly interface built with Flask.

## Installation and Usage

1. **Clone Repository**
   ```bash
   git clone https://github.com/username/resume-classification.git
   cd resume-classification
   ```
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Application**
   ```bash
   python app.py
   ```
4. **Use Ngrok for Public Access**
   ```bash
   ngrok http 5000
   ```
5. **Access the Application**
   Open a browser and visit http://127.0.0.1:5000 or use the URL provided by Ngrok.

## Dataset

The dataset used is sourced from Kaggle, consisting of 677 entries across six resume categories.

## Model Evaluation
- Model Accuracy: 83%
- Confusion Matrix: Used to assess classification performance.
- Evaluation Metrics: Precision, Recall, and F1-Score.

## Developer

Ahmad Muyaqi
Universitas Negeri Semarang

## Contact
For any inquiries or suggestions, feel free to contact LinkedIn: https://www.linkedin.com/in/ahmadmuyaqi/.

