import re

text = """
Product 123 costs $450.
Product 456 costs $700.
Product 789 costs $1200.
"""

numbers = re.findall(r"\d+", text)

print(numbers)
