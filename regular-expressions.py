import re

t = "foo \tsome oTher \tstuff other"


print('split ---------------------------------')
# split on white spaces (ignores tabs)
x = re.split(r"\s+", t)
print(x)

# can compile regex to make it reusable
r = re.compile(r"\s+")
x = re.split(r, t)
print(x)

print('findall ---------------------------------')
# get list of all matching patterns for a particular regex and string
r2 = re.compile(r'\bwin?[a-z]+\b', re.IGNORECASE)
sentence = 'the winners played to WIN'
p = r2.findall(sentence) # ['winners', 'WIN']
print(p)

print('search ---------------------------------')
# search only returns first one found
r = re.compile(r"other", flags=re.IGNORECASE)
p = r.search(t)
print(p) # <re.Match object; span=(10, 15), match='oTher'>
print(p.group()) # oTher
w = t[p.start():p.end()]
print(w) # oTher


print('match ---------------------------------')
# match only matches if regex is at start of string
s = "holy cow"
x = re.match(r"ho", s)
print(x)
w = s[x.start():x.end()]
print(w) # ho
x = re.match(r"cow", s)
print(x) # None

print('sub ---------------------------------')
# sub replaces words
s = """
charlie company12
bill    company23
"""
r = re.compile(r"company\d+")
x = r.sub('REDACTED', s)
print(x)


print('regex groups ---------------------------------')
# make regex groups
s = """kyle.9907
bill.1343
"""
r = re.compile(r"([a-z]+)\.([0-9]{4})")
print(r.findall(s)) # [('kyle', '9907'), ('bill', '1343')]
m = r.match(s)
print(m.groups()) # remember match only matches at start of string so will only return ('kyle', '9907')

# can use sub along with groups
t = r.sub(r"name: \1, id: \2", s)
print(t) # name: kyle, id: 9907 name: bill, id: 1343

















