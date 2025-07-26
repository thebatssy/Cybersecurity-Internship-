import nltk
import argparse
import itertools
from zxcvbn import zxcvbn
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK resources (only needed once) or get from file named nltk_data/
nltk.download('punkt')
nltk.download('stopwords')

leet_dict = {
    'a': ['a', '@', '4'],
    'b': ['b', '8'],
    'c': ['c', '('],
    'e': ['e', '3'],
    'g': ['g', '9'],     
    'i': ['i', '1', '!'],
    'l': ['l', '1', '|'],
    'o': ['o', '0'],
    's': ['s', '$', '5'],
    't': ['t', '7'],
    'z': ['z', '2']
}

def analyze_password(password):
    result = zxcvbn(password)
    print("\n[Password Analysis]")
    print("Password:", password)
    print("Score:", result['score'], "/ 4")
    print("Guesses needed:", result['guesses'])
    if result['feedback']['warning']:
        print("Feedback:", result['feedback']['warning'])
    else:
        print("Feedback: Looks good!\n")


def leetspeak(word):
    options = [leet_dict.get(c.lower(), [c]) for c in word]
    return [''.join(p) for p in itertools.product(*options)]

def preprocess_with_nltk(text):
    # tokenize, remove stopwords, and keep alphanumeric only
    words = word_tokenize(text)
    clean = [w.lower() for w in words if w.lower() not in stopwords.words('english') and w.isalnum()]
    return clean

def generate_wordlist(data):
    base_words = []

    for entry in data:
        if entry:
            base_words.extend(preprocess_with_nltk(entry))

    wordlist = set()
    suffixes = ['', '123', '2024', '2025', '!', '@']

    for word in base_words:
        for variant in leetspeak(word):
            for suffix in suffixes:
                wordlist.add(variant + suffix)

    for a, b in itertools.permutations(base_words, 2):
        wordlist.add(a + b)
        wordlist.add(b + a)

    return sorted(wordlist)

def save_wordlist(wordlist, filename):
    with open(filename, 'w') as f:
        for word in wordlist:
            f.write(word + '\n')
    print("Wordlist saved to '" + filename + "' with " + str(len(wordlist)) + " entries.\n")

def main():
    parser = argparse.ArgumentParser(description="Password Analyzer & Wordlist Generator")
    parser.add_argument('--password', required=True, help='Password to analyze')
    parser.add_argument('--name', help='Your name')
    parser.add_argument('--dob', help='Date of birth')
    parser.add_argument('--pet', help='Pet name')
    parser.add_argument('--partner', help="Partner's name")
    parser.add_argument('--extra', help="Any extra personal info")
    parser.add_argument('--output', default='wordlist.txt', help='Output wordlist file')
    args = parser.parse_args()

    analyze_password(args.password)

    user_inputs = [args.name, args.dob, args.pet, args.partner, args.extra]
    wordlist = generate_wordlist(user_inputs)
    save_wordlist(wordlist, args.output)

if __name__ == '__main__':
    main()
    
    
