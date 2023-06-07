## Import all the dependent libraries
import os
import spacy
from spacy.matcher import PhraseMatcher



def get_mca_questions(context: str):
   nlp = spacy.load('en_core_web_sm')
   # Define the questions and their expected answers
    questions = [
        {
            'question': 'Which of the following are examples of light-dependent reactions in photosynthesis?',
            'answers': ['Stripping electrons from suitable substances', 'Creating NADPH and ATP']
        },
        {
            'question': 'Which of the following are sources of electrons used by the first photosynthetic organisms?',
            'answers': ['Hydrogen sulfide', 'Water']
        },
        {
            'question': 'Which of the following are byproducts of photosynthesis?',
            'answers': ['Oxygen', 'NADPH']
        },
    ]
    
    # Tokenize the context using spaCy
    doc = nlp(context)
    
    mca_questions = []
    
    # Iterate over the questions and find the matching answers in the context
    for question in questions:
        answers = question['answers']
        matcher = PhraseMatcher(nlp.vocab)
        
        # Create patterns for each answer
        patterns = [nlp(answer) for answer in answers]
        matcher.add('Answer', None, *patterns)
        
        # Find the matches in the context
        matches = matcher(doc)
        
        # Extract the matched answer strings
        matched_answers = [doc[start:end].text for match_id, start, end in matches]
        
        # Check if all the expected answers are matched
        if set(answers) == set(matched_answers):
            mca_questions.append(question['question'])
   
   return mca_questions  
