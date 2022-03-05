users = [
    {
        "id": 1,
        "first_name": "alex",
        "age": 31
    },
    {
        "id": 2,
        "first_name": "bob",
        "age": 32
    },
    {
        "id": 3,
        "first_name": "carl",
        "age": 33
    },
]
result = list(filter(lambda x: x["id"] == 3, users))
print(result[0] if result else [])
