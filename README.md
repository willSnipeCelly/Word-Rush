{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Word Rush\
\
A simple Wordle clone implemented in Python using the Tkinter library. This is an attempt to balance wordle with a scoring mechanism. The game tracks your performance over ten rounds and provides a score based on accuracy and speed.\
\
## Features\
\
- Interactive GUI using Tkinter\
- Keyboard input for guessing words\
- Highlighted feedback for correct, present, and absent letters\
- Scoring system based on number of guesses and time taken\
- Scoreboard to track top scores\
\
## Setup\
\
### Prerequisites\
\
- Python 3.x\
- Tkinter (usually included with Python installations)\
\
### Installation\
\
1. **Clone the repository:**\
\
    ```bash\
    git clone https://github.com/username/WordleGame.git\
    cd WordleGame\
    ```\
\
2. **Ensure you have the necessary files:**\
\
    - `words.txt` - List of possible words to be guessed.\
    - `guessable_words.txt` - List of valid guessable words.\
    - The main script file (e.g., `wordle_game.py`).\
\
3. **Run the game:**\
\
    ```bash\
    python wordle_game.py\
    ```\
\
## How to Play\
\
1. Run the game using the instructions above.\
2. Enter your guesses in the text field and press "Enter" or click "Guess".\
3. The game provides feedback:\
    - Green for correct letters in the correct position.\
    - Yellow for correct letters in the wrong position.\
    - White for incorrect letters.\
4. The game continues until you guess the word correctly or exhaust your six attempts.\
5. After completing ten rounds, the game displays your total score and performance.\
6. Your score and details will be saved to `scores.txt`.\
\
## Scoring\
\
- 100 points for each correct word.\
- Points deducted for guesses:\
    - Guess 4: -25 points\
    - Guess 5: -50 points\
    - Guess 6: -100 points\
- Time bonus: 120 points minus 2 points per second taken (max 60 seconds, otherwise 0 points).\
\
## File Structure\
\
- `wordle_game.py` - Main game script.\
- `words.txt` - List of possible answer words.\
- `guessable_words.txt` - List of guessable words.\
- `scores.txt` - File to store the scoreboard.\
\
## Contributing\
\
Contributions are welcome! Please fork the repository and submit a pull request.\
\
1. Fork the repository.\
2. Create a new branch (`git checkout -b feature-branch`).\
3. Commit your changes (`git commit -am 'Add new feature'`).\
4. Push to the branch (`git push origin feature-branch`).\
5. Create a new pull request.\
\
## License\
\
This project is licensed under the MIT License. See the `LICENSE` file for details.\
\
## Acknowledgements\
\
- Inspired by the popular word game Wordle.\
- Developed using Python and Tkinter.\
\
## Contact\
\
For any questions or feedback, please contact [WKEII](mailto:WKEII@gmail.com).\
}
