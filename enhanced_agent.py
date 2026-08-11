import ollama
from datetime import datetime

memory = []

def calculator(expression):
    try:
        return eval(expression)
    except:
        return "Invalid calculation"

def get_time():
    return datetime.now().strftime("%I:%M:%S %p")

def agent(task):
    print("\n🤖 Agent received:", task)
    print("🧠 Agent planning...")

    # Calculator tool
    if any(word in task.lower() for word in
           ["calculate", "multiply", "add", "subtract", "divide"]):

        print("🔧 Tool selected: Calculator")

        expression = (
            task.lower()
            .replace("calculate", "")
            .replace("multiply", "*")
            .replace("add", "+")
            .replace("subtract", "-")
            .replace("divide", "/")
        )

        result = calculator(expression)
        print("🧮 Result:", result)

        memory.append((task, str(result)))
        return f"The calculated result is {result}"

    # Time tool
    if "time" in task.lower():

        print("🔧 Tool selected: Time")
        result = get_time()

        memory.append((task, result))
        return f"The current time is {result}"

    # AI reasoning
    print("🤖 Tool selected: Ollama AI")

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful Agentic AI. Answer clearly and briefly."
            },
            {
                "role": "user",
                "content": task
            }
        ]
    )

    result = response["message"]["content"]
    memory.append((task, result))

    return result


print("=" * 45)
print("🤖 ENHANCED AGENTIC AI")
print("=" * 45)

while True:
    task = input("\nEnter task (type exit to stop): ")

    if task.lower() == "exit":
        print("\n📊 Session Summary")
        print("Tasks completed:", len(memory))
        break

    result = agent(task)

    print("\n🎯 FINAL RESULT:")
    print(result)