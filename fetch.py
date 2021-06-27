import os
import json
import gspread
from dataparse import legaldate,embedemail
from datetime import datetime
from pytz import timezone
from models import Event, Logo

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
  now = datetime.now(timezone('Asia/Kolkata'))
  for data in dataset:
    if data['link'][:4] != 'http':
      data['link'] = 'https://' + data['link']
    if data['yt'][:4] != 'http':
      data['yt'] = 'https://' + data['yt']
    if data['datetime']:
      data['datetime'] = datetime.strptime(legaldate(data['datetime']), '%d%m%Y %H%M').replace(tzinfo=timezone('Asia/Kolkata'))
    else:
      continue
    if data['datetimeend']:
      data['datetimeend'] = datetime.strptime(legaldate(data['datetimeend']), '%d%m%Y %H%M').replace(tzinfo=timezone('Asia/Kolkata'))
    data['desc'].replace("<a", '<a target = "_blank" ')
    data['contact'] = embedemail(data['hosts'], data['email'])
    if data['datetimeend'] and data['datetimeend'] > now or data['datetime'] > now:
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
