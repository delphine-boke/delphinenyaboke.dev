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
    }
}

# =====================
# HERO / ABOUT SECTION
# =====================
about = {
    "title": "About Me",
    "intro": """I'm a Machine Learning and Software Engineer with experience designing and deploying 
    AI/ML systems in low-resource African settings. My work focuses on responsible AI, evidence synthesis, 
    multilingual systems, and human-in-the-loop approaches — particularly in policy, journalism, healthcare, and education.""",
}

# =====================
# EXPERIENCE 
# =====================
experience = [
    # {
    #     "role": "Mozilla Embedded Fellow",
    #     "company": "Baraza Media Lab",
    #     "period": "June 2026 – Present",
    #     "location": "Nairobi, Kenya",
    #     "description": "Leading the co-design and implementation of an AI bias auditing tool for Kenyan and African journalism as part of the Bias Lens project.",
    #     "highlights": [
    #         "Co-designing tools and annotation workflows with journalists through hackathons",
    #         "Building LangGraph + Streamlit prototype for detecting cultural and Western bias in AI-generated stories",
    #         "Running 100+ journalist pilot targeting >70% actionable accuracy",
    #         "Preparing open-source release and research outputs for Q4 2026"
    #     ]
    # },
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
    }
    
]

# =====================
# BIAS LENS FELLOWSHIP (Articles + Media)
# =====================
# fellowship = {
#     "title": "Bias Lens Fellowship",
#     "intro": "Updates, articles, and learnings from my Mozilla Fellowship work on AI bias auditing for journalism.",
#     "articles": [
#         {
#             "title": "First Journalist Hackathon – Key Learnings",
#             "date": "July 2026",
#             "summary": "Co-designed annotation guidelines with Kenyan journalists...",
#             "has_photo": True,
#             "photo": "static/images/fellowship/hackathon1.jpg",   # placeholder
#             "has_video": False,
#             "video_embed": None,   # or YouTube/Vimeo embed code later
#             "link": "#"
#         },
#         # Add more articles here...
#     ]
# }

# =====================
# FAMILY SECTION (3-4 photos)
# =====================
family = {
    "title": "Personal",
    "description": "A few moments that ground me.",
    "photos": [
        {"file": "static/images/family/family-photo-one.jpg", "caption": "With daughter"},
        {"file": "static/images/family/fmaily-photo-two.jpg", "caption": "With son"},
        {"file": "static/images/family/pigeon.jpg", "caption": "Partner"},
        {"file": "static/images/family/siblings.jpg", "caption": "Brother and Sister"},
    ]
}

# =====================
# SKILLS
# =====================
skills = {
    "technical": ["Python", "PyTorch", "LangChain / LangGraph", "Django", "Flask", "Docker", "Git"],
    "ai_ml": ["RAG Systems", "LLM Evaluation", "Multilingual AI", "Responsible AI", "XAI"],
    "languages": ["Swahili (Native)", "English (Fluent)", "Mandarin(Basic)", "French(Basic)", "Abagusii (Native)", "Agikuyu(Basic)"]
}

# =====================
# EDUCATION
# =====================
education = [
    {
        "degree": "MSc Engineering Artificial Intelligence",
        "institution": "Carnegie Mellon University(CMU)",
        "year": "2025"
    },
    {
        "degree": "BSc Electrical and Electronic Engineering",
        "institution": "Jomo Kenyatta University of Agriculture and Technology (JKUAT)",
        "year": "2020"
    }
]

# =====================
# CONTACT
# =====================
contact = {
    "email": SITE["email"],
    "message": "Feel free to reach out for collaborations, speaking, or just to say hello."
}

