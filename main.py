from tools.basic_calculator import basic_calculator
from tools.reverser import reverse_string
from agents.agent import Agent

def main():
    tools = [basic_calculator, reverse_string]

    agent = Agent(tools)

    while True:
        prompt = input("Ask me anything: ")
        if prompt.lower() == "exit":
            break

        agent.work(prompt)

if __name__ == "__main__":
    main()
