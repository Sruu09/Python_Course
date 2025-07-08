'''
Operator overloading means giving special meaning to standard operators (+, -, *, etc.) when used with user-defined objects.

Example: Using + to add two objects.

| Operator | Method Name            |
| -------- | ---------------------- |
| `+`      | `__add__(self, other)` |
| `-`      | `__sub__(self, other)` |
| `*`      | `__mul__(self, other)` |
| `==`     | `__eq__(self, other)`  |
| `<`      | `__lt__(self, other)`  |
| `>`      | `__gt__(self, other)`  |
| `str()`  | `__str__(self)`        |

'''
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"{self.x}i + {self.y}j"

v1 = Vector(2, 3)
v2 = Vector(1, 4)

result = v1 + v2  # __add__ called
print(result)     # 3i + 7j
