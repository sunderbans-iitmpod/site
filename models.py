class Obj:
  def __init__(self,attrs):
    for key in attrs:
      setattr(self,key,attrs[key])

class Event(Obj):
  pass

class Logo(Obj):
  pass 

class Photo(Obj):
  pass