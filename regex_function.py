def multiple_replace(mydict, text): 
  #replace text by dictionary key: regex. value: value to repalce.
  regex = re.compile("(%s)" % "|".join(map(re.escape,mydict.keys())))
  return regex.sub(lambda mo: ' '+mydict[mo.string[mo.start():mo.end()]]+' ', text) 
  
  
