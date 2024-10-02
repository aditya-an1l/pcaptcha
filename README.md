# 🔐 PCAPTCHA - Captcha Generation using Python

## v0.1.0: Bare Minimum ⚙️ 
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/downloads/)

This is an initial development version.

## Features 🚀

- Generate captcha images
- Generate corresponding captcha text
- Written in Python

## Installation 🛠️

1. Clone this repository:
   ```
   git clone https://github.com/aditya-an1l/pcaptcha.git
   cd pcaptcha
   ```

2. Set up a virtual environment:

On Unix
   ```
   python -m venv venv
   source venv/bin/activate 
   ```
On Windows
   ```
   python -m venv venv
   source venv\Scripts\activate
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage ✅

1. Navigate to the `scripts` directory:
   ```
   cd scripts
   ```

2. Run the main script:
   ```
   python ./main.py
   ```

Generated captcha images will be stored in the `scripts/media` directory.

## Project Structure 📁

```
pcaptcha/
├── scripts/
│   ├── main.py
│   └── media/
├── venv/
├── requirements.txt
└── README.md
```

## Known Limitations ⚠️

1. The application is entirely CLI-based with no GUI.
2. By default, it overwrites the previous captcha image unless an alternate name is provided in the script.

## Future Enhancements 🔮

1. Make the CLI more interactive
2. Implement a better naming mechanism for captcha images
3. Develop a GUI mode

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

