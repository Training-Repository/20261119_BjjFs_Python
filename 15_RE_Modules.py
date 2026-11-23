# path = r"c:\temp\notes\ramakant"
# print(path)


import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
    including the FTSE, fell by 11.48% - the worst day since it launched in 1998. \
    The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
    of STOXX 600 shares since its all-time peak on 19 February."

s = r"\d{2}"
print(f"{type(s) = }")

t = re.compile(s)
print(f"[{t}], {type(t) = }")

print("-"*40)
result = re.findall(t, string)
print(f"{result = }, {type(result) = }")


print("-"*40)
result = re.findall(s, string)
print(f"{result = }, {type(result) = }")

print("-"*40)
result = re.search(s, string)
print(f"{result = }, {type(result) = }")
print(f"{result.span() = }")
print(f"{result.start() = }")
print(f"{result.end() = }")
print(f"Matched string ->", f"{string[result.start():result.end()] = }")

print("-"*40)
s = r"\w{3}"
result = re.match(s, string)
print(f"{result = }, {type(result) = }")

print("-"*40)
print(len(string))

result = re.fullmatch(r'.{297}', string)
print(f"{result = }, {type(result) = }")

# Str Split method
print("-"*40)
result =  string.split('STOXX')
print(f"{result = }, {type(result) = }")


# re Split method
print("-"*40)
result =  re.split(r'\s', string)
print(f"{result = }, {type(result) = }")


# sub - Substitute
print("-"*40)
result =  re.sub(r'[A-Z]{2,}', "INDEX", string)
print(f"{result = }, {type(result) = }")


# subn - Substitute + count
print("-"*40)
result =  re.subn(r'[A-Z]{2,}', "INDEX", string)
print(f"{result = }, {type(result) = }")
