from langchain.document_loaders import PyPDFLoader
from langchain.docstore.document import Document
from langchain.text_splitter import TokenTextSplitter
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
import os
from dotenv import load_dotenv
from src.prompt import *

print("test")

# OpenAI authentication

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def file_processng(file_path):

    #load data from PDF
    loader = PyPDFLoader(file_path)
    data = loader.load()

    question_gen = ''

    # Getting content from data
    for page in data:
        question_gen += page.page_content

   # bigger data chunkins see chunk size and chunk overlap
    splitter_ques_gen = TokenTextSplitter(
        model_name = 'gpt-3.5-turbo',
        chunk_size = 10000,
        chunk_overlap = 200
    )
    
     # split_text --> means chunks
    chunks_ques_gen = splitter_ques_gen.split_text(question_gen)
    
    document_ques_gen = [Document(page_content=t) for t in chunks_ques_gen]

   # smaller data chunkins see chunk size and chunk overlap
    splitter_ans_gen = TokenTextSplitter(
        model_name = 'gpt-3.5-turbo',
        chunk_size = 1000,
        chunk_overlap = 100
    )

    # split_documents --> means chunks
    document_answer_gen = splitter_ans_gen.split_documents(document_ques_gen)

    return document_ques_gen, document_answer_gen

def llm_pipeline(file_path):

    # calling file_proessing method
    document_ques_gen, document_answer_gen = file_processng(file_path)

    
    # initializing OpenAI Client
    llm_ques_gen_pipeline = ChatOpenAI(
        temperature=0.3,
        model = "gpt-3.5-turbo"
    )
    
    # Created prompt template
    PROMPT_QUESTIONS = PromptTemplate(template=prompt_template, input_variables=["text"])

    # created refine template
    REFINE_PROMPT_QUESTIONS = PromptTemplate(
        input_variables=["existing_answer", "text"],
        template = refine_template
    )
    


