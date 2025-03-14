#Build a program that stores a list of jokes and randomly selects one to display every time the user runs it. Add a fun twist with jokes about Python or programming! 🐍💡
import random

# List of programming jokes
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs! 🪲",
    "Why was the JavaScript developer sad? Because he didn't 'null' his ex properly! 😢",
    "Why did the Python programmer break up with the Java programmer? Too many curly braces! {}{}{}",
    "Why do Python programmers love nature? Because they prefer 'beautiful' over 'ugly'! 🌿",
    "Why did the coder quit his job? Because he didn't get arrays! 😆",
    "What is a programmer's favorite hangout place? The Foo Bar! 🍻",
    "Why was the function feeling self-conscious? Because it had too many 'arguments'! 😅",
    "How do you comfort a JavaScript bug? You 'console' it. 🖥️😂"
]

# Select and display a random joke
print("\n🤖 Welcome to the Python Joke Generator! 🐍\n")
print(random.choice(jokes))
print("\n😂 Hope that made you laugh! Run the program again for another joke!\n")