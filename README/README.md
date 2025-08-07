## Multilingual HR & Employee Support Chatbot

## 🧠 ABOUT THIS PROJECT ==>

- This is a Python-based HR support chatbot that can understand and answer HR-related queries in multiple languages using advanced language models and translation tools.

- It is designed to assist employees with HR-related questions such as leave policies, payroll FAQs, and company news by leveraging Natural Language Processing (NLP) and OpenAI's GPT models.

- Ideal for internal company tools, global organizations, and multilingual teams.

---

## ⚙ TECHNOLOGIES USED ==>

- **Python**

- **Streamlit** (for the interactive web UI)

- **OpenAI GPT API** (for intelligent chat responses)

- **Googletrans / Langdetect** (for language detection & translation)

- **JSON / TXT** (for knowledge base storage)

- **Natural Language Processing** (via LLMs)

---

## 📁 PROJECT FOLDER STRUCTURE ==>

multilingual-hr-bot/
│
├── hr_knowledge/
│   ├── company_policies.txt
│   ├── leave_rules.json
│   ├── payroll_faqs.txt
│   └── company_news.json
│
├── modules/
│   ├── chatbot.py             # Main chatbot logic & memory
│   ├── hr_knowledge_loader.py # Loads & preprocesses HR knowledge
│   ├── translation.py         # Language detection + translation logic
│   └── openai_api.py          # Wrapper for OpenAI GPT API calls
│
├── venv/                    
│
├── app.py                     # Streamlit app (frontend)
├── requirements.txt
└── README.md                  # Setup & usage instructions


---

## 📝 WHAT EACH FILE DOES ==>

**app.py**:
- The main entry point for the chatbot.
- Builds the UI using Streamlit.
- Handles session state, user input, and response display.

**requirements.txt**:
- Contains all Python packages required to run the project, such as streamlit, openai, googletrans, and others.

**chatbot.py**:
- Implements the HRChatbot class.
- Handles conversation logic, maintains context, and interacts with translation and OpenAI modules.

**hr_knowledge_loader.py**:
- Loads and processes internal HR knowledge documents (e.g., policies, FAQs).
- Prepares text snippets for GPT context augmentation.

**translation.py**:
- Detects user input language using langdetect.
- Translates input to English and output back to the original language using googletrans.

**openai_api.py**:
- Contains all logic for interacting with the OpenAI API.
- Centralizes prompt formatting and handles GPT-4/GPT-4o calls with error handling.

**company_policies.txt**:
- Plain-text file outlining HR and employee conduct policies.

**leave_rules.json**:
- Contains structured information about leave types, limits, and application rules.

**payroll_faqs.txt**:
- Text-based frequently asked questions related to salary, payslips, tax, etc.

**company_news.json**:
- A sample feed of company announcements or updates, potentially used to enrich chatbot responses.

**venv**:
- Contains all the locally installed dependencies isolated from your system Python

---

## 🚀 HOW TO RUN ==>

- Open cmd and run following commands ->

# Step 1: Move to the project directory:
cd "D:\multilingual_hr_bot"
D:

# Step 2: Install a virtual environment:
python -m venv venv

# Step 3: Run the virtual environment:
venv\Scripts\activate

# Step 4: Install the required dependencies:
pip install -r requirements.txt

# Step 5: Set OPENAI_API_KEY:
set OPENAI_API_KEY=your_openai_api_key_here                                  <<-- READ 'How_to_generate_openai_key.txt' TO GET THIS KEY !!

# Step 6: Run the Multilingual HR Chatbot:
streamlit run app.py
http://localhost:8501                 <-- [IT SHOULD OPEN ON YOUR BROWSER AUTOMATICALLY / OR MANUALL TYPE THIS IN BROWSER IF NOT OPENED! ]

---

## ✨ SAMPLE OUTPUT ==>

🌐 Language Detected: French
🔄 Translated Query: "What are the working hours in the company?"
📥 User Asked: "Quelles sont les heures de travail dans l'entreprise ?"

🤖 Bot Reply (English):  
"The standard working hours are from 9:00 AM to 6:00 PM, Monday through Friday. Flexible timings are available upon manager approval."

📝 Source: company_policies.txt  
📊 Confidence: 96.8%  
✅ Status: Response Delivered


---

## 📬 CONTACT ==>

For questions or feedback, feel free to reach out!


---
