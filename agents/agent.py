from toolbox.toolbox import ToolBox
from prompts.prompts import agent_system_prompt_template
from models.google_genai_models import LLMClient
from models.tool_result import ToolResult
from langchain_core.output_parsers import PydanticOutputParser
from termcolor import colored

class Agent:
    def __init__(self, tools):
        self.tools = tools
        self.parser = PydanticOutputParser(pydantic_object=ToolResult)

    def prepare_tools(self):
        toolbox = ToolBox()
        toolbox.store(self.tools)
        tool_descriptions = toolbox.tools()
        return tool_descriptions
    
    def think(self, prompt):
        tool_descriptions = self.prepare_tools()
        model = LLMClient()
        model_response = model.generate_text(
            system_prompt=agent_system_prompt_template,
            user_prompt=prompt,
            partial_variables={"tool_descriptions": tool_descriptions},
            input_variables=["user_input", "tool_descriptions"]
        )

        return model_response
    
    def work(self, prompt):
        model_response = self.think(prompt)
        print(colored(model_response, "red"))
        parsed = self.parser.parse(model_response)

        tool_choice = parsed.tool_choice
        tool_input = parsed.tool_input

        for tool in self.tools:
            if tool.__name__ == tool_choice:
                response = tool(tool_input)
                print(colored(response, 'cyan'))
                return

        print(colored(tool_input, 'cyan'))
        return            