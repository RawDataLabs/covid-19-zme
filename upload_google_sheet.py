import gspread, os
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']


# f = open('MagicUniverses-0bb6ec1a1ec4.json', 'w')
# f.write(  os.environ.get('GTOKEN') )
# f.close()

credentials = ServiceAccountCredentials.from_json_keyfile_name('../MagicUniverses-0bb6ec1a1ec4.json', scope)
# credentials = ServiceAccountCredentials.from_json_keyfile_name('MagicUniverses-0bb6ec1a1ec4.json', scope)

gc = gspread.authorize(credentials)


def createWorkSheet(state):
  wks = gc.create('ZMECVD19_Timeseries_'+state)
  print ("created spreadsheet: "+ wks.id)
  shareWorkSheet(wks.id)
  return wks.id
  # ID returned
  # 1nODJ-NFS_P3zwZGz6RuyIWLJoHKPKLS3S-hCbGVKwpk   

def shareWorkSheet(id):
    # Make the spreadsheet publicly readable
  gc.insert_permission(
    id,
    None,
    perm_type='anyone',
    role='reader'
  )

  gc.insert_permission(
    id,
    'spinualin@gmail.com',
    perm_type='user',
    role='writer'
  )

  gc.insert_permission(
    id,
    'tibipuiu@gmail.com',
    perm_type='user',
    role='writer'
  )

  # sh = gc.open_by_key(id)
  # sh.share('spinualin@gmail.com', perm_type='user', role='owner', notify='True')
  # sh.share('tibipuiu@gmail.com', perm_type='user', role='owner', notify='True')


  # wks = gc.open("US_States_Working_ZME_CVD19")
def addWorksheetsForState(state, data):
  wksid = createWorkSheet(state)
  # wks = gc.open_by_key("")
  # worksheet = wks.add_worksheet(title=state, rows="100", cols="10")
  # worksheet = wks.worksheet(state)
  print("added worksheet for state :"+state)
  # print(worksheet.id)
  # 1nODJ-NFS_P3zwZGz6RuyIWLJoHKPKLS3S-hCbGVKwpk
  gc.import_csv(wksid, data)
  print(" <<<<<<<<<<<<<" + wksid + " >>>>>>>>>>>>>>>" )
  print("https://docs.google.com/spreadsheets/d/" + wksid + "/edit" )

def addWorksheetsForStateById(id, state, data):
  wks = gc.open_by_key(id)
  print("added worksheet for state :"+state)
  # print(worksheet.id)
  # 1nODJ-NFS_P3zwZGz6RuyIWLJoHKPKLS3S-hCbGVKwpk
  gc.import_csv(wks.id, data)
  print(" <<<<<<<<<<<<<" + wks.id + " >>>>>>>>>>>>>>>" )
  print("https://docs.google.com/spreadsheets/d/" + wks.id + "/edit" )

def addFileToGspread(filePath, state):
  content = open( filePath, 'r').read()
  addWorksheetsForState(state, content)


# worksheets 
# {
#   filePath
#   SPREADSHEET_ID
#   query
# }

def listAllAthenaQueryResults():
  path = 'athena-report-gen/query-results'
  files = []
  # r=root, d=directories, f = files
  for r, d, f in os.walk(path):
      for file in f:
          if '.csv' in file:
              # files.append(os.path.join(r, file))
              print(os.path.join(r, file))
              print(file)
              addFileToGspread(os.path.join(r, file), file )

listAllAthenaQueryResults()



# for i in ["1bwvUhboM7aK6ziw31sA9huC0DUSWhpJwCL7_9eryEok","1fQloqhn7WdXI32Fdjj7V-nC7DtFP8Qw8Dh-LrZX7gDc", "1IWsKUv9lKs3J2xx3AzquDPizqeNjycIrJoMuDo_PReg", "1ntdG2N3_ks7R6avxxxQxyVVivuuS5VhZzAmiJuyzGUc", "1zRTPbuEy8xzahIKKfeagxujcXrozP3lODVWtROSoQl4" ]:
#   gc.del_spreadsheet(i)

# created spreadsheet: 1bwvUhboM7aK6ziw31sA9huC0DUSWhpJwCL7_9eryEok
# athena-report-gen/query-results/1_New Jersey.csv
# 1_New Jersey.csv
# created spreadsheet: 1fQloqhn7WdXI32Fdjj7V-nC7DtFP8Qw8Dh-LrZX7gDc
# athena-report-gen/query-results/0_New York.csv
# 0_New York.csv
# created spreadsheet: 1IWsKUv9lKs3J2xx3AzquDPizqeNjycIrJoMuDo_PReg
# athena-report-gen/query-results/2_California.csv
# 2_California.csv
# created spreadsheet: 1ntdG2N3_ks7R6avxxxQxyVVivuuS5VhZzAmiJuyzGUc
# athena-report-gen/query-results/4_Massachusetts.csv
# 4_Massachusetts.csv
# created spreadsheet: 1zRTPbuEy8xzahIKKfeagxujcXrozP3lODVWtROSoQl4



# content = open( 'csse_covid_19_data/time_series_19-covid-Confirmed.csv', 'r').read()
# wks = gc.open("1Kui1mg90hNUPg9awKeQcTS5XUQwm00Bn-A9Q6Ti5s_s")
# gc.import_csv("1Kui1mg90hNUPg9awKeQcTS5XUQwm00Bn-A9Q6Ti5s_s", content)
# gc.import_csv("test", content)

# os.environ.get('SPREADSHEET_ID')