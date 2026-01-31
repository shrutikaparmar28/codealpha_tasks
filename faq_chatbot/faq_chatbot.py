
import nltk
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


nltk.download('punkt')
nltk.download('stopwords')



faqs = {
    "What is your return policy?": "You can return the product within 7 days of delivery.",
    "How can I contact customer support?": "You can contact customer support via email or phone.",
    "What payment methods do you accept?": "We accept UPI, debit card, credit card, and net banking.",
    "Do you provide home delivery?": "Yes, we provide home delivery all over India.",
    "How long does delivery take?": "Delivery usually takes 3 to 5 working days."
}



def preprocess_text(text):
    """
    This function:
    1. Converts text to lowercase
    2. Removes punctuation
    3. Tokenizes words
    4. Removes stopwords
    """

    text = text.lower()

    text = text.translate(str.maketrans('', '', string.punctuation))

    tokens = word_tokenize(text)

    stop_words = stopwords.words('english')
    cleaned_tokens = [word for word in tokens if word not in stop_words]

    return " ".join(cleaned_tokens)


questions = list(faqs.keys())
processed_questions = [preprocess_text(q) for q in questions]


vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(processed_questions)


def get_best_answer(user_question):

   
    processed_user_question = preprocess_text(user_question)

   
    user_vector = vectorizer.transform([processed_user_question])

    
    similarity_scores = cosine_similarity(user_vector, faq_vectors)

    
    best_match_index = similarity_scores.argmax()

    
    return faqs[questions[best_match_index]]


