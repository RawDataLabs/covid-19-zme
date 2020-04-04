from dataflows import Flow, load, dump_to_path, printer
from datetime import timedelta, date

BASE_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'
CONFIRMED_US = 'time_series_covid19_confirmed_US.csv'
DEATH_US = 'time_series_covid19_deaths_US.csv'


# processing dataset with -1 day lag
today_s = date.today()  - timedelta(days=1)
today = today_s.strftime('%-m/%-d/20') 

yesterday_s =  date.today() - timedelta(days=2)
yesterday = yesterday_s.strftime('%-m/%-d/20') 

# def print_days(package):
#     elems = package.pkg.descriptor['resources'][0]['schema']['fields'][-2:]
#     extra_value.yesterday = elems[0]['name']
#     extra_value.today = elems[1]['name']
    
def add_dates_column_to_schema(package):
    # Add a new field to the first resource
    elems = package.pkg.descriptor['resources'][0]['schema']['fields'][-2:]
    # yesterday = elems[0]['name']
    # today = elems[1]['name']

    package.pkg.descriptor['resources'][0]['schema']['fields'].append(dict(
        name='yesterday',
        type='number'
    ))
    package.pkg.descriptor['resources'][0]['schema']['fields'].append(dict(
        name='today',
        type='number'
    ))
    # Must yield the modified datapackage
    yield package.pkg
    # And its resources
    yield from package

def add_dates_column(row):
    row['yesterday'] = row[yesterday]
    row['today'] = row[today]


Flow(
    load(f'{BASE_URL}{CONFIRMED_US}'),
    # add_dates_column_to_schema,
    # add_dates_column,
    dump_to_path('csse_covid_19_data/confirmed_us/'),
).process()[1]


Flow(
    load(f'{BASE_URL}{DEATH_US}'),
    # add_dates_column_to_schema,
    # add_dates_column,
    dump_to_path('csse_covid_19_data/deaths_us/'),
).process()[1]

