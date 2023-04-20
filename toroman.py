#convert letter to roman number 
def convert_to_number():
    sentence = input("Insert sentence that you want to convert every letter to roman number: ")
    user_list_input = list(sentence.upper().strip())
    alphabet = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    to_number = []

    for letter in user_list_input:
        for i in range(len(alphabet)):
            if letter == alphabet[i]:
                letter = letter.replace(alphabet[i], str(i+1))
                break
        to_number.append(letter)

    roman = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI"]
    user_list_input = []

    for number in to_number:
        for i in range(len(roman)):
            if number == str(i+1):
                number = roman[i]
                break
        user_list_input.append(number)

    user_input = " ".join(user_list_input)
    print(f"\n\t{user_input}")

