# Example taken from:
#  http://stackoverflow.com/questions/14536992/how-do-i-receive-github-webhooks-in-python#14550657

import web
import logging

urls = ('/.*', 'hooks')

class hooks:
    def POST(self):
        data = web.data()
        logging.info("DATA RECEIVED: %s", str(data))
        return "OK, {}".format(str(data))

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
