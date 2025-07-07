import os
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate   # type: ignore
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

from langchain.schema.runnable import RunnableParallel, RunnableSequence

load_dotenv()

# Model
model = ChatGroq(temperature=0, model_name="llama3-8b-8192")
output_parser = StrOutputParser()

# -------- PROMPTS FOR PARALLEL TASKS --------

# Extract performance summary
performance_prompt = ChatPromptTemplate.from_template('''Extract a short summary of mutual fund performance from the text below.

Text:
{performance_text}''')

# Extract risk insights
risk_prompt = ChatPromptTemplate.from_template('''Summarize the potential risks of the mutual fund based on this text.

Text:
{risk_text}''')

# -------- FINAL ANALYSIS PROMPT --------

final_prompt = ChatPromptTemplate.from_template('''You are an investment analyst. Based on the following performance and risk summaries, write a recommendation for investors.

Performance Summary:
{performance}

Risk Summary:
{risk}''')

# -------- PARALLEL RUNNABLE --------

parallel_chain = RunnableParallel(
    {
        "performance": performance_prompt | model | output_parser,
        "risk": risk_prompt | model | output_parser,
    }
)

# -------- SEQUENCE: PARALLEL ➜ FINAL MODEL --------

full_chain = (
    parallel_chain
    | final_prompt
    | model
    | output_parser
)

# -------- INPUT DATA --------
q = '''The mutual fund generated an 8.4% return in Q1 2025, with Chinese stocks increasing by 12%.
The expense ratio is 0.95%, and 45% of the portfolio is in technology stocks.
The fund has a turnover rate of 25%, and its average yield is 4.2%.
The price-to-earnings (P/E) ratio is 15, with a dividend yield of 2.1%.
The fund also has a beta of 1.1.'''

input_data = {
    "performance_text": q,
    "risk_text": q
}

# -------- RUN THE CHAIN --------

final_response = full_chain.invoke(input_data)

print("📊 Final Recommendation:\n", final_response)