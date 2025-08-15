import spacy
import re

nlp = spacy.load("en_core_web_sm")

JUNIOR_SDE_SKILLS = [
    'python', 'java', 'javascript', 'c++', 'c#', 'html', 'css', 'react', 
    'angular', 'vue', 'nodejs', 'django', 'sql', 'mysql', 'postgresql', 
    'mongodb', 'git', 'github', 'aws', 'azure', 'docker', 'kubernetes',
    'algorithms', 'data structures', 'system design', 'debugging', 'testing'
]

def extract_skills(text):
    found_skills = []
    for skill in JUNIOR_SDE_SKILLS:
        escaped_skill = re.escape(skill)
        if re.search(r'\b' + escaped_skill + r'\b', text.lower()):
            found_skills.append(skill)
    return found_skills

def calculate_score(resume_text):
    skills = extract_skills(resume_text)
    skill_score = (len(skills) / len(JUNIOR_SDE_SKILLS)) * 100
    
    doc = nlp(resume_text.lower())
    experience_keywords = ['experience', 'years', 'project', 'developed', 'built', 'implemented']
    experience_count = sum(1 for token in doc if token.text in experience_keywords)
    experience_score = min(experience_count * 5, 30)
    
    total_score = skill_score + experience_score
    return min(100, round(total_score, 1))

def screen_resume(resume_text):
    skills = extract_skills(resume_text)
    score = calculate_score(resume_text)
    
    return {
        'skills': skills,
        'score': score
    }
