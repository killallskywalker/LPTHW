#how to declare a variable and use a variable 
author = "Killalltheskywalker"
familiar_language = "HTML,JAVASCIPT,PHP,PYTHON"
familiar_framework = "Codeigniter,Bootstrap"
number_phone = 0145002011
my_gba_point = 0.1

#print standard variable
print "My name is",author,", My familiar language are",familiar_language,"and my familiar framwework are",familiar_framework ,"."

#check variable type 
number_phone_type = type(number_phone) #use type() to check the type of variable 
#print number_phone_type

#print with print formatter
formatter = "%r %r %r %r" #raw output ,known as representation 
print formatter % ("Testing","Testing 2","Testing 3","Testing 4")

#testing
formattter_newline = "%r"
print formattter_newline % ("My name is killalskywalker\nAnd im 30 years old") #new line will not work because we using formatter %r which is it will print the output as type

#testing formatter using %s
formattter_newline = "%s"
print formattter_newline % ("My name is killalskywalker\nAnd im 30 years old")

#escape sequence
'''
\\ Backslash (\)
\' Single-quote (') \" Double-quote (")
\a ASCII bell (BEL)
\b ASCII backspace (BS)
\f ASCII formfeed (FF)
\n ASCII linefeed (LF)
\N{name} Character named name in the Unicode database (Unicode only) \r ASCII carriage return (CR)
\t ASCII horizontal tab (TAB)
\uxxxx Character with 16-bit hex value xxxx (Unicode only) \Uxxxxxxxx Character with 32-bit hex value xxxxxxxx (Unicode only) \v ASCII vertical tab (VT)
\ooo Character with octal value oo
\'xhh Character with hex value hh
'''

