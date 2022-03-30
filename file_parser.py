
def parse_int(line):
  p = line.find(' ')
  if p == -1:
    return (None, line)
  count = line[:p]
  line = line[p+1:]
  #if line.startswith('/'):
  #  count2, line2 = parse_int(line[line[1:]])
  #  if count2 != None:
  #    count += '/' + count2
  #    line = line2
  return (count, line)


def parse_units(line):
  if line.startswith('oz '):
    return ('oz', line[3:])
  if line.startswith('tbsp '):
    return ('tbsp', line[5:])
  return (None, line)


def parse_line(line):
  line = line.strip('", ')
  if line.endswith('\\r'):
    line = line[:-2]
  if line == '<hr>':
    return (None, None, None)
  count, line = parse_int(line)
  units, line = parse_units(line)
  return (count, units, line)


def parse_lines(text):
  lines = text.splitlines()
  for line in lines:
    count, units, ingredient = parse_line(line)
    print 'c=%s u=%s i="%s"' % (count, units, ingredient)


with open("text.txt", "r") as f:
  file_text = f.read()

lines = parse_lines(file_text)
print(lines)

