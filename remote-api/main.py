import jinja2
import webapp2
from google.appengine.ext import ndb


class Log(ndb.Model):
    text = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)


index_template = jinja2.Template("""\
<head>
    <title>Remote API Example</title>
</head>

<h1>Log</h1>

<ul>
    {% for log in logs %}
    <li>{{ log.date }} - {{ log.text }}</li>
    {% endfor %}
</ul>
""")


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(index_template.render(
            logs=Log.query().order(Log.date)))

    def post(self):
        text = self.request.get('text')
        if text:
            log = Log(text=text)
            log.put()

        self.redirect('/')


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
