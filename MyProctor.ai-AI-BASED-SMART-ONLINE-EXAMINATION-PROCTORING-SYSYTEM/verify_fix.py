import nltk
from objective import ObjectiveTest

def verify():
    print("Testing ObjectiveTest with sample text...")
    sample_text = "The solar system consists of the Sun and the objects that orbit it. The Sun is the largest object in the solar system. Eight planets orbit the Sun."
    no_of_ques = 2
    
    try:
        # We need to make sure nltk resources are downloaded
        nltk.download('punkt', quiet=True)
        nltk.download('averaged_perceptron_tagger', quiet=True)
        nltk.download('wordnet', quiet=True)
        
        generator = ObjectiveTest(sample_text, no_of_ques)
        questions, answers = generator.generate_test()
        
        print(f"Generated {len(questions)} questions.")
        for i, (q, a) in enumerate(zip(questions, answers)):
            print(f"Q{i+1}: {q}")
            print(f"A{i+1}: {a}")
        
        print("Verification successful! No TypeError raised.")
    except Exception as e:
        print(f"Verification FAILED: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    verify()
