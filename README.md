# Resume-screening-app
Project Title: Intelligent Resume Screening Web App
Tools Used: Python, Streamlit, scikit-learn, NLTK, Pickle, HTML/CSS

In this project, I built a user-friendly resume screening web application that helps predict the most relevant job category for a given resume using Machine Learning. The idea was to automate and simplify the first-level resume screening process typically done by HR professionals.

The backend model was trained using real-world resume data across 25 job roles including Data Scientist, Java Developer, Civil Engineer, DevOps Engineer, and many more. I used Natural Language Processing (NLP) techniques like tokenization, stop word removal, and regular expression-based cleaning to prepare the resume text. After preprocessing, resumes were vectorized using TF-IDF and passed into a trained classification model (pickled for deployment).

On the frontend, I used Streamlit to create an interactive web interface. Users can upload resumes in .txt or .pdf format, and with just one click, the app processes the text, predicts the job category, and displays the result in a clean, attractive interface. To make it more engaging, I customized the UI with a visually appealing background image, added a glassmorphic content container, and ensured responsive design for better readability.

This project not only helped me understand how machine learning integrates with real-world business needs, but also gave me hands-on experience in full-stack ML deployment — from model building and file handling to UI styling and real-time prediction.

What I Learned:

1) Real-world NLP preprocessing for resumes

2) Using TF-IDF and classification models for text prediction

3) Deploying ML models with Streamlit

4) Customizing UI with embedded HTML/CSS in Streamlit

5) Handling text encoding issues in uploaded files

This application streamlines the resume screening process by using machine learning to categorize resumes. It's built with a combination of Streamlit for the front-end, Flask for the backend API, and a machine learning model (as developed in the provided notebook) for resume classification.

**Key Features:**

* **Resume Upload:** Users can upload resumes through a user-friendly Streamlit interface.
* **ML-Powered Categorization:** The uploaded resume is sent to a Flask API, where a pre-trained machine learning model classifies the resume into relevant categories (e.g., "Data Science," "Web Designing," "HR").
* **Category Display:** The predicted category is displayed on the Streamlit UI.
* **Efficient Screening:** This tool helps recruiters quickly sort and filter resumes, saving time and improving efficiency.

**Technologies Used:**

* **Streamlit:** For creating an interactive and easy-to-use web interface.
* **Flask:** To build a RESTful API that handles resume processing and ML model prediction.
* **Machine Learning:** A machine learning model (likely using libraries like scikit-learn) is used for classifying resumes into categories.  The model is trained on a dataset of resumes and their corresponding categories (as seen in the provided notebook).
* **Python:** The entire application is developed in Python.

**Workflow:**

1.  **UI (Streamlit):**
    * Users upload a resume file.
    * The file is sent to the Flask API.
    * The predicted category is received from the API and displayed.

2.  **API (Flask):**
    * Receives the resume file from Streamlit.
    * Preprocesses the resume text (cleaning, vectorization using TF-IDF).
    * Uses the pre-trained ML model to predict the category.
    * Sends the predicted category back to Streamlit.

**Machine Learning Model:**

The machine learning model is trained to classify resumes into predefined categories.  Key steps in the model development include:

* **Data Preprocessing:** Cleaning the resume text (removing URLs, special characters, etc.).
* **Feature Extraction:** Converting the text into numerical features using TF-IDF.
* **Model Training:** Training a classification model (e.g., SVC, Random Forest) on the training data.
* **Model Evaluation:** Evaluating the model's performance on a test dataset.
* **Model Deployment:** Saving the trained model for use in the Flask API.

**UI Examples:**

**1. Resume Upload UI:**

![Home Page](https://github.com/profitter261/Resume-screening-app/blob/main/Dashboard/Screenshot%202025-04-09%20232301.png)

**2. Resume with Predicted Category:**

![Results](https://github.com/profitter261/Resume-screening-app/blob/main/Dashboard/Screenshot%202025-04-09%20232328.png)
![Results](https://github.com/profitter261/Resume-screening-app/blob/main/Dashboard/Screenshot%202025-04-09%20232343.png)
![Results](https://github.com/profitter261/Resume-screening-app/blob/main/Dashboard/Screenshot%202025-04-09%20232301.png)

