from dataflows import Flow, load, dump_to_path

BASE_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'
CONFIRMED_GLOBAL = 'time_series_covid19_confirmed_global.csv'
DEATH_GLOBAL = 'time_series_covid19_deaths_global.csv'
RECOVERED_GLOBAL = 'time_series_covid19_recovered_global.csv'
# RECOVERED = 'time_series_19-covid-Recovered.csv'
# DEATHS = 'time_series_19-covid-Deaths.csv'
# CONFIRMED = 'time_series_19-covid-Confirmed.csv'
CONFIRMED_US = 'time_series_covid19_confirmed_US.csv'
DEATH_US = 'time_series_covid19_deaths_US.csv'

# Flow(
#       load(f'{BASE_URL}{CONFIRMED}'),
#       load(f'{BASE_URL}{RECOVERED}'),
#       load(f'{BASE_URL}{DEATHS}'),
#       dump_to_path('csse_covid_19_data')
# ).results()[0]


Flow(
      load(f'{BASE_URL}{CONFIRMED_US}'),
      dump_to_path('csse_covid_19_data/confirmed_us/')
).results()[0]

Flow(
      load(f'{BASE_URL}{DEATH_US}'),
      dump_to_path('csse_covid_19_data/deaths_us/')
).results()[0]

# Flow(
#       load(f'{BASE_URL}{CONFIRMED_GLOBAL}'),
#       dump_to_path('csse_covid_19_data/confirmed_global/')
# ).results()[0]

# Flow(
#       load(f'{BASE_URL}{DEATH_GLOBAL}'),
#       dump_to_path('csse_covid_19_data/deaths_global/')
# ).results()[0]

# Flow(
#       load(f'{BASE_URL}{RECOVERED_GLOBAL}'),
#       dump_to_path('csse_covid_19_data/recovered_global/')
# ).results()[0]