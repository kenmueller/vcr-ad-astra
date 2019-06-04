import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open('VCR').sheet1

def total_loss(probability):
	return -2 * probability / 100

def break_even(probability):
	return -probability / 100

def two_times(probability):
	return 3 * probability / 100

def ten_times(probability):
	return 11 * probability / 100

def expected_value(company, multiplier):
	expected_value = (total_loss(company['total_loss']) + break_even(company['break_even']) + two_times(company['two_x']) + ten_times(company['ten_x'])) * company['impact'] * company['equity'] * multiplier / 100
	print(company['name'] + ': ' + str(expected_value))
	return expected_value

def expected_values(companies, multiplier):
	print('MULTIPLIER: ' + str(multiplier) + '%')
	for i in range(0, len(companies)):
		sheet.update_cell(i + 2, 8, expected_value(companies[i], multiplier))

expected_values(sheet.get_all_records(), int(sheet.cell(2, 10).value))