#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import urllib
import webapp2
import jinja2
from model.converter import *

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


class RobotsHandler(webapp2.RequestHandler):
    def get(self):
        self.response.content_type = "text/plain"
        self.response.write("""
        User-agent: *\n
        Disallow:\n
        Allow: /\n
        Sitemap: http://input.zone/sitemap.xml\n
        """)


class SitemapHandler(webapp2.RequestHandler):
    def get(self):
        self.response.content_type = "text/xml"
        content = """
            <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
        """
        for c in Converter.query().fetch():
            content += """<url>
            <loc>http://input.zone/{0}.html</loc>
            <changefreq>monthly</changefreq>
            </url>""".format(c.key.id())
        content += "</urlset>"
        self.response.write(content)


class ConverterHandler(webapp2.RequestHandler):
    def get(self, converter_id):
        context = Converter.get_by_id(converter_id)
        if context is not None:
            template = JINJA_ENVIRONMENT.get_template('build/web/template.html')
            self.response.write(template.render(c=context))


app = webapp2.WSGIApplication(routes=[
    ('/robots.txt', RobotsHandler),
    ('/sitemap.xml', SitemapHandler),
    webapp2.Route(r'/<converter_id:\w+>.html', handler=ConverterHandler, name='converter')
], debug=True)
