import os
import json
import gspread
from dataparse import embedemail
from datetime import datetime
from dateutil import parser
from pytz import timezone
from models import *

gc = sh = worksheet = dataset = None

def init(i):
  global gc, sh, worksheet, dataset
  gc = gspread.service_account_from_dict(json.loads(os.environ['all-secrets']))
  link = 'https://docs.google.com/spreadsheets/d/1Dt7G2Lbe6Ao-8JCQ8xhndtoiNM_vGB9kNHs7SImD7mk/'
  sh = gc.open_by_url(link)
  worksheet = sh.get_worksheet(i)
  dataset = worksheet.get_all_records()

def events():
  init(0)
  eventlist = []

  tzinfo = timezone('Asia/Kolkata')
  now = datetime.now(tzinfo)

  for data in dataset:
    if data['link'] and data['link'][:4] != 'http':
      data['link'] = 'https://' + data['link']
    if data['date']:
      data['date'] = parser.parse(data['date'])
      data['date'] = data['date'].strftime('%d %B %Y ')
    if data['time']:
      data['time'] = parser.parse(data['time'])
      data['time'] = data['time'].strftime('⋅ %H:%M')
    if data['dateend']:
      data['dateend'] = parser.parse(data['dateend'])
      data['dateend'] = data['dateend'].strftime('%d %B %Y ')
    if data['timeend']:
      data['timeend'] = parser.parse(data['timeend'])
      data['timeend'] = data['timeend'].strftime('⋅ %H:%M')
    data['desc'] = data['desc'].replace("<a", '<a target = "_blank" ')
    data['contact'] = embedemail(data['hosts'], data['email'])
    #if data['datetime'] > now or data['datetimeend'] and data['datetimeend'] > now:
    eventlist.append(Event(data))
  #eventlist.sort(key = lambda x : x.date)
  return eventlist


def logos():
  init(1)
  logolist = []
  for data in dataset:
    if data['ilink'][:4] != 'http':
      data['ilink'] = 'https://' + data['ilink']    
    logolist.append(Logo(data))
  logolist.sort(key = lambda x : x.id)
  return logolist

def photos():
  init(2)
  photolist = []
  for data in dataset:
    if data['ilink'][:4] != 'http':
      data['ilink'] = 'https://' + data['ilink']    
    photolist.append(Photo(data))
  photolist.sort(key = lambda x : x.id)
  return photolist

def captures():
  init(5)
  photolist = []
  for data in dataset:
    if data['ilink'][:4] != 'http':
      data['ilink'] = 'https://' + data['ilink']    
    photolist.append(Obj(data))
  photolist.sort(key = lambda x : x.id)
  return photolist