"""
creator - radiocontrolled


(completed)


You're re-designing a blog and the blog's posts have the following format for
showing the date and time a post was made: Weekday Month Day, time e.g., Friday May 2, 7pm

You're running out of screen real estate, and on some pages you want to display
a shorter format, Weekday Month Day that omits the time.
Write a function, shortenToDate, that takes the Website date/time in its original
string format, and returns the shortened format.

Assume shortenToDate's input will always be a string, e.g. "Friday May 2, 7pm".
Assume shortenToDate's output will be the shortened string, e.g., "Friday May 2".
"""


### I slightly misread the sample tests and it ended up making it a lot harder
### for me but I still managed to get the solution even if there is a suffix on 
### the day, such as "2nd" 

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

            try:
                
                q = int(long_date[long_date.index(day):long_date.index(day) + 2])
                day = str(q)

            except:
                pass

            break

        except:
            pass

    end_result = weekday + ' ' + month + ' ' + day

    return end_result

print(shorten_to_date("Tuesday January 29, 10pm"))

