text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(':')
slice = text[pos+1:]
strip = slice.strip()
istrip = float(strip)
print(istrip)
