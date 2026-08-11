from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# Test cases
tests = [
    ("calculate 10 + 5", "calculator"),
    ("calculate 20 * 5", "calculator"),
    ("calculate 100 / 4", "calculator"),
    ("calculate 50 - 20", "calculator"),
    ("multiply 6 * 7", "calculator"),

    ("What is Python?", "ai"),
    ("Explain machine learning", "ai"),
    ("What is Agentic AI?", "ai"),
    ("Explain artificial intelligence", "ai"),
    ("What is an LLM?", "ai"),
]


def predict(task):
    """
    Simulates the decision made by our agent.
    """

    calculation_words = [
        "calculate",
        "multiply",
        "add",
        "subtract",
        "divide"
    ]

    if any(word in task.lower() for word in calculation_words):
        return "calculator"

    return "ai"


actual = []
predicted = []

print("=" * 50)
print("🤖 AGENT EVALUATION")
print("=" * 50)

for task, expected in tests:

    result = predict(task)

    actual.append(expected)
    predicted.append(result)

    status = "✅" if result == expected else "❌"

    print(f"\nTask: {task}")
    print(f"Expected : {expected}")
    print(f"Predicted: {result}")
    print(f"Result   : {status}")


# Calculate metrics
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


print("\n" + "=" * 50)
print("📊 FINAL EVALUATION")
print("=" * 50)

print(f"Total Tests        : {len(tests)}")
print(f"Accuracy           : {accuracy * 100:.2f}%")
print(f"Precision          : {precision:.2f}")
print(f"Recall             : {recall:.2f}")
print(f"F1-Score           : {f1:.2f}")

print("=" * 50)