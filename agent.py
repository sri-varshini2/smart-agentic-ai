import ollama


def calculator(expression):
    try:
        return eval(expression)
    except:
        return "Invalid calculation"


def agent(task):
    print("\n🤖 Agent received:", task)
    print("🧠 Agent is planning...")

    # Decide whether calculator tool is needed
    if any(word in task.lower() for word in [
        "calculate",
        "multiply",
        "add",
        "subtract",
        "divide"
    ]):

        print("🔧 Agent selected: Calculator tool")

        expression = (
            task.lower()
            .replace("calculate", "")
            .replace("multiply", "")
            .replace("add", "")
            .replace("subtract", "")
            .replace("divide", "")
        )

        result = calculator(expression)

        print("🧮 Calculator result:", result)

        return str(result)

    # Otherwise use Llama
    print("🤖 Agent selected: Llama 3.2")

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "system",
                "content": """
You are a helpful Agentic AI.

For every task:
1. Understand the user's request.
2. Think about the task.
3. Provide a correct and useful answer.
"""
            },
            {
                "role": "user",
                "content": task
            }
        ]
    )

    return response["message"]["content"]


# Main program

print("================================")
print("🤖 AGENTIC AI WITH TOOLS")
print("================================")

task = input("\nEnter your task: ")

result = agent(task)

print("\n🎯 FINAL RESULT:")
print(result)