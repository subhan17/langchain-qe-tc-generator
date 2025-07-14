from itertools import chain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import chatPromptTemplate
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4", temperature=0.3, api_key=api_key)

template = """
You are an expert QA engineer. Write Gherkin-style BDD test scenarios for the following requirement:
{feature_description}
"""

prompt = chatPromptTemplate(template)

def generate_bdd(feature_description):
    chain = prompt | llm
    response = chain.invoke({"feature_description": feature_description}).content.strip()
    return response.content
