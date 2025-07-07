import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableMap, RunnableLambda, RunnableParallel
from langchain_anthropic import ChatAnthropic
from langchain.memory import ConversationBufferMemory
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

def input_to_upper(input):  #{"input": "hello", "input2": "goodbye"})
    output = input['input2'].upper() #OUTPUT = GOODBYE
    return {"input": "hello", 'input2': output}

def input_(input):  #{"input": "hello", "input2": "goodbye"}
    output = input['input'].upper()+str(100)  ##output = HELLO100
    return {"input": output, 'input2': output}

if __name__=='__main__':

    chain = RunnableParallel({"x": RunnableLambda(input_), "y": RunnableLambda(input_to_upper)})

    #x = chain.invoke("hello")
    y = chain.invoke({"input": "hello", "input2": "goodbye"})
    print(y)