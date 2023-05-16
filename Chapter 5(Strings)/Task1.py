"""Write code using find() and string slicing to extract the number at the end of the line below.
Convert the extracted value to a floating point number and print it out."""

text = "X-DSPAM-Confidence:0.8475"
start = text.find(":")
print(start)
extract = text[start+1:] #Starting from index of colon to the end of the string
print("The string is %s" %extract)
print("Converting string to float by adding 42.0")
value = float(extract) + 42.0
print(value)
