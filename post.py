import os
import json
import gspread

from models import Event

gc = sh = worksheet = dataset = None

def init(i):
  global gc, sh, worksheet, dataset
  
  gc = gspread.service_account_from_dict(json.loads(os.environ['all-secrets']))
  link = 'https://docs.google.com/spreadsheets/d/1Dt7G2Lbe6Ao-8JCQ8xhndtoiNM_vGB9kNHs7SImD7mk/'
  sh = gc.open_by_url(link)
  worksheet = sh.get_worksheet(i)
  dataset = worksheet.get_all_records()

def add_event(e):
  init(0)
  ins_loc = len(dataset) + 2
  col = 1
  for var in vars(e):
    worksheet.update_cell(ins_loc, col, vars(e)[var])
    col = col + 1