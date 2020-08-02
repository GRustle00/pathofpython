# \\ backslash(\)
# \' Single-quote(')
# \" Double-quote(")
# \a ASCII bell (BEL)
# \b ASCII backspace (BS)
# \f ASCII formfeed (FF)
# \n ASCII linefeed (LF)
# \N{name} Character named name in the Unicode database (Unicode only)
# \r Carriage Return (CR)
# \t Horizontal Tab (TAB)
# \uxxxx Character with 16-bit hex value xxxx
# \Uxxxxxxxx Character with 32-bit hex value xxxxxxxx
# \v ASCII vertical tab (VT)
# \000 Character with octal value 000
# \xhh Character with hex value hh

backslash = "Why don't you Back\\your slash up."
single_quote = 'Don\'t'
double_quote = "I \"get\" it, I understand"
bel = "\a"
bs = "This is a\btest (Again)"
ff = "Morning\fGood!"
lf = "Good\nNight"
unicode = "\N{WINKING FACE}"

print(backslash)
print(single_quote)
print(double_quote)
print(bel)
print(bs)
print(ff)
print(lf)
print(unicode)
print("test.one\r,test.two")
print("ok:\t*test.four")
print("test \v1\v 2\v 3")