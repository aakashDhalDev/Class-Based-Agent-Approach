from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

class LLMClient:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash-lite",
            temperature=0
        )

    def generate_text(
            self, 
            system_prompt: str, 
            user_prompt: str, 
            partial_variables: dict[str,str] = None, 
            input_variables: dict[str,str] = None):

        template = ChatPromptTemplate.from_messages(
            [
                ("system", "{system_prompt}"),
                ("user", "{user_prompt}")
            ]
        )

        if partial_variables:
            template = template.partial(**partial_variables)

        prompt_value = template.format_prompt(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            input_variables=input_variables
        )

        messages = prompt_value.to_messages()

        response = self.llm.invoke(messages)

        return response.content