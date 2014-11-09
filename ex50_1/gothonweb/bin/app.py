import web

urls = (
  '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('F:/Dropbox/Python Exercise/Python Exercise/ex50_1/gothonweb/templates/')

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = "%s, %s" % (form.greet, form.name)
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()