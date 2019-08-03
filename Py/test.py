
print u'\u7cbe\u88c5'

print u'7.5\u5143/m\xb2/\u5929'

d = {
    'ac_type': '',
    'address': '',
    'building_id': 1881,
    'building_name': u'\u5143\u8fb0\u946b\u5927\u53a6',
    'chewei_nums': '',
    'city_id': 12,
    'city_name': '\xe5\x8c\x97\xe4\xba\xac',
    'crawled_at': '2016-09-18',
    'created_at': 1474191352,
    'display_rank': 0,
    'district_id': 985,
    'district_name': u'\u671d\u9633',
    'elevator_type': '',
    'has_image': 1,
    'house_nums': 0,
    'jianzhu_area': '',
    'jinggao': '',
    'latlng': '',
    'layout_nums': 0,
    'network': '',
    'owner_type': '',
    'price_avg': u'7.5\u5143/m\xb2/\u5929',
    'property_level': '',
    'room_rate': '',
    'ruzhu_company': '',
    'street_id': u'998',
    'street_name': u'\u5b89\u8d1e/\u9a6c\u7538',
    'thumb_image': u'http://image.diandianzu.com/Uploads/Photo/w_57624d95ccef4.jpg',
    'total_ceng': '',
    'updated_at': 1474191352,
    'url': 'http://bj.diandianzu.com/listing/detail-i1881.html',
    'website_id': 3,
    'wuye_compony': '',
    'wuye_fee': ''
}


def test():
    yield 1
    x = 123


test()

print '#' * 20


x = {'area': [u'340'],
 'building_id': 2242,
 'building_name': [u'\u4e2d\u56fd\u65b0\u65f6\u4ee3\u5927\u53a6'],
 'city_id': 12,
 'city_name': u'\u5317\u4eac',
 'crawled_at': '2016-09-18',
 'created_at': 1474197754,
 'gongwei': '',
 'guwen': '',
 'guwen_phone': '',
 'house_id': [u'14518'],
 'house_status': '',
 'min_zuqi': '',
 'owner_type': '',
 'rent_price': [u'6.5'],
 'rent_price_unit': [u'\u5143/m\xb2/\u5929'],
 'thumb_status': 0,
 'thumb_url': '',
 'updated_at': 1474197754,
 'url': 'http://bj.diandianzu.com/listing/detail-i2242.html',
 'zhuangxiu': ''}
sql = "INSERT INTO ws_house_info_3 (guwen,crawled_at,area,city_id,created_at,gongwei,house_status,min_zuqi,rent_price_unit,updated_at,rent_price,thumb_status,url,city_name,guwen_phone,owner_type,building_id,zhuangxiu,house_id,thumb_url,building_name) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"  % ['', '2016-09-18', u'398', 12, 1474198789, '', '', '', u'\u5143/m\xb2/\u5929', 1474198789, u'12.5', 0, 'http://bj.diandianzu.com/listing/detail-i484.html', u'\u5317\u4eac', '', '', 484, '', 6729, '', u'\u5bcc\u5c14\u5927\u53a6']

print sql
