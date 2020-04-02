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

# Read CSV file contents
content = open( 'csse_covid_19_data/time_series_19-covid-Confirmed.csv', 'r').read()
# content = open( os.environ.get('SOURCE_FILE'), 'r').read()

gc.import_csv('1Kui1mg90hNUPg9awKeQcTS5XUQwm00Bn-A9Q6Ti5s_s', content)
# gc.import_csv(os.environ.get('SPREADSHEET_ID'), content)



# wks = gc.open("Where is the money Lebowski?").sheet1



