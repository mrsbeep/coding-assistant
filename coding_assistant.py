#!/usr/bin/env python3
"""
AI Coding Assistant

A command-line tool that helps developers with coding tasks using OpenAI's API.
"""

import os
import sys
import click
from dotenv import load_dotenv
from openai import OpenAI
from colorama import init, Fore, Back, Style
import json

# Initialize colorama for colored terminal output
init(autoreset=True)

class CodingAssistant:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()
        
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.model = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
        
        if not self.api_key:
            click.echo(f"{Fore.RED}Error: OPENAI_API_KEY not found in environment variables.")
            click.echo(f"{Fore.YELLOW}Please create a .env file with your OpenAI API key:")
            click.echo(f"{Fore.WHITE}OPENAI_API_KEY=your_api_key_here")
            click.echo(f"{Fore.CYAN}You can copy .env.example to .env and update it with your key.")
            sys.exit(1)
        
        try:
            self.client = OpenAI(api_key=self.api_key)
        except Exception as e:
            click.echo(f"{Fore.RED}Error initializing OpenAI client: {str(e)}")
            sys.exit(1)

    def get_code_help(self, prompt, language=None, context=None):
        """Get coding help from OpenAI API"""
        
        system_message = """You are an expert programming assistant. Help developers with:
- Code generation and completion
- Bug fixing and debugging
- Code optimization and refactoring
- Explaining complex code concepts
- Best practices and design patterns
- Testing strategies

Provide clear, practical, and well-commented code examples when appropriate."""

        user_message = prompt
        
        if language:
            user_message = f"Language: {language}\n\n{user_message}"
        
        if context:
            user_message = f"Context:\n{context}\n\nQuestion: {user_message}"

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.7,
                max_tokens=1500
            )
            
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            return f"Error getting AI response: {str(e)}"

    def analyze_code(self, code_content, filename=None):
        """Analyze code for potential issues and improvements"""
        
        prompt = f"""Please analyze the following code and provide:
1. Potential bugs or issues
2. Performance improvements
3. Code quality suggestions
4. Security concerns (if any)

Code:
```
{code_content}
```
"""
        
        if filename:
            prompt = f"Filename: {filename}\n\n{prompt}"
        
        return self.get_code_help(prompt)

    def generate_code(self, description, language=None):
        """Generate code based on description"""
        
        prompt = f"Generate code for: {description}"
        
        if language:
            prompt = f"Generate {language} code for: {description}"
        
        return self.get_code_help(prompt, language)

# CLI Interface
@click.group()
@click.version_option(version='1.0.0')
def cli():
    """AI Coding Assistant - Help every developer code better!"""
    pass

@cli.command()
@click.argument('prompt')
@click.option('--language', '-l', help='Programming language context')
@click.option('--context', '-c', help='Additional context for the question')
def ask(prompt, language, context):
    """Ask the AI assistant for coding help"""
    
    assistant = CodingAssistant()
    
    click.echo(f"{Fore.CYAN}🤖 AI Coding Assistant")
    click.echo(f"{Fore.WHITE}Question: {prompt}")
    
    if language:
        click.echo(f"{Fore.YELLOW}Language: {language}")
    
    if context:
        click.echo(f"{Fore.YELLOW}Context: {context}")
    
    click.echo(f"{Fore.GREEN}{'='*50}")
    
    response = assistant.get_code_help(prompt, language, context)
    click.echo(response)

@cli.command()
@click.argument('file_path', type=click.Path(exists=True))
def analyze(file_path):
    """Analyze a code file for issues and improvements"""
    
    assistant = CodingAssistant()
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code_content = f.read()
        
        click.echo(f"{Fore.CYAN}🔍 Analyzing: {file_path}")
        click.echo(f"{Fore.GREEN}{'='*50}")
        
        analysis = assistant.analyze_code(code_content, os.path.basename(file_path))
        click.echo(analysis)
        
    except Exception as e:
        click.echo(f"{Fore.RED}Error reading file: {str(e)}")

@cli.command()
@click.argument('description')
@click.option('--language', '-l', help='Programming language for the code')
@click.option('--output', '-o', type=click.Path(), help='Save generated code to file')
def generate(description, language, output):
    """Generate code based on description"""
    
    assistant = CodingAssistant()
    
    click.echo(f"{Fore.CYAN}⚡ Generating code...")
    click.echo(f"{Fore.WHITE}Description: {description}")
    
    if language:
        click.echo(f"{Fore.YELLOW}Language: {language}")
    
    click.echo(f"{Fore.GREEN}{'='*50}")
    
    code = assistant.generate_code(description, language)
    click.echo(code)
    
    if output:
        try:
            with open(output, 'w', encoding='utf-8') as f:
                f.write(code)
            click.echo(f"{Fore.GREEN}✅ Code saved to: {output}")
        except Exception as e:
            click.echo(f"{Fore.RED}Error saving file: {str(e)}")

@cli.command()
def setup():
    """Setup the coding assistant (check configuration)"""
    
    click.echo(f"{Fore.CYAN}🔧 AI Coding Assistant Setup")
    click.echo(f"{Fore.GREEN}{'='*30}")
    
    # Check for .env file
    if os.path.exists('.env'):
        click.echo(f"{Fore.GREEN}✅ .env file found")
    else:
        click.echo(f"{Fore.YELLOW}⚠️  .env file not found")
        click.echo(f"{Fore.WHITE}Copy .env.example to .env and add your OpenAI API key")
        return
    
    # Check API key
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    
    if api_key:
        if api_key.startswith('sk-') and len(api_key) > 20:
            click.echo(f"{Fore.GREEN}✅ OpenAI API key is configured")
            
            # Test API connection
            try:
                assistant = CodingAssistant()
                test_response = assistant.get_code_help("Say 'Hello, World!' in Python", "python")
                if "print" in test_response.lower() or "hello" in test_response.lower():
                    click.echo(f"{Fore.GREEN}✅ API connection successful")
                    click.echo(f"{Fore.CYAN}🎉 Setup complete! You're ready to use the coding assistant.")
                else:
                    click.echo(f"{Fore.RED}❌ Unexpected API response")
            except Exception as e:
                click.echo(f"{Fore.RED}❌ API connection failed: {str(e)}")
        else:
            click.echo(f"{Fore.RED}❌ Invalid API key format")
    else:
        click.echo(f"{Fore.RED}❌ OPENAI_API_KEY not set in .env file")
    
    # Show model info
    model = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
    click.echo(f"{Fore.WHITE}Model: {model}")

if __name__ == '__main__':
    cli()