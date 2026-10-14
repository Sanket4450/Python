import json

test1 = '{"name": "John", "age": 30, "city": "New York"}'
parsed1 = json.loads(test1)

print(parsed1)  # {'name': 'John', 'age': 30, 'city': 'New York'}

test2 = {
    "name": "Jane",
    "age": 25,
    "city": "Los Angeles",
    "is_student": False,
    "courses": ["Math", "Science", "History"],
    "address": {"zip_code": "90001", "street": "123 Main St"},
}

converted1 = json.dumps(
    test2, indent=4, sort_keys=True
)  # Convert Python object to JSON string with indentation of 4 spaces for readability with sorted keys
print(converted1)

# Supported data types for JSON serialization include:
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print(json.loads("null"))  # None
