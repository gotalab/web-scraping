from locale import currency
from booking.booking import Booking


with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='JPY')
    bot.select_place_to_go('Sapporo')
    bot.select_dates(check_in_date='2022-03-01', check_out_date='2022-03-03')
    bot.select_adults(10)
    # bot.select_kids(5)
    bot.select_rooms(3)
    bot.click_search()