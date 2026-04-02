import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

# ==============================
# QUESTIONS
# ==============================
questions = [
    "who are you",
    "what is your name",
    "where do you study",
    "which university do you study in",
    "what is your course",
    "what do you study",
    "what is your goal",
    "what are your skills",
    "what is your achievement",
    "what is your academic result",
    "what are you interested in",
    "what is your dream",
    "what is your future plan",
    "tell me about yourself",
    "why are you doing this internship",
    "why did you choose this course",
    "what are your hobbies",
    "what do you do in your free time",
    "what makes you unique"
]

# ==============================
# ANSWERS
# ==============================
answers = [
    "I am Rahmat Ullah Sabbir, a passionate student interested in AI and software development.",
    "My name is Rahmat Ullah Sabbir.",
    "I study at Ulster University in the UK.",
    "I study at Ulster University in the UK.",
    "I am studying BSc (Hons) Computing Systems.",
    "I am studying BSc (Hons) Computing Systems at Ulster University.",
    "My goal is to become a software engineer and build impactful technology solutions.",
    "My skills include Python programming, problem solving, and basic AI knowledge.",
    "I received the Community Hero award and participated in robotics programs.",
    "I achieved GPA 5.00 in SSC and 4.42 in HSC.",
    "I am interested in AI, technology, and climate change.",
    "My dream is to become a successful software engineer and entrepreneur.",
    "My future plan is to study computer science and build my own IT company.",
    "I am a motivated student passionate about learning and building projects.",
    "I am doing this internship to gain practical experience in AI.",
    "I choose this course because I am passionate about technology and want to become a software engineer.",
    "My hobbies include playing cricket, football, travelling, and gardening.",
    "In my free time, I enjoy playing cricket and football, travelling, and gardening.",
    "I am unique because I combine my passion for technology with real-world problem solving and continuous self-improvement."
]

# ==============================
# KEYWORD-BASED SMART RESPONSES
# ==============================
def keyword_response(user_input):
    if "name" in user_input:
        return "My name is Rahmat Ullah Sabbir."

    elif "university" in user_input:
        return "I study at Ulster University in the UK."

    elif "course" in user_input:
        return "I am studying BSc (Hons) Computing Systems."

    elif "study" in user_input:
        return "I study BSc (Hons) Computing Systems at Ulster University."

    elif "goal" in user_input:
        return "My goal is to become a software engineer and build impactful technology solutions."

    elif "skill" in user_input:
        return "My skills include Python programming, problem solving, and basic AI knowledge."

    elif "dream" in user_input:
        return "My dream is to become a successful software engineer and entrepreneur."

    elif "achievement" in user_input:
        return "I received the Community Hero award and participated in robotics programs."

    elif "result" in user_input:
        return "I achieved GPA 5.00 in SSC and 4.42 in HSC."

    elif "internship" in user_input:
        return "I am doing this internship to gain practical experience in AI."

    elif "hobby" in user_input or "free time" in user_input:
        return "My hobbies include playing cricket, football, travelling, and gardening."

    elif "unique" in user_input:
        return "I am unique because I combine my passion for technology with real-world problem solving and continuous self-improvement."

    return None

# ==============================
# CLEAN TEXT FUNCTION
# ==============================
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# ==============================
# NLP RESPONSE WITH CONFIDENCE
# ==============================
def nlp_response(user_input):
    processed_questions = [clean_text(q) for q in questions]
    all_questions = processed_questions + [user_input]

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(all_questions)

    similarity = cosine_similarity(vectors[-1], vectors[:-1])
    best_match_index = similarity.argmax()
    best_score = similarity[0][best_match_index]

    # Confidence threshold
    if best_score < 0.4:
        return None

    return answers[best_match_index]

# ==============================
# CHATBOT LOOP
# ==============================
print("🤖 Sabbir's AI Chatbot (type 'exit' to stop)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot stopped 👋")
        break

    cleaned = clean_text(user_input)

    # Step 1: keyword matching
    response = keyword_response(cleaned)

    # Step 2: NLP fallback
    if response is None:
        response = nlp_response(cleaned)

    # Step 3: unknown handling
    if response is None:
        response = "Sorry, I don’t have information about that."

    print("Bot:", response)
