from locale import currency
from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='JPY')
        bot.select_place_to_go('Sapporo')
        bot.select_dates(check_in_date='2022-03-01', check_out_date='2022-03-03')
        bot.select_adults(2)
        bot.select_rooms(1)
        bot.click_search()
        # bot.apply_filtrations()
        bot.report_result()

except Exception as e:
    if 'in PATH' in str(e):
        print("Please add to PATH your selenium Drivers \n"
              "Windows: set PATH=%PATH%;C:path-to-your-chromedriver \n"
              "Linux: PATH=$PATH: /path/to/your/chromedriver \n"
              )
    else:
        raise