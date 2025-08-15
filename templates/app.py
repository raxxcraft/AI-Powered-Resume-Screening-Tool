from flask import Flask, render_template, request, jsonify
import webbrowser
import threading
import time
import PyPDF2
from ats_screener import screen_resume

app = Flask(__name__)

def open_browser():
    time.sleep(2)
    try:
        webbrowser.open('http://localhost:8080')
    except:
        pass

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_resume():
    try:
        if 'resume' not in request.files:
            return jsonify({'error': 'No file uploaded'})
        
        file = request.files['resume']
        if file.filename == '' or not file.filename.endswith('.pdf'):
            return jsonify({'error': 'Please upload a PDF file only'})
        
        reader = PyPDF2.PdfReader(file)
        resume_text = ''
        for page in reader.pages:
            resume_text += page.extract_text()
        
        if not resume_text.strip():
            return jsonify({'error': 'Could not extract text from PDF'})
        
        result = screen_resume(resume_text)
        
        skill_score = (len(result['skills']) / 25) * 100
        experience_score = result['score'] - skill_score
        
        # Evaluation description
        if result['score'] >= 70:
            evaluation = "Excellent match! Strong candidate for Junior SDE role."
            status = "excellent"
        elif result['score'] >= 50:
            evaluation = "Good match. Candidate shows relevant skills and experience."
            status = "good"
        else:
            evaluation = "Needs improvement. Consider gaining more relevant experience."
            status = "needs-work"
        
        return jsonify({
            'filename': file.filename,
            'score': result['score'],
            'skills': result['skills'],
            'skill_count': f"{len(result['skills'])}/25",
            'skill_score': round(skill_score, 1),
            'experience_score': round(experience_score, 1),
            'evaluation': evaluation,
            'status': status
        })
    except Exception as e:
        return jsonify({'error': f'Processing failed: {str(e)}'})

if __name__ == '__main__':
    print("Starting ATS Screener...")
    threading.Thread(target=open_browser, daemon=True).start()
    app.run(host='localhost', port=8080, debug=False, use_reloader=False)
