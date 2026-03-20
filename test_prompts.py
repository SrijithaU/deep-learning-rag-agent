from prompts import build_question_prompt, build_guard_prompt

# Sample context
context = """
Convolutional Neural Networks (CNNs) are used for image processing.
They extract features using convolution layers.
"""

# Test 1: Question generation
print("=== Question Generation ===")
print(build_question_prompt(context))

print("\n-----------------\n")

# Test 2: Valid query
print("=== Valid Query ===")
print(build_guard_prompt(context, "What is CNN?"))

print("\n-----------------\n")

# Test 3: Off-topic query
print("=== Off Topic Query ===")
print(build_guard_prompt(context, "Who won FIFA 2018?"))
