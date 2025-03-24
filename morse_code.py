# Import necessary libraries
import time
import neopixel
import board

# Define the Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/'
}

# Function to clean user input and convert to uppercase
def clean_input(text):
    text = text.upper()  # Convert to uppercase for dictionary lookup
    return ''.join(char for char in text if char in MORSE_CODE_DICT)

# Function to convert text to Morse code
def text_to_morse(text):
    return ' '.join(MORSE_CODE_DICT[char] for char in text)

# Function to get a valid unit time from user input
def get_unit_time():
    while True:
        try:
            unit_time = float(input("Enter unit time for Morse code (0-1 sec): "))
            if 0 <= unit_time <= 1:
                return unit_time
            else:
                print("Please enter a number between 0 and 1.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

# Function to get a valid LED color from user input
def get_led_color():
    print("Enter RGB values (0-255) for LED color.")
    while True:
        try:
            r = int(input("Red: "))
            g = int(input("Green: "))
            b = int(input("Blue: "))
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return (r, g, b)
            else:
                print("Values must be between 0 and 255.")
        except ValueError:
            print("Invalid input. Please enter integer values between 0 and 255.")

# Function to display Morse code using LEDs
def display_morse(morse_code, unit_time, color):
    pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.3)
    
    for symbol in morse_code:
        if symbol == '.':  # Short blink
            pixels.fill(color)
            time.sleep(unit_time)
        elif symbol == '-':  # Long blink
            pixels.fill(color)
            time.sleep(unit_time * 3)
        elif symbol == ' ':  # Space between letters
            time.sleep(unit_time * 3)
        elif symbol == '/':  # Space between words
            time.sleep(unit_time * 7)
        
        pixels.fill((0, 0, 0))  # Turn off LEDs
        time.sleep(unit_time)  # Short pause between signals

# Main program execution
if __name__ == "__main__":
    user_text = input("Enter text to convert to Morse code: ")
    cleaned_text = clean_input(user_text)
    morse_code = text_to_morse(cleaned_text)
    print("Morse Code:", morse_code)
    
    unit_time = get_unit_time()  # Get valid unit time from user
    color = get_led_color()  # Get valid LED color from user
    
    display_morse(morse_code, unit_time, color)
