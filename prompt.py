def format_prompt(user_input):
    """
    Generates a structured prompt for Phi-2 to behave like a chatbot.
    """
    return f"""
    
    Example interactions:
    User: Hello
    AI: Hi there! How can I help you today?
    
    User: Tell me about machine learning.
    AI: Machine learning is a branch of AI that enables computers to learn from data without being explicitly programmed.

    Now, continue the conversation:
    
    User: {user_input}
    AI:
    """
