# Knowledge-Based QA Chatbot

A comprehensive Knowledge-Based Question Answering system with rule-based responses for domain-specific information retrieval. This chatbot demonstrates information retrieval techniques and NLP concepts through an interactive interface.

## Features

- **Knowledge-Based System**: Structured domain-specific knowledge base with course and staff information
- **Rule-Based QA Engine**: Intent recognition and response generation based on predefined patterns
- **Natural Language Processing**: Keyword extraction and intent classification
- **Interactive CLI**: User-friendly command-line interface for chatbot interaction
- **Extensible Architecture**: Easy to add new courses, staff, or FAQ entries
- **Response Templates**: Template-based response generation for consistent output

## Project Structure

```
knowledge-based-qa-chatbot/
├── knowledge_base.py       # Knowledge base with courses and staff data
├── qa_engine.py            # QA engine with intent recognition
├── main.py                 # Main CLI interface
├── requirements.txt        # Project dependencies
├── README.md              # This file
└── .gitignore             # Git ignore rules
```

## Components

### 1. Knowledge Base (`knowledge_base.py`)

Manages domain-specific information:
- **Courses**: Python, JavaScript, Data Science, Web Design
- **Staff**: Instructors with contact and office hour information
- **FAQ**: Common questions about enrollment, prerequisites, certificates

### 2. QA Engine (`qa_engine.py`)

Implements question answering logic:
- **Intent Classification**: Identifies query type (course, staff, schedule, etc.)
- **Keyword Extraction**: Extracts relevant keywords from user input
- **Entity Matching**: Finds matching courses or staff based on keywords
- **Response Generation**: Creates contextual responses using templates

### 3. Main Interface (`main.py`)

Provides CLI interaction:
- Interactive chat loop
- User input handling
- Response display
- Error handling and exit management

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/knowledge-based-qa-chatbot.git
cd knowledge-based-qa-chatbot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Chatbot

```bash
python main.py
```

The chatbot will display a welcome message and wait for your questions.

### Example Queries

**Course Information:**
- "Tell me about Python course"
- "What courses are available?"
- "When is JavaScript scheduled?"

**Staff Information:**
- "Who is Dr. John Smith?"
- "Tell me about Emily Chen"
- "What are Sarah Johnson's office hours?"

**General Queries:**
- "How do I enroll in a course?"
- "What are the prerequisites?"
- "Do I get a certificate?"

### Exit Commands

Type any of these to exit:
- `quit`
- `exit`
- `bye`

## How It Works

1. **User Input**: User types a question
2. **Intent Recognition**: QA engine identifies query type
3. **Keyword Extraction**: Relevant terms are extracted
4. **Entity Matching**: Finds matching courses or staff
5. **Response Generation**: Creates response using templates
6. **Output**: Returns formatted answer to user

## Example Interaction

```
============================================================
Welcome to the Knowledge-Based QA Chatbot
Ask me questions about courses and staff
Type 'quit' or 'exit' to exit
============================================================

You: Tell me about Python course
Bot: The Python Programming course is taught by Dr. John Smith and runs for 8 weeks. Learn Python fundamentals including variables, loops, functions, and OOP

You: When is it scheduled?
Bot: The Python Programming course is scheduled for Monday and Wednesday, 2:00 PM - 3:30 PM.

You: quit
Bot: Goodbye! Have a great day!
```

## Topics Covered

### Core NLP Concepts
- Information Retrieval
- Intent Classification
- Keyword Extraction
- Named Entity Recognition (simplified)
- Response Generation

### Software Engineering
- Object-Oriented Programming
- Knowledge Base Design
- Rule-Based Systems
- CLI Development
- Error Handling

## Future Enhancements

- Add machine learning-based intent classification
- Implement similarity-based matching
- Support for follow-up questions
- Web interface with Flask
- Database integration
- Multi-language support
- Conversation history logging

## Requirements

See `requirements.txt` for dependencies.

Core dependencies:
- Python 3.8+

Optional dependencies:
- Flask for web interface
- NLTK for advanced NLP
- scikit-learn for ML-based classification

## Architecture

The system follows a modular architecture:

```
User Input
    ↓
Main Interface (main.py)
    ↓
QA Engine (qa_engine.py)
    ├→ Intent Recognition
    ├→ Keyword Extraction
    ├→ Entity Matching
    └→ Response Generation
    ↓
Knowledge Base (knowledge_base.py)
    ├→ Courses
    ├→ Staff
    └→ FAQ
    ↓
Response Output
```

## Learning Outcomes

After exploring this project, you will understand:
- How rule-based QA systems work
- Information retrieval fundamentals
- Pattern matching and keyword extraction
- Response template systems
- Chatbot design principles
- Python OOP practices

## Contributing

Contributions are welcome! Feel free to:
- Add more courses or staff data
- Improve intent recognition
- Add new response templates
- Implement new features
- Report bugs or suggest improvements

## License

MIT License - feel free to use this project for educational purposes.

## Author

Created as an educational project to demonstrate Knowledge-Based QA systems and Information Retrieval concepts.

## References

- Information Retrieval: https://en.wikipedia.org/wiki/Information_retrieval
- Rule-Based Systems: https://en.wikipedia.org/wiki/Rule-based_system
- Chatbot Development: https://en.wikipedia.org/wiki/Chatbot
- NLP Basics: https://en.wikipedia.org/wiki/Natural_language_processing
