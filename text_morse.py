
# # SOLUTION 1

# PLAIN_TEXT = input("Enter text: ")
# def char_to_morse(char):
#     morse_code_dict = {
#             'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
#             'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
#             'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#             'Y': '-.--', 'Z': '--..',
#             '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
#             '6': '-....', '7': '--...', '8': '---..', '9': '----.',
#             ' ': '/'
#         }
#     return morse_code_dict.get(char.upper())

# def text_to_morse(text):
#     print(text)
#     print("".join( [ char_to_morse(t) for t in text ] ))

# text_to_morse(PLAIN_TEXT)

# SOLUTION 2

class TextMorse:
    MORSE_CODE_DICT = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..',
            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.',
            ' ': '/'
        }

    def __init__(self):
        self.plain_text = input('Enter Text: ')
    
    def text_to_morse(self):
        return ("".join([ self.MORSE_CODE_DICT.get(t.upper()) for t in self.plain_text ]))      
 