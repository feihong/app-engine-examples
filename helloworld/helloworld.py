import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write("""
        <h1>Hello World</h1>
        <p>Groobus, Smelt!</p>
        """)


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
