def generate_summary(text, max_length=150):
    """Basic summary generator (replace with GPT/LLAMA3 integration)"""
    if len(text) <= max_length:
        return text
    return text[:max_length] + '...'

# For advanced usage: Integrate with Llama3 or OpenAI API