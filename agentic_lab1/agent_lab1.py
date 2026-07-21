# Import Required Libraries
import os
import wikipedia
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType, Tool
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# Set User-Agent for Wikipedia requests
wikipedia.set_user_agent(
    "AgenticAILab/1.0 (student@example.com)"
)

# Load Environment Variables
load_dotenv()

# Initialize the LLM
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile",
    temperature=0
)

# Wikipedia Tool
wiki_wrapper = WikipediaAPIWrapper(
    top_k_results=1,
    doc_content_chars_max=500
)

wiki = WikipediaQueryRun(
    api_wrapper=wiki_wrapper
)

# Calculator Tool
def calculator(expression: str) -> str:
    """
    Evaluates a simple mathematical expression.
    Example:
        1879 * 2
    """

    try:
        # Allow only numbers and basic operators
        allowed = set("0123456789+-*/(). ")

        if not set(expression).issubset(allowed):
            return "Error: Invalid mathematical expression."

        result = eval(expression)
        return str(result)

    except Exception as e:
        return f"Error: {e}"
    
# Register Tools
tools = [
    Tool(
        name="Wikipedia",
        func=wiki.run,
        description=(
            "Use this tool only to retrieve factual information from Wikipedia. "
            "Do not use it for mathematical calculations."
        )
    ),

    Tool(
        name="Calculator",
        func=calculator,
        description="Use this tool only for arithmetic calculations such as addition, subtraction, multiplication, and division."
    )
]

# Create the ReAct Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    max_iterations=5,
    early_stopping_method="generate"
)

# User Question
question = (
    "Who developed the theory of relativity, "
    "and what is his birth year multiplied by 2?"
)

# Execute the Agent
response = agent.invoke(
    {"input": question}
)

# Print the Result
print("\n" + "=" * 40)
print("FINAL ANSWER")
print("=" * 40)


print(response["output"])
