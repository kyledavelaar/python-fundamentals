import re

# split on white spaces (ignores tabs)
t = "foo \tsome oTher \tstuff other"
x = re.split(r"\s+", t)
print(x)

# can compile regex to make it reusable
r = re.compile(r"\s+")
x = re.split(r, t)
print(x)

# get list of all matching patterns for a particular regex and string
p = r.findall(t)
print(p)

# search only returns first one found
r = re.compile(r"other", flags=re.IGNORECASE)
p = r.search(t)
print(p)
w = t[p.start():p.end()]
print(w)


# match only matches if regex is at start of string
s = "holy cow"
x = re.match(r"ho", s)
print(x)
w = s[x.start():x.end()]
print(w) # ho
x = re.match(r"cow", s)
print(x) # None

# sub replaces words
s = """
charlie company12
bill    company23
"""
r = re.compile(r"company\d+")
x = r.sub('REDACTED', s)
print(x)


# make regex groups
s = """kyle.9907
bill.1343
"""
r = re.compile(r"([a-z]+)\.([0-9]{3})")
print(r.findall(s)) # [('kyle', '990'), ('bill', '134')]
m = r.match(s)
print(m.groups()) # remember match only returns what found at start of the string, so will only return ('kyle', '990')

# can use sub along with groups
t = r.sub(r"name: \1, id: \2", s)
print(t) # name: kyle, id: 9907 name: bill, id: 1343
# why is id not 134 above?

















