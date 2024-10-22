# Interview-question-GenAI

---

## Generative AI Interview Question Project

This project utilizes **LangChain**, **OpenAI**, and **FAISS** to generate questions and answers based on input PDF files. It is designed to prepare coders and programmers for technical exams and interviews by generating context-aware questions and answers from coding documentation or other technical content provided in PDF format.

### **Table of Contents:**
1. [Project Structure](#project-structure)
2. [Setup and Installation](#setup-and-installation)
3. [How it Works](#how-it-works)
4. [Usage](#usage)
5. [Dependencies](#dependencies)
6. [Running the Project](#running-the-project)
7. [File Descriptions](#file-descriptions)

---

### **Project Structure**

```bash
.
├── data/
│   ├── docs/
│   ├── output/
│   └── research/
│       └── trials.ipynb
├── src/
│   ├── helper.py
│   ├── prompt.py
│   └── __init__.py
├── static/
│   ├── docs/
│   ├── output/
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
├── setup.py
├── template.py
├── test.py
└── README.md
```

- `data`: Stores any research files or output.
- `src`: Contains the core logic for processing files and generating Q&A.
- `static`: Stores static assets like PDFs and output files.
- `templates`: Contains the HTML template for the FastAPI interface.
- `app.py`: The main FastAPI application that allows users to upload PDFs and receive generated Q&A.
- `requirements.txt`: Lists the Python dependencies for the project.

---

### **Setup and Installation**

To get started, follow the steps below:

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create a Virtual Environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # For Linux/macOS
   # or
   .\.venv\Scripts\activate  # For Windows
   ```

3. **Install Dependencies:**
   Install the necessary Python libraries using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up OpenAI API Key:**
   - Create a `.env` file in the root directory.
   - Add your OpenAI API Key to the `.env` file:
     ```
     OPENAI_API_KEY=<your-openai-api-key>
     ```

---

### **How it Works**

1. **Upload a PDF:**  
   Users can upload a PDF file through the FastAPI web interface.
   
2. **Document Processing:**  
   The file is processed in `src/helper.py` using the **LangChain PyPDFLoader** to extract content, split it into chunks, and create document objects for further processing.

3. **Question Generation:**  
   A **LangChain Summarize Chain** is used with the provided prompts in `src/prompt.py` to generate interview questions based on the PDF content. The chain type used is "refine", where initial questions are generated and refined based on context.

4. **Answer Generation:**  
   Using **FAISS**, a vector store is created for document retrieval. The generated questions are then passed to a **RetrievalQA Chain** to generate answers.

5. **Q&A Output:**  
   The generated questions and answers are stored in a CSV file and made available for download.

---

### **Usage**

1. **Run the FastAPI Server:**
   To start the application, run:
   ```bash
   python app.py
   ```

2. **Access the Web Interface:**
   Open a browser and go to `http://localhost:8080`. You'll be presented with a simple interface to upload a PDF and generate Q&A.

3. **Upload a PDF:**  
   - Click the "Choose File" button and select a PDF from your system.
   - Click "Generate Q&A" to start the process.
   - The system will display a PDF preview and download link for the generated Q&A CSV file.

---

### **Dependencies**

The project uses the following key libraries and frameworks:
- **LangChain**: For document loading, chunking, and question generation.
- **OpenAI**: For language models (e.g., `gpt-3.5-turbo`).
- **FAISS**: To create an efficient vector store for document retrieval.
- **FastAPI**: For building the web interface and handling requests.
- **Uvicorn**: To serve the FastAPI application.
- **PDF libraries**: Such as **PyPDFLoader** for handling PDF file content extraction.

Additional dependencies are listed in the `requirements.txt` file.

---

### **Running the Project**

1. Ensure you have followed the setup steps above and that all dependencies are installed.
   
2. Run the application with:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8080 --reload
   ```

3. Open the browser at `http://localhost:8080` to use the application.

---

### **File Descriptions**

Here’s a breakdown of key files in the project:

- **app.py**:  
   The main FastAPI file that handles routing and provides an interface for uploading PDFs, generating questions, and downloading Q&A.

- **src/helper.py**:  
   Contains the logic for processing the PDF files. It uses LangChain for loading PDFs, splitting text, and creating document objects. It also handles the LangChain Summarize Chain for question generation.

- **src/prompt.py**:  
   Stores the question generation and refinement templates for the LangChain prompt.

- **template.py**:  
   A script that ensures necessary directories and files are created in the project structure. It checks if files already exist and creates them if they don’t.

- **requirements.txt**:  
   Lists all the dependencies required to run the project.

---
