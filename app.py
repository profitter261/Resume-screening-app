import streamlit as st
import pickle
import nltk
import re

# NLTK downloads
nltk.download('stopwords')
nltk.download('punkt')

# Load model and vectorizer
clf = pickle.load(open('clf.pkl', 'rb'))
tfidfd = pickle.load(open('tfidf (1).pkl', 'rb'))

# Define text cleaning function
def clean_resume(resume_text):
    cleantxt = re.sub('http\S+\s', ' ', resume_text)
    cleantxt = re.sub('RT|cc', ' ', cleantxt)
    cleantxt = re.sub('#\S+\s', ' ', cleantxt)
    cleantxt = re.sub('@\S+', ' ', cleantxt)
    cleantxt = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_{|}~"""), ' ', cleantxt)
    cleantxt = re.sub(r'[^\x00-\x7f]', ' ', cleantxt)
    cleantxt = re.sub('\s+', ' ', cleantxt)
    return cleantxt

# Category Mapping
category_mapping = {
    6: 'Data Science', 12: 'HR', 0: 'Advocate', 1: 'Arts', 24: 'Web Designing',
    16: 'Mechanical Engineer', 22: 'Sales', 14: 'Health and fitness', 5: 'Civil Engineer',
    15: 'Java Developer', 4: 'Business Analyst', 21: 'SAP Developer', 2: 'Automation Testing',
    11: 'Electrical Engineering', 18: 'Operations Manager', 20: 'Python Developer',
    8: 'DevOps Engineer', 17: 'Network Security Engineer', 19: 'PMO', 7: 'Database',
    13: 'Hadoop', 10: 'ETL Developer', 9: 'DotNet Developer', 3: 'Blockchain', 23: 'Testing'
}

# Streamlit App
def main():
    st.set_page_config(page_title="Resume Screening", page_icon="📄", layout="centered")

    # Set custom background and content style
    st.markdown("""
        <style>
        .stApp {
            background-image: url("https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.2tmhpp-mzDTRA1zNcoipuAAAAA%26pid%3DApi&sp=1744039194T2ac7ab816e38f3dc10f99c640f275caa607fce810a6b4bbb960c11b2726dc32c");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }

        /* Reduce top spacing */
        .block-container {
            padding-top: 1rem;
            padding-bottom: 2rem;
        }

        /* Glass effect panel */
        .css-18e3th9 {
            background: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
        }

        h1 {
            color: #1c1c1c;
            text-shadow: 0px 1px 3px rgba(0, 0, 0, 0.1);
        }

        h2 {
            color: #004e89;
        }

        p {
            color: #333333;
        }

        .stMarkdown, .stTextInput, .stFileUploader, .stButton, .stSuccess {
            color: #000;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title and instructions
    st.markdown("<h1 style='text-align: center;'>📄 Resume Screening App</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Upload your resume below and get the predicted job category.</p>", unsafe_allow_html=True)
    st.markdown("---")

    uploaded_file = st.file_uploader('Upload Resume', type=['txt', 'pdf'])

    if uploaded_file is not None:
        try:
            resume_bytes = uploaded_file.read()
            resume_text = resume_bytes.decode('utf-8')
        except UnicodeDecodeError:
            resume_text = resume_bytes.decode('latin-1')

        cleaned_resume = clean_resume(resume_text)
        input_features = tfidfd.transform([cleaned_resume]).toarray()
        prediction_id = clf.predict(input_features)[0]
        prediction_label = category_mapping.get(prediction_id)

        st.success("✅ Resume uploaded successfully!")
        st.markdown("### 🎯 Predicted Job Category")
        st.markdown(f"<h2>{prediction_label}</h2>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
