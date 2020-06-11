# movie_review_API



**DB**

```python
import json

dict = {"member #002":{"first name": "John", "last name": "Doe", "age": 34},
        "member #003":{"first name": "Elijah", "last name": "Baley", "age": 27},
        "member #001":{"first name": "Jane", "last name": "Doe", "age": 42}}

with open('data.json', 'w') as fp:
    json.dump(dict, fp)
```

