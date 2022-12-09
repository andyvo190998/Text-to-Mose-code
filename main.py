MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
def text2code():
    user_input = input("Type your text? \n")
    characters_list = list(user_input)
    converted_list = []
    for i in characters_list:
        # print(i)
        if i == " ":
            converted_list.append("/ ")
        for morse in MORSE_CODE_DICT:
            if i.upper() == morse:
                converted_list.append(MORSE_CODE_DICT[morse])
                converted_list.append(" ")
            else:
                pass
    final_translation = "".join(converted_list)
    print(f"Your translation is '{final_translation}'")


def code2text():
    converted_list = []
    user_input = input("Type your code? \n")
    code_list = user_input.split()
    for morse in code_list:
        if morse == "/":
            converted_list.append(" ")
        for i in MORSE_CODE_DICT:
            if morse == MORSE_CODE_DICT[i]:
                converted_list.append(i)
    final_translation = "".join(converted_list)

    print(f"Your final translation is '{final_translation}'")


print("Well come to encryted application!")
user_choice = input("you want to convert from text or code? \n")
if user_choice == "text":
    text2code()
elif user_choice == "code":
    code2text()
else:
    pass
    # print(characters_list)