import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    print(">>> main", repr(language_file), encoding, errors)
    line = language_file.readline() #read lines language_file

    if line: #if there's an written line do:
        print(">>> Printing line", repr(line), encoding, errors)
        print_line(line, encoding, errors) #use print_line function then:
        print(">>> calling main")
        return main(language_file, encoding, errors) #return back to main function
        
    print("End of file")


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages1.txt", encoding="utf-8")

main(languages, input_encoding, error)