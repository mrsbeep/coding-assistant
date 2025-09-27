# 🤖 AI Coding Assistant

An intelligent command-line tool that helps every developer code better using OpenAI's powerful language models.

## ✨ Features

- **Ask Questions**: Get instant help with coding problems, debugging, and best practices
- **Code Analysis**: Analyze your code files for potential issues, optimizations, and improvements
- **Code Generation**: Generate code snippets based on natural language descriptions
- **Multi-language Support**: Works with Python, JavaScript, Java, C++, and many more languages
- **Easy Setup**: Simple .env configuration with your OpenAI API key

## 🚀 Quick Start

> **📖 New to the assistant? Check out our [Getting Started Guide](GETTING_STARTED.md) for a step-by-step walkthrough!**

### 1. Clone and Install

```bash
git clone https://github.com/mrsbeep/coding-assistant.git
cd coding-assistant
pip install -r requirements.txt
```

### 2. Configure OpenAI API Key

Copy the example environment file and add your OpenAI API key:

```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=sk-your-actual-api-key-here
```

### 3. Test Your Setup

```bash
python coding_assistant.py setup
```

## 📖 Usage

### Ask for Coding Help

```bash
# Basic question
python coding_assistant.py ask "How do I reverse a string in Python?"

# With language context
python coding_assistant.py ask "How to handle exceptions?" --language python

# With additional context
python coding_assistant.py ask "Optimize this algorithm" --context "Working with large datasets"
```

### Analyze Code Files

```bash
python coding_assistant.py analyze my_script.py
python coding_assistant.py analyze src/main.js
```

### Generate Code

```bash
# Generate code snippet
python coding_assistant.py generate "Create a function to calculate factorial"

# Generate for specific language
python coding_assistant.py generate "REST API endpoint for user authentication" --language python

# Save to file
python coding_assistant.py generate "Binary search algorithm" --language python --output binary_search.py
```

## 🛠 Installation as CLI Tool

For easier access, install as a command-line tool:

```bash
pip install -e .
```

Then use with shorter commands:
```bash
coding-assistant ask "How to use decorators in Python?"
ca analyze my_file.py  # 'ca' is a short alias
```

## 🔧 Configuration Options

### Environment Variables

Create a `.env` file with the following options:

```bash
# Required: Your OpenAI API key
OPENAI_API_KEY=sk-your-api-key-here

# Optional: Choose your preferred model (default: gpt-3.5-turbo)
OPENAI_MODEL=gpt-4
# OPENAI_MODEL=gpt-3.5-turbo
```

### Supported Models

- `gpt-3.5-turbo` (default, faster and cheaper)
- `gpt-4` (more capable but slower and more expensive)

## 💡 Examples

### Getting Help with Debugging

```bash
python coding_assistant.py ask "My Python script has a memory leak, how can I debug it?" --language python
```

### Code Review

```bash
python coding_assistant.py analyze examples/sample_flask_app.py
```

### Learning New Concepts

```bash
python coding_assistant.py ask "Explain async/await in JavaScript with examples" --language javascript
```

### Generating Boilerplate

```bash
python coding_assistant.py generate "Express.js server with JWT authentication" --language javascript --output server.js
```

> **📚 More examples available in [examples/usage_examples.md](examples/usage_examples.md)**

## 🎯 Use Cases

- **Learning**: Get explanations and examples for new programming concepts
- **Debugging**: Help identify and fix bugs in your code
- **Code Review**: Get suggestions for code improvements and optimizations
- **Boilerplate Generation**: Quickly generate common code patterns
- **Best Practices**: Learn industry standards and best practices
- **Refactoring**: Get suggestions for cleaner, more maintainable code

## 📋 Requirements

- Python 3.7 or higher
- OpenAI API key
- Internet connection

## 🤝 Contributing

Feel free to open issues and submit pull requests to improve this coding assistant!

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Troubleshooting

### "OPENAI_API_KEY not found"
- Make sure you've created a `.env` file with your API key
- Check that the key starts with `sk-` and is valid

### "API connection failed"
- Verify your API key is correct and has sufficient credits
- Check your internet connection
- Ensure you're using a supported model name

### Commands not working
- Make sure you've installed all requirements: `pip install -r requirements.txt`
- Try running the setup command: `python coding_assistant.py setup`
