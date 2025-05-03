# Hire-Helper

👋 Hi!
I'm Hire Helper, your AI assistant 🤖, assisting you with screening the candidates.

### Steps to use:
- Create a directory on your local machine.
- Open your terminal, navigate to the directory
- Execute the following lines one by one:
  
  ```
  git clone https://github.com/Aashish2502/Hire-Helper
  
  `python -m venv venv

  .\venv\Scripts\activate

  pip install -r requirements.txt

  streamlit run .\app\app.py --logger.level=error
  ```
> NOTE: Make sure to create your own API Keys to use the application. This will be resolved in the next versions of the app.

## Application Architecture:

The HIRE HELP application is structured around a modular and scalable architecture that integrates advanced AI technologies with a user-friendly interface. The core components include:

1. ### **Frontend Interface**
     Built with Streamlit for rapid UI development and easy deployment.

     Allows HR users to upload resumes and interact with the AI assistant.
    
     Provides real-time feedback and visual insights into candidate evaluation.

2. ### **Conversational AI Engine**
    Groq API is used for high-speed, low-latency response generation, enabling smooth and intelligent conversations.
    
    LangSmith is integrated for tracing, debugging, and monitoring model behavior.

3. ### **Embedding and Retrieval**
    Uses Hugging Face Transformers to generate embeddings from uploaded resume data.
    
    Embeddings are stored in a FAISS Vector Database for efficient semantic search and retrieval.

4. ### **Backend Pipeline**
    Uploaded resumes are preprocessed, parsed, and vectorized.
    
    On user queries, relevant documents are retrieved using vector similarity and passed to the LLM for context-aware responses.

5. ### **Monitoring and Improvement**
    LangSmith logs queries, latencies, and output reliability, allowing data-driven improvements in model accuracy and relevance.


## Upcoming Enhancements:
- You will only be required to input the Groq API Key to use the application.
- The User Experience will also be improved.
- Security of the app will be strengthened.

#### Thank you For Visiting and trying out Hire-Helper

### If any queries, please reach out to me:
- EMAIL: [Email📩](mailto:waghmare.2502@gmail.com)
- LinkedIn: [Aashish-Waghmare](https://www.linkedin.com/in/aashish-waghmare-1b4810202/)
- 
