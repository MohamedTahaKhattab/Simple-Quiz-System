# Simple Quiz System

A client-server quiz application built with Python that provides an interactive quiz experience through a GUI interface.

## Features

- **Client-Server Architecture**: Separate server and client components for scalability
- **Random Question Selection**: Server randomly selects 6 questions from a pool of 20 questions
- **Interactive GUI**: Clean, user-friendly interface built with tkinter
- **Real-time Scoring**: Live score tracking during the quiz
- **Immediate Feedback**: Shows correct/incorrect answers with explanations
- **Multiple Choice Questions**: 4 options per question covering various topics

## Question Topics

The quiz covers a wide range of general knowledge topics including:
- Geography (capitals, landmarks, natural features)
- Science (chemistry, astronomy, biology)
- World records and extremes
- Nature and wildlife

## Requirements

- Python 3.6 or higher
- tkinter (usually comes with Python)
- socket (built-in Python module)
- json (built-in Python module)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/Simple-Quiz-System.git
cd Simple-Quiz-System
```

2. No additional dependencies need to be installed as the project uses only Python standard library modules.

## Usage

### Starting the Server

First, start the quiz server:

```bash
python quiz_server.py
```

The server will start listening on `localhost:8080` and display:
```
Server started. Listening for incoming connections...
```

### Running the Client

In a separate terminal, start the quiz client:

```bash
python quiz_client.py
```

This will open the quiz GUI window where you can:
1. Read each question
2. Select from 4 multiple choice answers
3. Get immediate feedback on your selection
4. See the correct answer if you were wrong
5. Progress through all 6 questions
6. View your final score

## How It Works

### Server (`quiz_server.py`)
- Maintains a pool of 20 pre-defined questions
- Listens for client connections on port 8080
- Randomly selects 6 questions per client request
- Sends quiz data as JSON to connected clients
- Handles multiple client connections sequentially

### Client (`quiz_client.py`)
- Connects to the server to fetch quiz questions
- Displays questions in a tkinter GUI
- Handles user interactions (button clicks, navigation)
- Tracks score and provides feedback
- Shows final results when quiz is complete

## Architecture

```
┌─────────────────┐     TCP Socket     ┌─────────────────┐
│   Quiz Client   │ ◄────────────────► │   Quiz Server   │
│   (GUI App)     │    Port 8080       │ (Question Pool) │
└─────────────────┘                    └─────────────────┘
```

## Customization

### Adding New Questions

Edit the `quiz_data` list in `quiz_server.py`:

```python
{"question": "Your question here?", 
 "choices": ["Option A", "Option B", "Option C", "Option D"], 
 "answer": "Correct Option"}
```

### Changing Quiz Length

Modify the sample size in `quiz_server.py`:

```python
random_quiz_data = random.sample(self.quiz_data, 6)  # Change 6 to desired number
```

### Styling

The GUI styling can be customized in the `create_widgets()` method of `quiz_client.py`:

```python
self.style.configure("TLabel", font=("Helvetica", 20))
self.style.configure("TButton", font=("Helvetica", 16))
```

## Future Enhancements

- Support for multiple concurrent clients
- Database integration for question management
- User authentication and score persistence
- Timer functionality for timed quizzes
- Different difficulty levels
- Question categories/filtering
- Web-based interface

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Troubleshooting

**Connection Issues:**
- Ensure the server is running before starting the client
- Check that port 8080 is available
- Verify firewall settings if running on different machines

**GUI Issues:**
- Make sure tkinter is installed (`python -m tkinter`)
- Try running with `python3` instead of `python`

**General Issues:**
- Check Python version compatibility
- Ensure all files are in the same directory
- Verify file permissions

## Author

**Mohamed Taha Khattab** - mohamed.taha.khattab0@gmail.com
