from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()


def generate_rhyme(query: str):
    """Generates a rhyme using a language model and returns the response."""

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.7,
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        convert_system_message_to_human=True
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a friendly and creative AI that writes short, fun rhymes or poems for kids aged 5 to 10."),
        ("human", """Write a short rhyme or poem (8 - 12 lines) about the theme: {query}.
Make it simple, playful, and age-appropriate.
Use easy vocabulary and a fun rhythm.
Make sure the tone is cheerful."""),
    ])

    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"query": query})


def ask_your_buddy(question: str) -> str:
    """Ask your AI buddy a question and get a response."""

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.4,
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        convert_system_message_to_human=True
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a joyful, friendly AI buddy for kids. Be playful, encouraging, and age-appropriate."),
        ("human", "{question}"),
    ])

    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"question": question})


if __name__ == "__main__":
    print(generate_rhyme("A happy cat playing with a ball of yarn"))
