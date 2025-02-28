# Parašykite funkciją, kuri įvestą datą (formatas dd.mm.yyyy) keistų į yyyy mm dd.
import re


def change_date_format(given_date):
    try:
        regex_pattern = re.compile(r"(0[1-9]|1[0-9]|2[0-9]|3[0-1])\.(0[1-9]|1[0-2])\.(\d{4})")
        result = regex_pattern.search(given_date)
        changed_date = f'New date format {result.group(3)} {result.group(2)} {result.group(1)} (yyyy mm dd)'
        print(changed_date)
    except AttributeError:
        print(f"Invalid date input: {given_date}")


good_dates_text = "28.12.2020"
bad_dates_text = "32.13.2020"
print(f'Given date format {good_dates_text} (dd.mm.yyyy)')
change_date_format(good_dates_text)
change_date_format(bad_dates_text)

#  date = regex_pattern.sub('\{g<3>} \g<2> \g<1>', given_date)
