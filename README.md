# AI-Powered-Resume-Screening-Tool
This project uses Natural Language Processing (NLP) to automate resume screening and skill extraction. It reads resumes in PDF or text format, identifies key skills, and optionally matches them against a job description to generate a relevance score.
# 🎯 Junior SDE ATS Resume Screener

A professional AI-powered Applicant Tracking System (ATS) designed specifically for Junior Software Development Engineer positions. Built with Flask, Spacy NLP, and modern web technologies.

![ATS Screener Demo](demo.png)

## ✨ Features

- **🤖 AI-Powered Analysis**: Advanced NLP processing using Spacy for accurate skill extraction
- **📄 PDF Resume Upload**: Seamless PDF parsing and text extraction
- **🎨 Professional UI**: Clean, modern interface with responsive design
- **📊 Detailed Scoring**: Comprehensive breakdown of skills and experience evaluation
- **⚡ Real-time Processing**: Instant results with professional feedback
- **🎯 Junior SDE Focused**: Tailored specifically for entry-level software engineering roles

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/Anand0295/ats_screener.git
cd ats_screener

# Install dependencies
pip install -r requirements.txt

# Download Spacy language model
python -m spacy download en_core_web_sm

# Run the application
python app.py
```

The application will automatically open in your browser at `http://localhost:8080`

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **NLP Processing**: Spacy
- **PDF Processing**: PyPDF2
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Modern CSS with gradients and animations

## 📋 Evaluation Criteria

### Technical Skills (25 Categories)
- **Programming Languages**: Python, Java, JavaScript, C++, C#
- **Web Technologies**: HTML, CSS, React, Angular, Vue, Node.js, Django
- **Databases**: SQL, MySQL, PostgreSQL, MongoDB
- **Tools & Platforms**: Git, GitHub, AWS, Azure, Docker, Kubernetes
- **Core Concepts**: Data Structures, Algorithms, System Design, Testing, Debugging

### Scoring Algorithm
- **Skill Score (0-100%)**: Based on technical skills found in resume
- **Experience Score (0-30%)**: Weighted by experience keywords and project descriptions
- **Final Score**: Combined weighted score with professional evaluation

## 📊 Sample Output

```
Skills Found (11/25): python, javascript, css, nodejs, django, sql, mysql, postgresql, git, aws, testing
Match Score: 65.7%

Breakdown:
• Skill Score: 44.0%
• Experience Score: 21.7%
• Total: 65.7%

Evaluation: Good match. Candidate shows relevant skills and experience.
```

## 🎨 User Interface

### Upload Screen
- Clean, professional design
- Drag-and-drop PDF upload
- Instant file validation

### Results Screen
- **File Display**: Shows uploaded filename as professional button
- **Score Card**: Large, prominent score with gradient background
- **Evaluation**: Color-coded feedback (Excellent/Good/Needs Work)
- **Skills Tags**: Visual representation of detected skills
- **Detailed Breakdown**: Comprehensive scoring analysis

## 📁 Project Structure

```
ats_screener/
├── app.py                 # Flask web application
├── ats_screener.py        # Core NLP processing logic
├── templates/
│   └── index.html         # Frontend interface
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── screenshot.png        # Demo screenshot
```

## 🔧 Configuration

### Customizing Skills
Edit the `JUNIOR_SDE_SKILLS` list in `ats_screener.py`:

```python
JUNIOR_SDE_SKILLS = [
    'python', 'java', 'javascript', 'react',
    # Add or remove skills as needed
]
```

### Adjusting Scoring
Modify the scoring algorithm in `calculate_score()` function:

```python
def calculate_score(resume_text):
    skill_score = (len(skills) / len(JUNIOR_SDE_SKILLS)) * 100
    experience_score = min(experience_count * 5, 30)  # Adjust multiplier
    return min(100, round(skill_score + experience_score, 1))
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## 🙏 Acknowledgments

- [Spacy](https://spacy.io/) for powerful NLP capabilities
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [PyPDF2](https://pypdf2.readthedocs.io/) for PDF processing

---

⭐ **Star this repository if you found it helpful!**
