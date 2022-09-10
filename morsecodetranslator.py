print("Morse Code Translator V1")

print("")
print("")

# Put Anything You Want To Translate Below!
# p.s. Uppercase Alphabet Are Not Yet Supported, but lowercase and number are supported
input = "python is good. and easy to use"

def convert_to_morse(code):
    
    code = code.replace(" ", "  ")
    code = code.replace("", " ")
    code = code.replace(",", " ")
    code = code.replace(".", "  ")
    
    code = code.replace("a", ".-")
    code = code.replace("b", "-...")
    code = code.replace("c", "-.-.")
    code = code.replace("d", "-..")
    code = code.replace("e", ".")
    code = code.replace("f", "..-.")
    code = code.replace("g", "--.")
    code = code.replace("h", "....")
    code = code.replace("i", "..")
    code = code.replace("j", ".---")
    code = code.replace("k", "-.-")
    code = code.replace("l", ".-..")
    code = code.replace("m", "--")
    code = code.replace("n", "-.")
    code = code.replace("o", "---")
    code = code.replace("p", ".--.")
    code = code.replace("q", "--.-")
    code = code.replace("r", ".-.")
    code = code.replace("s", "...")
    code = code.replace("t", "-")
    code = code.replace("u", "..-")
    code = code.replace("v", "...-")
    code = code.replace("w", ".--")
    code = code.replace("x", "-..-")
    code = code.replace("y", "-.--")
    code = code.replace("z", "--..")
    
    code = code.replace("1", ".----")
    code = code.replace("2", "..---")
    code = code.replace("3", "...--")
    code = code.replace("4", "....-")
    code = code.replace("5", ".....")
    code = code.replace("6", "-....")
    code = code.replace("7", "--...")
    code = code.replace("8", "---..")
    code = code.replace("9", "----.")
    code = code.replace("0", "-----")
    
    return code
    
initial_code = input

morse_code = convert_to_morse(input)


print(f"Initial Code: {initial_code}")

print(f"Morse Code: {morse_code}")


print("")
print("")
print("Created by Emery 21 © 2022")
