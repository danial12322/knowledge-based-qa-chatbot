"""
Main Chatbot Interface
Provides both CLI and interactive interface for the QA chatbot
"""

from knowledge_base import KnowledgeBase
from qa_engine import QAEngine

def main():
    """
    Main function to run the chatbot
    """
    # Initialize knowledge base and QA engine
    kb = KnowledgeBase()
    qa_engine = QAEngine(kb)
    
    print("\n" + "="*60)
    print("Welcome to the Knowledge-Based QA Chatbot")
    print("Ask me questions about courses and staff")
    print("Type 'quit' or 'exit' to exit")
    print("="*60 + "\n")
    
    while True:
        try:
            user_query = input("You: ").strip()
            
            if not user_query:
                print("Bot: Please ask a question.\n")
                continue
            
            if user_query.lower() in ['quit', 'exit', 'bye']:
                print("Bot: Goodbye! Have a great day!\n")
                break
            
            # Process query and get response
            response = qa_engine.process_query(user_query)
            print(f"Bot: {response}\n")
            
        except KeyboardInterrupt:
            print("\nBot: Goodbye!")
            break
        except Exception as e:
            print(f"Bot: An error occurred: {str(e)}")
            print("Please try again.\n")

if __name__ == "__main__":
    main()
