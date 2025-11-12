# Qutrub-ng: Modern Arabic Verb Conjugation

## قطرب: تصريف الأفعال العربية

A modern, development-focused fork of the Qutrub Arabic verb conjugation software, optimized for Jupyter notebook development and research.

**🔬 Development Focus**: This repository prioritizes notebook-based exploration, testing, and development of Arabic verb conjugation algorithms.

**📚 Original Project**: Based on the work of Taha Zerrouki ([tahadz.com](http://tahadz.com))

---

## Quick Start with Jupyter

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Launch Jupyter

```bash
jupyter notebook qutrub_notebook.ipynb
```

### 3. Start Conjugating

```python
import libqutrub.conjugator

# Basic conjugation
verb = "كَتَبَ"
table = libqutrub.conjugator.conjugate(verb, "فتحة", transitive=True)
print(table)
```

---

## Features

- 🎯 **Comprehensive Conjugation**: Support for all Arabic verb forms (Regular, Irregular, Defective)
- 📖 **Notebook-Ready**: Optimized for interactive development and research
- 🌐 **Multiple Formats**: HTML, CSV, XML, TeX, and more
- 🔍 **Validation**: Built-in verb validation and suggestions
- 🧪 **Extensible**: Easy to extend with new conjugation rules
- 📊 **API Ready**: RESTful API integration

---

## Development Setup

### Requirements
- Python 3.7+
- pyarabic>=0.6.2

### Installation

```bash
# Clone the repository
git clone https://github.com/msylergy/qutrub-ng.git
cd qutrub-ng

# Install dependencies
pip install -r requirements.txt

# Start developing with the notebook
jupyter notebook qutrub_notebook.ipynb
```

---

## Library Usage

### Basic Conjugation

```python
import libqutrub.conjugator

verb = "سعد"
future_type = "كسرة"
table = libqutrub.conjugator.conjugate(verb, future_type, transitive=True)
print(table)
```

### Advanced Options

```python
import libqutrub.conjugator

verb = "كَتَبَ"
future_type = "ضمة"

# All conjugation options
table = libqutrub.conjugator.conjugate(
    verb,
    future_type,
    all=True,           # all tenses
    past=True,         # past tense
    future=True,       # future tense
    passive=True,      # passive voice
    imperative=True,   # imperative mood
    future_moode=True, # subjunctive/jussive
    confirmed=False,   # confirmed form
    transitive=True,   # transitive verb
    display_format="HTML"  # output format
)
```

### Display Formats

Available formats:
- `'Text'`
- `'HTML'`
- `'HTMLColoredDiacritics'`
- `'DICT'`
- `'CSV'`
- `'GUI'`
- `'TABLE'`
- `'XML'`
- `'TeX'`
- `'ROWS'`

---

## Web API

For API documentation, see [doc/api.md](doc/api.md)

---

## Testing

```bash
# Run all tests
python -m pytest tests/

# Run specific test suite
python -m pytest tests/test_conjugate.py
```

---

## Project Structure

```
├── libqutrub/           # Core conjugation library
├── qutrub_notebook.ipynb # Development notebook
├── tests/               # Test suite
├── config/              # Configuration files
├── interfaces/          # GUI and web interfaces
├── data/               # Verb databases
└── tools/              # Utility scripts
```

---

## Contributing

This is a development-focused fork. Contributions are welcome, especially:
- 🧪 Improvements to the Jupyter notebook
- 🔧 Library enhancements
- 📝 Documentation improvements
- 🐛 Bug fixes and optimizations

---

## License

GPL License (see [COPYING](COPYING))

---

## Original Project

Based on [Qutrub](https://github.com/linuxscout/qutrub) by Taha Zerrouki

Developer: Taha Zerrouki
Email: taha dot zerrouki at gmail dot com
Website: [qutrub.arabeyes.org](http://qutrub.arabeyes.org)