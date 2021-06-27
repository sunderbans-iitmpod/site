import string
def legaldate(datetimestr):
  datetimestr = str(datetimestr)
  if not datetimestr:
    return ""
  illegals = string.punctuation
  for illegal in illegals:
    datetimestr = datetimestr.replace(illegal,'')
  if datetimestr[-5] != ' ':
    datetimestr = datetimestr[:-4]+' '+datetimestr[-4:]
  return datetimestr

def embedemail(hosts, emails):
  if not emails:
    return "nothing here"
  hosts = hosts.replace(', ',',').replace(' ,',',').split(',')
  emails = emails.replace(', ',',').replace(' ,',',').split(',')
  output = ""
  minmatch = min(len(hosts), len(emails))
  for i in range(minmatch):
    if emails[i] == 'none':
      output += hosts[i]
    else:
      output += f'<a href="mailto:{emails[i]}" target="_blank">{hosts[i]}</a>'
    output += ',&nbsp;'
  for i in range(minmatch, len(emails)):
    output += f'<a href="mailto:{emails[i]}" target="_blank">{emails[i]}</a>'
    output+= ',&nbsp;'
  return output.strip(',&nbsp;')