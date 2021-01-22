"""


(uncompleted)


You're re-designing a blog and the blog's posts have the following format for
showing the date and time a post was made: Weekday Month Day, time e.g., Friday May 2, 7pm

You're running out of screen real estate, and on some pages you want to display
a shorter format, Weekday Month Day that omits the time.
Write a function, shortenToDate, that takes the Website date/time in its original
string format, and returns the shortened format.

Assume shortenToDate's input will always be a string, e.g. "Friday May 2, 7pm".
Assume shortenToDate's output will be the shortened string, e.g., "Friday May 2".


creator - radiocontrolled
"""




def shorten_to_date(long_date):
    for i in long_date:

        if i == ' ':

            weekday = long_date[:long_date.index(i)]

            month = long_date[long_date.index(i) + 1:]



    for j in month:

        if j.isspace():

            month = month[:month.index(j)]

            break

    for i in long_date:

        try:
            i = int(i)
            day = str(i)
            break
        except:
            pass


    return weekday, month, day







print(shorten_to_date("Monday February 2, 8pm"))
