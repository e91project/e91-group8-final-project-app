"""
This test suite checks that the page is online, and that the correct data is returned.

Environment variables must be set to provide the host, port and path.  The defaults are ...

TEST_HOST localhost
TEST_PORT 80
TEST_PATH index.html
"""

import os
import unittest
from html.parser import HTMLParser
from http.client import HTTPConnection

# Get host/port/path from environment variables if provided
TEST_HOST_DEFAULT = 'localhost'
TEST_PORT_DEFAULT = 80
TEST_PATH_DEFAULT = '/'
test_host = TEST_HOST_DEFAULT if 'TEST_HOST' not in os.environ else os.environ['TEST_HOST']
test_port = TEST_PORT_DEFAULT if 'TEST_PORT' not in os.environ else int(os.environ['TEST_PORT'])
test_path = TEST_PATH_DEFAULT if 'TEST_PATH' not in os.environ else os.environ['TEST_PATH']

H1_TITLE_TEXT = 'E91 Group 8 Final Project Sample Website'

TEAM_MEMBERS = [
    "David Stampfli",
    "Jonathan Nichols",
    "Kakhaber Urigashvili",
    "Navdeep Singh",
    "Paul Hasenfus",
    "Robert Cavezza"
]

class TestWebSite(unittest.TestCase):

    def test_200OK(self):
        conn = HTTPConnection(test_host, test_port)
        conn.request('GET', test_path)
        resp = conn.getresponse()
        self.assertEqual(200, resp.status)
        conn.close()

    def test_resp_type(self):
        conn = HTTPConnection(test_host, test_port)
        conn.request('GET', test_path)
        resp = conn.getresponse()
        self.assertEqual(resp.headers['content-type'], 'text/html')
        conn.close()

    def test_is_html_page(self):
        conn = HTTPConnection(test_host, test_port)
        conn.request('GET', test_path)
        resp = conn.getresponse()
        body = resp.read().decode()
        self.assertTrue(body.startswith('<!DOCTYPE html>'))
        conn.close()

    def test_header_text(self):
        conn = HTTPConnection(test_host, test_port)
        conn.request('GET', test_path)
        resp = conn.getresponse()
        body = resp.read().decode()
        parser = TestHTMLTagParser('h1')
        parser.feed(body)
        self.assertTrue(len(parser.text) == 1)
        self.assertTrue(parser.text[0] == H1_TITLE_TEXT)
        conn.close()

    def test_team_members(self):
        conn = HTTPConnection(test_host, test_port)
        conn.request('GET', test_path)
        resp = conn.getresponse()
        body = resp.read().decode()
        parser = TestHTMLTagParser('li')
        parser.feed(body)
        self.assertTrue(len(parser.text) == len(TEAM_MEMBERS))
        for person in parser.text:
            self.assertTrue(person in parser.text)
        conn.close()

    def test_has_footer(self):
        conn = HTTPConnection(test_host, test_port)
        conn.request('GET', test_path)
        resp = conn.getresponse()
        body = resp.read().decode()
        parser = TestHTMLTagParser('footer')
        parser.feed(body)
        self.assertEqual(len(parser.text), 1)
        conn.close()

    def test_version(self):
        conn = HTTPConnection(test_host, test_port)
        conn.request('GET', test_path)
        resp = conn.getresponse()
        body = resp.read().decode()
        parser = TestHTMLTagParser('p')
        parser.feed(body)
        version_found = False
        for text in parser.text:
            if text.startswith('Version'):
                version_found = True
        self.assertTrue(version_found)
        conn.close()


"""Parses an HTML string, and find the text for the specified HTML tag."""
class TestHTMLTagParser(HTMLParser):

    def __init__(self, tag):
        super().__init__()
        self.tag = tag
        self.just_found = False
        self.text = []

    def handle_starttag(self, tag, attrs):
        if tag == self.tag and not self.just_found:
            self.just_found = True

    def handle_data(self, data):
        if self.just_found:
            self.text.append(data)
            self.just_found = False

if __name__ == '__main__':
    unittest.main()
