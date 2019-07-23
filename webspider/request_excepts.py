# -*- coding:utf-8 -*-
# https://stackoverflow.com/questions/24518944/try-except-when-using-python-requests-module

import requests

test_urls = ['http://httpbin.org/user-agent',
             'http://httpbin.org/status/404',
             'http://httpbin.org/status/500',
             'httpx://invalid/url']


def return_json(url):
    try:
        response = requests.get(url, timeout=1)

        # Consider any status other than 2xx an error
        if not response.status_code // 100 == 2:
            return "Error: Unexpected response {}".format(response)

        json_obj = response.json()
        return json_obj
    except requests.exceptions.ConnectTimeout as e:
        print 'requests.exceptions.ConnectTimeout'
        return "requests.exceptions.ConnectTimeout: {}".format(e)
    except requests.exceptions.Timeout:
        print 'requests.exceptions.Timeout'
    except requests.exceptions.ConnectionError:
        print 'requests.exceptions.ConnectionError'
    except requests.exceptions.RequestException as e:
        # A serious problem happened, like an SSLError or InvalidURL
        print "requests.exceptions.RequestException: {}".format(e)


for url in test_urls:
    print "Fetching URL '{}'".format(url)
    print return_json(url)
    print
