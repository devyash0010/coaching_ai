# Coaching AI

## Overview
Coaching AI is a project designed to manage student data and generate embeddings for their academic performance using machine learning techniques. The application connects to a database, retrieves student information, and processes this data to create meaningful embeddings that can be used for various analytical purposes.

## Project Structure
```
coaching-ai
├── src
│   ├── db.py            # Database connection logic
│   ├── embedding.py     # Embedding model and data processing
│   └── main.py          # Entry point for the application
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment variables
├── .gitignore           # Files to ignore in Git
└── README.md            # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd coaching-ai
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Copy the `.env.example` file to `.env` and fill in the required database connection details.

5. **Run the application:**
   ```bash
   python src/main.py
   ```

## Usage
The application will connect to the specified database, fetch student data, generate embeddings for each student, and save these embeddings back to the database. You can modify the logic in `src/embedding.py` to customize how embeddings are generated or processed.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.