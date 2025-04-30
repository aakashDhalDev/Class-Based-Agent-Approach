from pydantic import BaseModel

class ToolResult(BaseModel):
    tool_choice: str
    tool_input: str
    