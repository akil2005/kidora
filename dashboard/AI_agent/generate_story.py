# from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
# from langchain_core.output_parsers import StrOutputParser
# import os
# from dotenv import load_dotenv
# from .prompt_templates import generate_story_prompt

# load_dotenv()


# def generate_story(question: str):
#     """Generates a story using a language model and returns the response."""

#     llm = ChatGoogleGenerativeAI(
#         model="gemini-pro",
#         temperature=0.6,
#         google_api_key=os.getenv("GOOGLE_API_KEY"),
#         convert_system_message_to_human=True
#     )

#     prompt = generate_story_prompt()

#     chain = prompt | llm | StrOutputParser()
#     return chain.invoke({"question": question})
def generate_story(question: str) -> str:
    # 🔥 TEMP DEMO STORY (NO GEMINI)
    return """
**STORY SETTING:**
A sunny park

**STORY STYLE:**
Cartoon, kids illustration

**MAIN CHARACTER:**
A detective duck wearing a coat

**Here is your story in 5 magical steps:**

**1.**
The detective duck arrives at the park.
**Visual Scene Description:**
A duck in detective clothes standing in a green park.

**2.**
He finds clues near a basket.
**Visual Scene Description:**
Duck examining a basket with a magnifying glass.

**3.**
He talks to animals.
**Visual Scene Description:**
Duck talking to squirrels and birds.

**4.**
He discovers a hidden nest.
**Visual Scene Description:**
Duck looking at a nest behind bushes.

**5.**
The egg is returned safely.
**Visual Scene Description:**
Happy duck returning the egg.
"""
