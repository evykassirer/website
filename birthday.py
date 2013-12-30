import webapp2
from dateValidation import valid_month, valid_day, valid_year
import cgi

def escape_html(s):
    return cgi.escape(s, quote = True)

birthdayform = """
<form method="post"> 
        What is your birthday?
	<br>
	<label> Month <input type="text" name="month" value="%(month)s"> </label>
	<label> Day <input type="text" name="day" value="%(day)s"> </label> 
	<label> Year <input type="text" name="year" value="%(year)s"> </label>
	<div style="color: red">%(error)s</div>	
	<br>
	<br>
        <input type="submit">
</form>
"""    

class BirthdayHandler(webapp2.RequestHandler):
    def write_birthday_form(self, error="", month="", day="", year=""):
        self.response.out.write(birthdayform % {"error": error, "month": escape_html(month), "day": escape_html(day), "year": escape_html(year)})
    def get(self):
        self.write_birthday_form()
    def post(self):
	user_month = self.request.get('month')
	user_day = self.request.get('day')
	user_year = self.request.get('year')
	month = valid_month(user_month)
	day = valid_day(user_day)
        year = valid_year(user_year)
	if not(month and day and year):
            self.write_birthday_form("That doesn't look valid to me, friend.", user_month, user_day, user_year)	
        else: 
            self.redirect("/thanks")       

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks! That's a totally valid day!")

