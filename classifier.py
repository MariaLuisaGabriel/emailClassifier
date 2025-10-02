from flask import Flask, request, make_response
import spacy
import re
import nltk
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
from nltk.corpus import stopwords
from transformers import pipeline

app = Flask(__name__)

classifier = pipeline("zero-shot-classification", model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli", framework="pt")

@app.route('/classifier', methods=['GET'])
def handler():
    email = request.args.get('email', 'sem email')
    
    # Definir labels que definem com maior clareza o que são emails produtivos e improdutivos
    labels = ["solicitações suporte técnico atualização casos em aberto dúvidas sistema comunicados manutenção",
                "parabéns felicitações agradecimentos reconhecimento bom trabalho anúncio convite evento webinar workshop"]
    
    # Pré-processamento do email (lematização e remoção dos stopwords)
    ppemail = preprocess_text(email)
    
    # Classificação do email com zero-shot-classification
    result = classifier(ppemail, candidate_labels=labels)
    lb = result['labels'][0] # label com maior score
    classif = "Produtivo" if lb.startswith("solicitações") else "Improdutivo"
    
    # Gerar resposta HTTP
    response = make_response(classif)
    response.headers['Content-Type'] = 'text/plain'
    response.headers['Access-Control-Allow-Origin'] = '*'
    
    return response

def preprocess_text(text):
    
    # remoção de quebras de linha, hífens, aspas e pontos
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r' - ', ' ', text)
    text = re.sub(r'- ', '', text)
    text = re.sub(r'•', ' ', text)
    text = re.sub(r'“', ' ', text)
    text = re.sub(r'”', ' ', text)
    
    doc = ""
    
    # remoção de pontuações
    for s in text:
        if not(s==')' or s =='(' or s ==','  or s == '.' or s == ';' or s == ':' or s == '!' or s == '?' or s =='"' or s =='\'' or s =='/' or s =='\\'):
            doc += s
    
    # Definir stopwords em português
    stop_words = set(stopwords.words("portuguese"))

    # Tokenizar palavras
    no_stopwords_doc = []
    
    palavras = word_tokenize(doc, language='portuguese')
    no_stopwords_doc = [palavra for palavra in palavras if palavra.lower() not in stop_words]
    no_stopwords_doc = [nsd for nsd in no_stopwords_doc if nsd]
    
    # Carregar modelo de linguagem do spaCy (português)
    nlp = spacy.load("pt_core_news_sm")
    
    # Lematização
    tokens = nlp(" ".join(no_stopwords_doc))
    doc_lemma = " ".join([token.lemma_ for token in tokens]).lower()
    
    return doc_lemma

if __name__ == '__main__':
    app.run(debug=True)