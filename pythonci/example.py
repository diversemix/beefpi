# Example taken from:
#  http://stackoverflow.com/questions/14536992/how-do-i-receive-github-webhooks-in-python#14550657

import web

urls = ('/.*', 'hooks')

class hooks:
    def POST(self):
        data = web.data()
        print
        print 'DATA RECEIVED:'
        print data
        print
        return 'OK'

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
