import streamlit as st
import random

# List of words for the hangman game
WORDS = ["python", "streamlit", "hangman", "developer", "openai", "machine", "learning"]

def initialize_game():
    word = random.choice(WORDS)
    guessed_letters = []
    attempts_left = 6
    return word, guessed_letters, attempts_left

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Initialize session state variables
if "word" not in st.session_state:
    st.session_state.word, st.session_state.guessed_letters, st.session_state.attempts_left = initialize_game()
if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.title("🎯 Hangman Game - Streamlit Version")

st.subheader(f"Attempts Left: {st.session_state.attempts_left}")

displayed_word = display_word(st.session_state.word, st.session_state.guessed_letters)
st.header(displayed_word)

# Only allow input if game is not over
if not st.session_state.game_over:
    guess = st.text_input("Enter a letter:", max_chars=1)

    if st.button("Guess"):
        if guess:
            guess = guess.lower()
            if guess in st.session_state.guessed_letters:
                st.warning(f"You already guessed '{guess}'!")
            elif guess in st.session_state.word:
                st.success(f"Good job! '{guess}' is in the word!")
                st.session_state.guessed_letters.append(guess)
            else:
                st.error(f"Oops! '{guess}' is not in the word.")
                st.session_state.guessed_letters.append(guess)
                st.session_state.attempts_left -= 1

        # Check if game is won
        if all(letter in st.session_state.guessed_letters for letter in st.session_state.word):
            st.balloons()
            st.success(f"Congratulations! You guessed the word '{st.session_state.word}'!")
            st.session_state.game_over = True

        # Check if game is lost
        if st.session_state.attempts_left == 0:
            st.error(f"Game Over! The word was '{st.session_state.word}'.")
            st.session_state.game_over = True

# Restart the game
if st.button("Restart Game"):
    st.session_state.word, st.session_state.guessed_letters, st.session_state.attempts_left = initialize_game()
    st.session_state.game_over = False
    st.experimental_rerun()
