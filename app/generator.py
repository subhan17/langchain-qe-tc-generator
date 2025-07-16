from itertools import chain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4o", temperature=0.5, api_key=api_key)



def generate_bdd(user_input):
    template = """
    You are an expert QA engineer. Write **complete** Gherkin-style BDD test scenarios for the following requirement:
      """+user_input

    prompt = ChatPromptTemplate(template)
    # filled_prompt = prompt.format(feature_description=feature_description)
    # print("Final Prompt:\n", filled_prompt)
    chain1 = prompt | llm
    response = chain1.invoke({"feature_description": user_input}).content.strip()
    #print(feature_description)
    return response
