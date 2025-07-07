import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableMap, RunnableLambda
from langchain_anthropic import ChatAnthropic
from langchain.memory import ConversationBufferMemory
from langchain_core.output_parsers import StrOutputParser


if __name__=='__main__':

    chain = RunnablePassthrough() | RunnablePassthrough () | RunnablePassthrough ()
    x = chain.invoke({"user_input": "test"})
    print(x)