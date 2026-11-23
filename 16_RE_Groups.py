import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% - the worst day since it launched in 1998. \
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."

print()
result = re.search(r".+\s(.+ex).+(\d\d\s.+).", string)
print("type(result) ->", type(result))
print("result.groups() ->", result.groups())
print("result.group() ->", result.group())
print("result.group(0) ->", result.group(0))    # Same as result.group()
print("result.group(1) ->", result.group(1))
print("result.group(2) ->", result.group(2))
print("result.group(1, 2) ->", result.group(1, 2))
