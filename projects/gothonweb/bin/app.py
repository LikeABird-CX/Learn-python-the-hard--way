import web

urls = (
  '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('F:/Dropbox/Python Exercise/Python Exercise/projects/gothonweb/templates/')

class Index(object):
    def GET(self):
        greeting = "Hello World"
        return render.index(greeting = greeting)
 
if __name__ == "__main__":
    app.run()