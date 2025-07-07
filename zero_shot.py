import os
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate   # type: ignore
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

load_dotenv()


llama ='llama3-70b-8192'

model = ChatGroq(temperature=0, model_name=llama)

if __name__=='__main__':
    
    prompt = ChatPromptTemplate.from_template('''Extract key information from the below text and give output in key value format.
    Please give me the output in proper JSON format without any other verbose.                                    
                                              
                                               {topic}''')

    output_parser = StrOutputParser()

    chain = prompt | model | output_parser

    response = chain.invoke({"topic": '''The mutual fund generated an 8.4% return in Q1 2025, with Chinese stocks increasing by 12%. The expense ratio is 0.95%, and 45% of the portfolio is in technology stocks. 
        The fund has a turnover rate of 25%, and its average yield is 4.2%. The price-to-earnings (P/E) ratio is 15, with a dividend yield of 2.1%. 
        The fund also has a beta of 1.1.'''})

    print(response)
    