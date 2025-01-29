from flask import Flask, render_template, request, jsonify
import PyPDF2
from PyPDF2 import PdfReader
import re
import pickle
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load model dan model TF-IDF
model = joblib.load('model1.joblib')  # Ganti 'model.pkl' dengan nama file model yang sesuai
with open('kbest_feature.pickle', 'rb') as tfidf_file:  # Ganti 'tfidf_model.pickle' dengan nama file model TF-IDF yang sesuai
    tfidf_model = pickle.load(tfidf_file)

# Download WordNet jika belum diunduh
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

stopwords_eng = stopwords.words('english')

# Inisialisasi WordNet Lemmatizer
lemmatizer = WordNetLemmatizer()

def casefolding(text):
  text = text.lower()                               # Mengubah teks menjadi lower case
  text = re.sub(r'https?://\S+|www\.\S+', '', text) # Menghapus URL
  text = re.sub(r'[-+]?[0-9]+', '', text)           # Menghapus angka
  text = re.sub(r'[^\w\s]','', text)                # Menghapus karakter tanda baca
  text = text.strip()
  return text

def remove_stop_words(text):
  clean_words = []
  text = text.split()
  for word in text:
      if word not in stopwords_eng:
          clean_words.append(word)
  return " ".join(clean_words)

def lemmatization(text):
  text = lemmatizer.lemmatize(text)
  return text

def text_preprocessing(text):
  text = casefolding(text)
  text = remove_stop_words(text)
  text = lemmatization(text)
  return text 

def extract_text_from_pdf(pdf_path):
    # Membaca teks dari file PDF
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PdfReader(file) 
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            text = pdf_reader.pages[page_num].extract_text()
    return text

@app.route('/', methods=['GET', 'POST'])
def classify_document():
    if request.method == 'POST':
        # Terima dokumen dari formulir
        document = request.files['pdf']
        pdf_path = 'uploaded_document.pdf'

        # Simpan file PDF yang diunggah
        document.save(pdf_path)

        # Baca teks dari file PDF
        text_from_pdf = extract_text_from_pdf(pdf_path)

        # Proses teks
        preprocessed_text = text_preprocessing(text_from_pdf)

        # Konversi teks menjadi representasi TF-IDF
        tf_idf_vec = TfidfVectorizer(vocabulary=set(tfidf_model))
        tfidf_vector = tf_idf_vec.fit_transform([preprocessed_text])

        # Klasifikasikan dokumen menggunakan model
        prediction = model.predict(tfidf_vector)

        # Hapus file PDF yang diunggah
        import os
        os.remove(pdf_path)

        # Kirim hasil klasifikasi sebagai JSON
        if (prediction==0):
            result = 'Account'
        elif (prediction==1):
            result = 'Business-Development'
        elif (prediction==2):
            result = 'Digital-Media'
        elif (prediction==3):
            result = 'Engineering'
        elif (prediction==4):
            result = 'Human Resource'
        elif (prediction==5):
            result = 'Sales'
        else:
            result = 'Tidak Tersedia'
        #return jsonify(result=str(prediction[0]))
        return jsonify(result)

    # Tampilkan formulir saat mengakses halaman
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
