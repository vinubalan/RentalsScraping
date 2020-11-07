SCRAPE_TIMEOUT = 10  # seconds
SQL_SELECT_LIMIT_ROW_COUNT = 1000
IS_CHROME_HEADLESS_ENABLED = False

THRIFTY_COMPANY_ID = 1
THRIFTY_COMPANY_LOCATIONS_PAGE_URL = "https://www.thrifty.co.nz/locations/"

BUDGET_COMPANY_ID = 2
BUDGET_COMPANY_LOCATIONS_PAGE_URL = "https://www.budget.co.nz/en/locations/new-zealand"
BUDGET_BOOKING_PAGE_URL = "https://www.budget.co.nz/en/home"

GORENTALS_COMPANY_ID = 3
GORENTALS_COMPANY_LOCATIONS_PAGE_URL = (
    "https://www.gorentals.co.nz/rental-car-locations/"
)
GORENTALS_BOOKING_PAGE_URL = "https://www.gorentals.co.nz/"

RENTALS_SCRAPING_DB_CONNECTION_CONIFG = {
    "host": "stratford.cafcotgpxc6f.ap-southeast-2.rds.amazonaws.com",
    "database": "rentals_scraping",
    "user": "admin",
    "password": "NRtf1zLWXJWdMj7mazKn",
    "time_zone": "+13:00",
}

MONTHS = {
    "JANUARY": 1,
    "FEBRUARY": 2,
    "MARCH": 3,
    "APRIL": 4,
    "MAY": 5,
    "JUNE": 6,
    "JULY": 7,
    "AUGUST": 8,
    "SEPTEMBER": 9,
    "OCTOBER": 10,
    "NOVEMBER": 11,
    "DECEMBER": 12,
}

# The dictionary's key is office name, value is input value for pick-up and drop-off locations.
BUDGET_LOCATION_INPUT_VALUE_DICT = {
    "Auckland Airport": "Auckland",
    "Auckland Penrose": "Auckland",
    "Auckland Downtown": "Auckland",
    "Auckland North Shore": "Auckland",
    "Blenheim Airport": "Blenheim",
    "Christchurch Airport": "Christchurch",
    "Christchurch Downtown": "Christchurch",
    "Christchurch Sheffield Crescent": "Christchurch",
    "Dunedin Airport": "Dunedin",
    "Dunedin Downtown": "Dunedin",
    "Gisborne Airport": "Gisborne",
    "Greymouth Railway Station": "Greymouth",
    "Hamilton Airport": "Hamilton",
    "Hamilton Downtown": "Hamilton",
    "Hokitika Airport": "Hokitika",
    "Invercargill Airport": "Invercargill",
    "Kerikeri Airport": "Kerikeri",
    "Napier Airport": "Napier",
    "Nelson Airport": "Nelson",
    "New Plymouth Airport": "New Plymouth",
    "New Plymouth Downtown": "New Plymouth",
    "Palmerston North Airport": "Palmerston North",
    "Picton Ferry Terminal": "Picton",
    "Queenstown Airport": "Queenstown",
    "Queenstown Downtown": "Queenstown",
    "Rotorua Airport": "Rotorua",
    "Rotorua Downtown": "Rotorua",
    "Taupo Airport": "Taupo",
    "Taupo Downtown": "Taupo",
    "Tauranga Airport": "Tauranga",
    "Wellington Airport": "Wellington",
    "Wellington Ferry Terminal": "Wellington",
    "Wellington Downtown": "Wellington",
    "Petone Lower Hutt": "Petone Lower Hutt",
    "Whangarei Airport": "Whangarei",
}
