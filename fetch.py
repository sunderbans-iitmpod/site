import os
import json
import gspread
from dataparse import embedemail
from datetime import datetime
from dateutil import parser
from pytz import timezone
from models import Event, Logo, Photo

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
    if data['link'][:4] != 'http':
      data['link'] = 'https://' + data['link']
    if data['yt'][:4] != 'http':
      data['yt'] = 'https://' + data['yt']
    if data['datetime']:
      # data['datetime'] = datetime.strptime(legaldate(data['datetime']), '%d%m%Y %H%M').replace(tzinfo=tzinfo)
      data['datetime'] = parser.parse(data['datetime'] + '+5:30')
    else:
      continue
    if data['datetimeend']:
      # data['datetimeend'] = datetime.strptime(legaldate(data['datetimeend']), '%d%m%Y %H%M').replace(tzinfo=tzinfo)
      data['datetimeend'] = parser.parse(data['datetimeend'] + '+5:30' )
    data['desc'].replace("<a", '<a target = "_blank" ')
    data['contact'] = embedemail(data['hosts'], data['email'])
    if data['datetime'] > now or data['datetimeend'] and data['datetimeend'] > now:
      eventlist.append(Event(data))
  eventlist.sort(key = lambda x : x.datetime)
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



def photocon():
  init(2)
  photolist = []
  for data in dataset:
    if data['ilink'][:4] != 'http':
      data['ilink'] = 'https://' + data['ilink']    
    photolist.append(Photo(data))
  photolist.sort(key = lambda x : x.id)
  return photolist


def digart():
  init(3)
  photolist = []
  for data in dataset:
    if data['ilink'][:4] != 'http':
      data['ilink'] = 'https://' + data['ilink']    
    photolist.append(Photo(data))
  photolist.sort(key = lambda x : x.id)
  return photolist
