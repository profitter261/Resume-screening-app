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
