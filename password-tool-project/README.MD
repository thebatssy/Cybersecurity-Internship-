# 🔐 Password Strength Analyzer & Wordlist Generator

A simple command-line tool to analyze password strength and generate custom wordlists using personal information and leetspeak transformations.

## 🎯 Objective
To assist in cybersecurity practice by:
- Evaluating password strength
- Creating wordlists based on user-specific data

## 🛠️ Features
- Password strength analysis using `zxcvbn`
- Leetspeak word variants
- Common suffix additions (e.g., `123`, `2024`, `@`, etc.)
- Word combinations and permutations
- Wordlist saved as a `.txt` file

## 🧰 Technologies Used
- Python 3.x
- `argparse` – for command-line arguments
- `zxcvbn` – for password strength analysis
- `nltk` – for tokenizing personal inputs
- `itertools` – for generating combinations
- `os` (optional) – for handling file paths and checks

## 🚀 How to Run

```bash
python password_tool.py --password yourPass123 --name John --dob 01/01/2000 --output wordlist.txt
```

You can also add:
- `--pet` for pet name
- `--partner` for partner name
- `--extra` for any other relevant info

## 📂 Output Example

```
[Password Analysis]
Password: yourPass123
Score: 3 / 4
Guesses needed: 34000
Feedback: Add another word or two. Uncommon words are better.

[+] Wordlist saved to 'wordlist.txt' with 243 entries.
```

The file `wordlist.txt` will contain generated password guesses like:

```
john
john123
j0hn!
john2024
j0hn2025
...
```

## 📁 Project Structure

```
password_tool_project/
│
├── password_tool.py
├── README.md
├── wordlist.txt               # (Generated after running)
└── nltk_data/                 # (If used offline for tokenizers)
```

## ⚠️ Disclaimer

> This tool is developed for **educational and ethical cybersecurity purposes only**.  
> Do **not** use this tool to attempt unauthorized access to systems or user accounts.  
> The developer is **not responsible** for any misuse or damage caused by this tool.
