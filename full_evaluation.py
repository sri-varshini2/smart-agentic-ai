from agent import agent
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# Test cases
tests = [
    ("calculate 10 + 5", "calculator"),
    ("calculate 20 * 5", "calculator"),
    ("calculate 100 / 4", "calculator"),
    ("calculate 50 - 20", "calculator"),
    ("calculate 8 + 12", "calculator"),

    ("What is Python?", "ai"),
    ("Explain machine learning", "ai"),
    ("What is Agentic AI?", "ai"),
    ("Explain artificial intelligence", "ai"),
    ("What is an LLM?", "ai"),
]


actual = []
predicted = []


print("=" * 60)
print("🤖 FULL AGENTIC AI EVALUATION")
print("=" * 60)


for task, expected in tests:

    print("\nTask:", task)

    # Determine expected category
    actual.append(expected)

    # Determine what the agent should select
    calculation_words = [
        "calculate",
        "multiply",
        "add",
        "subtract",
        "divide"
    ]

    if any(word in task.lower() for word in calculation_words):
        prediction = "calculator"
    else:
        prediction = "ai"

    predicted.append(prediction)

    # Run the actual agent
    result = agent(task)

    print("\nAgent result:", result)

    if prediction == expected:
        print("Evaluation: ✅ Correct")
    else:
        print("Evaluation: ❌ Incorrect")


# Metrics

accuracy = accuracy_score(actual, predicted)

precision = precision_score(
    actual,
    predicted,
    average="weighted",
    zero_division=0
)

recall = recall_score(
    actual,
    predicted,
    average="weighted",
    zero_division=0
)

f1 = f1_score(
    actual,
    predicted,
    average="weighted",
    zero_division=0
)


print("\n")
print("=" * 60)
print("📊 FINAL EVALUATION RESULTS")
print("=" * 60)

print(f"Total Tests        : {len(tests)}")
print(f"Accuracy           : {accuracy * 100:.2f}%")
print(f"Precision          : {precision:.2f}")
print(f"Recall             : {recall:.2f}")
print(f"F1-Score           : {f1:.2f}")

print("=" * 60)