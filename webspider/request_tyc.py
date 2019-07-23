# -*-coding:utf-8-*-

import requests

# r = requests.get('http://www.tianyancha.com/v2/company/22822.json', headers = {'X-Requested-With': 'XMLHttpRequest'});
r = requests.get('http://yii.han.app/site/test1', headers = {'X-Requested-With': 'XMLHttpRequest'});
print r.content
