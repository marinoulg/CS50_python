# In the United States, dates are typically formatted in month-day-year order
# (MM/DD/YYYY), otherwise known as middle-endian order, which is arguably bad
# design. Dates in that format can’t be easily sorted because the date’s year
# comes last instead of first. Try sorting, for instance, 2/2/1800, 3/3/1900,
# and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in
# that format are also ambiguous. Harvard was founded on September 8, 1636,
# but 9/8/1636 could also be interpreted as August 9, 1636!

# Fortunately, computers tend to use ISO 8601, an international standard that
# prescribes that dates should be formatted in year-month-day (YYYY-MM-DD)
# order, no matter the country, formatting years with four digits, months with
# two digits, and days with two digits, “padding” each with leading zeroes as
# needed.

# In a file called outdated.py, implement a program that prompts the user for
# a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or
# September 8, 1636, wherein the month in the latter might be any of the values
# in the list below:

# Then output that same date in YYYY-MM-DD format. If the user’s input is not a
# valid date in either format, prompt the user again. Assume that every month
# has no more than 31 days; no need to validate whether a month has 28, 29, 30,
# or 31 days.

months = {
            "January":"01",
            "February":"02",
            "March":"03",
            "April":"04",
            "May":"05",
            "June":"06",
            "July":"07",
            "August":"08",
            "September":"09",
            "October":"10",
            "November":"11",
            "December":"12"
        }

def day_is_correct(day):
    if 0 < int(day) < 32:
        return True

def month_is_correct(month):
    if 0 < int(month) < 13:
        return True

while True:
    prompt = input("Date: ").strip()

    try:
        if "/" in prompt:
            month, day, year = prompt.split("/")
            if month_is_correct(month) and day_is_correct(day):
                if int(month) < 10:
                    month = "0" + month

                if int(day) < 10:
                    day = "0" + day

                print(f"{year}-{month}-{day}")
                break
            else: continue

        elif "," in prompt:
            m_d, year = prompt.split(",")
            year = year.strip()
            month, day = m_d.split()

            day = day.strip()
            if day_is_correct(day):
                if int(day) < 10:
                    day = "0" + day
            else: continue

            if month.title().strip() in months:
                month = months[month]
                print(f"{year}-{month}-{day}")
                break

            else: continue
    except ValueError:
        pass
