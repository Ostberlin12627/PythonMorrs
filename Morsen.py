#!/usr/bin/env python3
from gpiozero import LED, Button
from time import sleep

# Definiere die LED-Pinnummer
ledPin = 17
led = LED(ledPin)

# Morsecode-Tabelle
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

def translate_to_morse(text):
    morse = ''
    for char in text:
        if char.upper() in morse_code:
            morse += morse_code[char.upper()] + ' '
        else:
            morse += ' '
    return morse

def blink_morse_code(morse):
    for symbol in morse:
        if symbol == '.':
            led.on()
            sleep(0.2)
            led.off()
            sleep(0.2)
        elif symbol == '-':
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.2)
        elif symbol == ' ':
            sleep(0.5)

if __name__ == '__main__':
    input_text = input("Welchen Text soll ich dir Morsen? ")
    morse_code = translate_to_morse(input_text)
    print("Morsecode: ", morse_code)
    blink_morse_code(morse_code)