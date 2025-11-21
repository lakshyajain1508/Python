# 🐍 Python Regular Expressions (Regex)

Regular Expressions, often shortened to **Regex**, are powerful tools for sophisticated **string processing** in Python. They allow you to define patterns to search, match, and manipulate text data efficiently.

This guide is based on examples using Python's built-in **`re` module**.

---

## 🚀 Getting Started

The first step in using regex in Python is to import the `re` module.

```python
# Regex or Regular Expression
import re # re - regular
````

-----

## 🔍 Core Matching Functions

The Python `re` module provides several functions for pattern matching, the most common of which are `re.match()` and `re.search()`.

### 1\. `re.match()`

The `re.match()` function attempts to match the pattern **only at the beginning** of the string.

  * If the pattern is found at the start, it returns a **Match Object**.
  * Otherwise, it returns **`None`**.

#### Example: Pattern at the Start

```python
text = "Lakshya Web Coder"
Pattern = r"Lakshya" # Pattern is at the start
match = re.match(Pattern, text)

if match:
  print("Match Found - ", match.group()) # Output: Match Found -  Lakshya
else:
  print("No Match Found")
```

### 2\. `re.search()`

The `re.search()` function scans the **entire string** to find the *first* location where the pattern produces a match.

  * It returns a **Match Object** for the first match found anywhere in the string.
  * It returns **`None`** if no match is found.

#### Example: Pattern Not at the Start

```python
text = "Lakshya Web Coder"
Pattern = r"Coder" # Pattern is in the middle/end
match = re.search(Pattern, text)

if match:
  print("Match Found - ", match.group()) # Output: Match Found -  Coder
else:
  print("No Match Found")
```

> **🔑 Key Difference:** Use `re.match()` when you need to ensure the string **begins** with the pattern, and use `re.search()` to find the pattern **anywhere** within the string.

-----

## 🛠️ Matching with User Input

You can easily integrate `re.search()` with user input to make your pattern matching dynamic.

```python
text = "Lakshya Web Coder"
text_data = input("Enter search word : ") # User enters "Web"
Pattern = text_data
match = re.search(Pattern,text)

if match:
  print("Match Found - ",match.group()) # Output: Match Found -  Web
else:
  print("No Match Found")
```

-----

## ⚙️ Regex Flags

Flags modify how a regular expression searches for a match. They are passed as an optional third argument to the `re` functions.

### 1\. `re.IGNORECASE`

The `re.IGNORECASE` flag makes the matching case-insensitive.

```python
text = "Lakshya Web Coder"
Pattern = r"web" # Lowercase pattern
match = re.search(Pattern, text, re.IGNORECASE)

if match:
  print("Match Found - ",match.group()) # Output: Match Found -  Web
# The re.IGNORECASE flag allows r"web" to match "Web" regardless of case.
```

### 2\. `re.MULTILINE`

The `re.MULTILINE` flag changes the behavior of the start-of-string character (`^`) and the end-of-string character (`$`).

  * With this flag, `^` matches the **beginning of the string** *and* the **beginning of every line** (after a newline `\n`).
  * `re.findall()` returns a list of all non-overlapping matches.

<!-- end list -->

```python
sen = "match here \nmatch there \nmatch is not found"
pattern = r"^match" # Looks for 'match' at the start of a line

match = re.findall(pattern, sen, re.MULTILINE)
print(match) # Output: ['match', 'match', 'match']

int_m = len(match)
print("Find", int_m, "matches in this data.") # Output: Find 3 matches in this data.
```

-----

## ✨ Advanced Matching with Metacharacters

Metacharacters are characters with special meaning in a regex pattern.

| Metacharacter | Description | Example |
| :--- | :--- | :--- |
| `.` | Matches any character (except newline) | `r"f.x"` matches "fax", "fex", "fox", etc. |
| `^` | Matches the start of the string (or line with `re.MULTILINE`) | `r"^Hello"` matches a string that starts with "Hello" |
| `$` | Matches the end of the string (or line with `re.MULTILINE`) | `r"World$"` matches a string that ends with "World" |
| `*` | Zero or more occurrences of the preceding element | `r"a*"` matches "", "a", "aa", "aaa", etc. |
| `+` | One or more occurrences of the preceding element | `r"a+"` matches "a", "aa", "aaa", but not "" |
| `?` | Zero or one occurrence of the preceding element | `r"colou?r"` matches "color" or "colour" |
| `{n}` | Exactly $n$ occurrences of the preceding element | `r"a{3}"` matches "aaa" |
| `[ ]` | A set of characters | `r"[a-m]"` matches any lowercase letter from a to m |
| `( )` | A capturing and grouping mechanism | `r"(ab)+"` matches "ab", "abab", "ababab", etc. |
| `\` | Used to escape special characters or signal a special sequence | `r"\."` matches a literal dot character |

### Special Sequences

Special sequences are combinations of `\` and a character that have a predefined meaning:

| Sequence | Description | Example |
| :--- | :--- | :--- |
| `\d` | Matches any **digit** (0-9) | `r"\d{3}"` matches "123" |
| `\D` | Matches any **non-digit** character | `r"\D"` matches "a", "\!", " " |
| `\w` | Matches any **word character** (a-z, A-Z, 0-9, and \_) | `r"Hello\w"` matches "HelloA", "Hello\_1" |
| `\W` | Matches any **non-word character** | `r"\W"` matches "$", "#", " " |
| `\s` | Matches any **whitespace** character (space, tab, newline) | `r"\s"` matches " " |
| `\S` | Matches any **non-whitespace** character | `r"\S"` matches "a", "1", "$" |
| `\b` | Matches a **word boundary** (start or end of a word) | `r"\bword\b"` matches "word" but not "sword" |

### Example: Finding Digits

```python
text = "The code is 404 and the year is 2025."
pattern = r"\d+" # Matches one or more digits

# re.findall() returns a list of all non-overlapping matches
matches = re.findall(pattern, text)
print(matches) # Output: ['404', '2025']
```


