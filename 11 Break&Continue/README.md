
# Break & Continue

Control flow tools like `break` and `continue` are used in loops to alter their normal behavior. These are especially useful for managing complex looping conditions and improving code clarity.

---

## What is `break` in Python?

The `break` statement is used to **exit a loop immediately**, even if the condition of the loop hasn't become `False`.

### Syntax:

```python
for variable in sequence:
    if condition:
        break
```

### Example:

```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
```

**Output:**
```
1
2
```

> As soon as `i == 3`, the loop terminates.

---

## What is `continue` in Python?

The `continue` statement **skips the current iteration** and moves to the next iteration of the loop.

### Syntax:

```python
for variable in sequence:
    if condition:
        continue
```

### Example:

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

**Output:**
```
1
2
4
5
```

> When `i == 3`, the `continue` skips that iteration.

---

## Comparison Table

| Feature     | `break`                         | `continue`                         |
|-------------|----------------------------------|------------------------------------|
| Purpose     | Exits the loop entirely          | Skips to the next iteration        |
| Placement   | Typically in `if` conditionals   | Same                               |
| Usage       | When loop should stop early      | When some values should be skipped |

---

## When to Use?

- Use **`break`** when a certain condition **requires the loop to stop**.
- Use **`continue`** to **skip over unwanted values** or conditions.

---

## Real-world Example

```python
names = ["Alice", "Bob", "Eve", "Admin", "Charlie"]

for name in names:
    if name == "Admin":
        break
    if name.startswith("E"):
        continue
    print(name)
```

**Output:**
```
Alice
Bob
```

> `"Eve"` is skipped using `continue`, and `"Admin"` stops the loop with `break`.

---

## Summary

- `break` ➡️ exits the loop immediately.
- `continue` ➡️ skips the current iteration and continues.
- Both improve code control inside loops.
