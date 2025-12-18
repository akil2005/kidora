from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
from .prompt_templates import generate_story_prompt

load_dotenv()


def generate_story(question: str):
    """Generates a story using a language model and returns the response."""

    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        temperature=0.6,
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        convert_system_message_to_human=True
    )

    prompt = generate_story_prompt()

    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"question": question})
