class Event:
  def __init__(self,attrs):
    for key in attrs:
      setattr(self,key,attrs[key])

class Logo:
  def __init__(self,attrs):
    for key in attrs:
      setattr(self,key,attrs[key])