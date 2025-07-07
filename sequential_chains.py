import os
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate   # type: ignore
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

load_dotenv()


llama ='llama3-70b-8192'

model = ChatGroq(temperature=0, model_name=llama)


prompt_extract = ChatPromptTemplate.from_template('''Extract key information from the below text and give output in key value format.
    Please give me the output in proper JSON format without any other verbose.                                    
                                              
                                               {topic}''')

prompt_stage_2 = ChatPromptTemplate.from_template('''You are a financial analyst. Given the following JSON of mutual fund metrics, provide a risk assessment and investment summary.

JSON:
{json_data}

Include:
- Risk level (Low, Medium, High)
- Recommendation for conservative investors
- Notable strengths or red flags''')

output_parser = StrOutputParser()



chain = prompt_extract | model | output_parser | prompt_stage_2 | model | output_parser


q = '''The mutual fund generated an 8.4% return in Q1 2025, with Chinese stocks increasing by 12%.
The expense ratio is 0.95%, and 45% of the portfolio is in technology stocks.
The fund has a turnover rate of 25%, and its average yield is 4.2%.
The price-to-earnings (P/E) ratio is 15, with a dividend yield of 2.1%.
The fund also has a beta of 1.1.'''

response = chain.invoke({
    "topic": q
})

print(response)