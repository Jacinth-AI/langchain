import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableMap, RunnableLambda
from langchain_anthropic import ChatAnthropic
from langchain.memory import ConversationBufferMemory
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

def input_to_upper(input):
    output = input['user_input'].upper()  #HELLO
    return {'user_input': output}  #{'user_input': HELLO}

if __name__=='__main__':

    chain = RunnablePassthrough() | RunnableLambda(input_to_upper) | RunnablePassthrough()
    x = chain.invoke({"user_input": "hello"})
    print(x)