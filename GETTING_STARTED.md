# 🚀 Getting Started with AI Coding Assistant

This guide will help you get started with the AI Coding Assistant in just a few minutes!

## Step 1: Get Your OpenAI API Key

1. Go to [OpenAI's website](https://platform.openai.com/api-keys)
2. Sign up or log in to your account
3. Navigate to "API Keys" section
4. Click "Create new secret key"
5. Copy your API key (starts with `sk-`)

## Step 2: Setup the Coding Assistant

```bash
# Clone the repository
git clone https://github.com/mrsbeep/coding-assistant.git
cd coding-assistant

# Install dependencies
pip install -r requirements.txt

# Copy the environment template
cp .env.example .env
```

## Step 3: Configure Your API Key

Edit the `.env` file and add your API key:
```
OPENAI_API_KEY=sk-your-actual-api-key-here
```

## Step 4: Verify Setup

```bash
python coding_assistant.py setup
```

You should see:
```
🔧 AI Coding Assistant Setup
==============================
✅ .env file found
✅ OpenAI API key is configured
✅ API connection successful
🎉 Setup complete! You're ready to use the coding assistant.
Model: gpt-3.5-turbo
```

## Step 5: Start Using the Assistant!

### Ask Questions
```bash
python coding_assistant.py ask "How do I reverse a string in Python?"
```

### Analyze Code
```bash
python coding_assistant.py analyze my_script.py
```

### Generate Code
```bash
python coding_assistant.py generate "Create a function to validate email addresses"
```

## Step 6: Install as CLI Tool (Optional)

For easier access, install the package:
```bash
pip install -e .
```

Now you can use shorter commands:
```bash
coding-assistant ask "How to use decorators?"
ca analyze my_file.py  # 'ca' is the short alias
```

## 🎉 You're Ready!

You now have a powerful AI coding assistant at your fingertips. Happy coding!