# content.py
# all website content lives here as Python dictionaries.
# easy to update and extend.

SITE = {
    "name": "delphine nyaboke",
    "tagline": "Machine Learning & Software Engineer",
    "description": "Building responsible, inclusive AI for low-resource contexts",
    "location": "Nairobi, Kenya",
    "email": "delphinenyaboke [at] gmail [dot] com",
    "social": {
        "linkedin": "https://www.linkedin.com/in/delphine-nyaboke/",
        "github": "https://github.com/delphine-boke",
        "x": "https://x.com/delphinenyabo12", 
        "medium": "https://medium.com/@delphinenyaboke", 
    }
}

# =====================
# HERO / ABOUT SECTION
# =====================
about = {
    "title": "About Me",
    "intro": """I'm a Machine Learning and Software Engineer with experience designing and deploying  AI/ML systems in low-resource African settings. 
    My work focuses on responsible AI, evidence synthesis, 
    multilingual systems, and human-in-the-loop approaches — particularly in policy, journalism, healthcare, and education.""",
}

# =====================
# EXPERIENCE 
# =====================
experience = [
    {
        "role": "AI & Machine Learning Specialist",
        "company": "International Centre for Evaluation and Development (ICED)",
        "period": "February 2026 – April 2026",
        "location": "Nairobi, Kenya",
        "description": "Led the design and integration of AI-enabled tools to support evidence synthesis, systematic reviews, and policy decision-making.",
        "highlights": [
            "Built production-grade conversational RAG chatbot (LangGraph + Streamlit) for policy outputs from 500+ PDF collections",
            "Developed Flask file download API with SHA-256 integrity verification and secure streaming",
            "Created Django-based finance automation system integrated with Microsoft Graph API and Azure AD",
            "Designed RIS-to-PDF conversion pipelines with integrity checks"
        ]
    },
    {
        "role": "Machine Learning Intern",
        "company": "International Labour Organization (ILO)",
        "period": "June 2025 – December 2025",
        "location": "Geneva / Remote",
        "description": "Developed and deployed an LLM-powered document classification and ranking tool that reduced processing time from 3 days to under 5 minutes.",
        "highlights": [
            "Built production LLM document classification system with human-in-the-loop validation",
            "Implemented CI/CD pipelines and ontology-based quality checks",
            "Tool remains actively used by the ILO Library",
            "Contributed to Swahili component of Global PIQA benchmark (arXiv:2511.03464)"
        ]
    },
    {
        "role": "Software Engineer",
        "company": "THiNK",
        "period": "2023 – 2025",
        "location": "Kenya",
        "description": "Built multilingual conversational AI systems and automation tools for government and fintech platforms serving millions of users.",
        "highlights": [
            "Developed Rasa + Django multilingual chatbot integrated with Kenyan government platforms (eCitizen, etc.)",
            "Reduced operational costs by ~50% through LLM automation for bank/fintech processes",
            "Improved technical documentation coverage from 10% to 90%"
        ]
    },
    {
        "role": "Software Engineer",
        "company": "Sendy",
        "period": "2021 – 2023",
        "location": "Kenya & Regional",
        "description": "Contributed to logistics and payments infrastructure across five African countries.",
        "highlights": [
            "Worked on tracking systems, M-Pesa integrations, and algorithm optimization",
            "Supported compliance and process improvements across multiple markets"
        ]
    }
]

# =====================
# PROJECTS
# =====================
projects = [
    {
        "title": "Global PIQA (Swahili Component)",
        "description": "Contributed to the Swahili portion of the Global PIQA benchmark for physical commonsense reasoning in low-resource languages.",
        "tech": ["LLMs", "Evaluation", "Multilingual AI"],
        "link": "https://arxiv.org/abs/2510.24081"
    },
    
    {
        "title": "Enhancing Modified VGG16 for Monkeypox Detection",
        "description": "Improved model for monkeypox detection using modified VGG16 and explored architectures like ConvNext for enhanced accuracy in data processing",
        "tech": ["Deep Learning", "CNNs", "Medical Imaging"],
        "link": "https://drive.google.com/file/d/18ioVK1PuAFllV2v7fvo0ukvSYY3fSE3R/view?usp=sharing"
    },
    
    {   
        "title": "Forecasting Electoral Violence by Leveraging Conflict Datasets",
        "description": "Integrated datasets for ML-based forecasting, involving data processing and analysis at election-year-country level.",
        "tech": ["Data Analysis", "Machine Learning", "Forecasting"],
        "link": "https://drive.google.com/file/d/1Ia1q7wlPCSAzB00wjTJVo_ZzqiL2TTeD/view"
    },
    
    {
        "title": "AI-Powered Question Answering for Low-Resourced Schools",
        "description": "Developed conversational chatbot using Rasa, OpenAI, and LLMs for educational information management.",
        "tech": ["Rasa", "OpenAI", "LLMs"],
        "link": "https://drive.google.com/file/d/1SQoPg2NLBa8mH4Cg5WWsu7tbzavJ284-/view"
    },
    
    {
        "title": "LLM-Powered Hospital Navigation System",
        "description": "Collaborated on LLM system to streamline patient appointment booking, focusing on data processing and integration.",
        "tech": ["LLMs", "Chainlit", "Data Processing", "Healthcare"],
        "link": "https://drive.google.com/file/d/11GuEpYj6H1Y1fAEmIDjCAxsf5j5rZbym/view"
    },
    
    {
        "title": "Leveraging LLMs for Low-Resourced Languages",
        "description": "Built interface for science education in Kinyarwanda using LLMs, supporting information management in low-resource settings.",
        "tech": ["LLMs", "Multilingual AI", "Education"],
        "link": "https://drive.google.com/file/d/1qq5v1s6Tdv1tXxKCyvjbG6vZviaRscPw/view"
    }
    
]

# =====================
# FAMILY SECTION (3-4 photos)
# =====================
family = {
    "title": "Personal",
    "description": "A few moments that ground me ...",
    "photos": [
        {"file": "static/images/family/family-photo-one.jpg", "caption": "With daughter"},
        {"file": "static/images/family/karting.jpg", "caption": "Partner with kids"},
        {"file": "static/images/family/pigeon.jpg", "caption": "Partner"},
        {"file": "static/images/family/me.jpg", "caption": "Me"},
    ]
}

# =====================
# SKILLS
# =====================
skills = {
    "technical": ["Python", "C/C++", "Java", "PyTorch", "LangChain / LangGraph", "Django", "Flask", "Docker", "Git"],
    "ai_ml": ["Deep Learning", "Machine Learning", "Artificial Intelligence", "RAG Systems", "LLM Evaluation", "Multilingual AI", "Responsible AI", "Explainable AI"],
    "languages": ["Swahili (Native)", "English (Fluent)", "Mandarin(Basic)", "French(Basic)", "Abagusii (Native)", "Agikuyu(Basic)"]
}

# =====================
# EDUCATION
# =====================
education = [
    {
        "degree": "MSc Engineering Artificial Intelligence",
        "institution": "Carnegie Mellon University Africa",
        "year": "2025",
        "link": "https://www.cmu.edu/"
    },
    {
        "degree": "BSc Electrical and Electronic Engineering",
        "institution": "Jomo Kenyatta University of Agriculture and Technology (JKUAT)",
        "year": "2020",
        "link": "https://www.jkuat.ac.ke/"
    }
]

# =====================
# CONTACT
# =====================
contact = {
    "email": SITE["email"],
    "message": "Feel free to reach out for collaborations, speaking, or just to say hello."
}

