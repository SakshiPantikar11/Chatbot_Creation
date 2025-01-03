import nltk

from nltk.chat.util import Chat, reflections
import spacy

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def preprocess_input(text):
    tokens = word_tokenize(text)
    lemmatized_tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens]
    return ' '.join(lemmatized_tokens)

# Define conversation patterns and responses
patterns_and_responses = [
    (r'hi|hello|hey', ['Hello! How can I help you today?', 'Hi there! What can I do for you?']),
    (r'bye', ['Goodbye!', 'See you later!']),
    (r'what is your name?', ['I am a chatbot created by an AI intern!']),
    (r'how are you?', ['I am just a bot, but I am doing great!']),
]

# Initialize the chatbot with the patterns and reflections (a dictionary that can reflect responses)
chatbot = Chat(patterns_and_responses, reflections)

# Start chatbot
def start_chat():
    print("Hello! I am your AI assistant. Type 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    start_chat()
