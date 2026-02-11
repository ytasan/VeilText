# VeilText - Text Censorship Tool

This Python script automatically censors text according to specific rules.

## 📌 How It Works

The program:

1. Reads the `VeilText.input` file.
2. Censors lines that start with a `*` character.
3. Leaves lines without `*` unchanged.
4. Writes the result to `VeilText.output`.

---

## 🔎 Censorship Rules

For each word:

- **3-letter words** → `...`
- **4-letter words** → `....`
- **1–2 letter words** → left unchanged
- **5 or more letters** →  
  - First letter is kept  
  - Last letter is kept  
  - All letters in between are replaced with `.`  

Example:

```
word    → w..d
example → e.....e
we      → we
```

---

## 📂 File Structure

The following files should be in the same folder:

```
VeilText.input
VeilText.py
```

After the program runs, this file is created:

```
VeilText.output
```

---

## ▶️ Usage

From the terminal:

```bash
python VeilText.py
```

No parameters are required. The program always reads:

```
VeilText.input
```

---

## 🧠 Important Details

- Leading indentation on lines is preserved.
- Spaces between words are preserved.
- Only lines starting with `*` are censored.
- The `*` character is not written to the output file.

---

## 📝 Sample Input

```
Normal line.
*            1. an example sentence here
```

## 📝 Sample Output

```
Normal line.
            1. an e.....e s.......e h..e
```

---

## 🗺️ Future Plans

- **Modular structure**: Refactor into separate modules (e.g. I/O, censorship rules, word processing) for maintainability.
- **Regex usage**: Document and optionally expose pattern-based logic for line detection and word censoring.
- **Development notes**: Add a section for contributors (setup, testing, design decisions).
