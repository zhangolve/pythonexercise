# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function, division

from ljmall.feature.search_keyword.search_keyword import get_all_search_keyword_statics, get_all_search_keyword_product_hits_and_search_hits
from veil.profile.web import *
from ljmall.feature.search_keyword import *
from veil.utility.encoding import *

operator_route = route_for('operator')

import csv
import tempfile

HOT_KEYWORD_EXPIRED_MONTH = 4

def get_all_search_keyword_statics():
    return db().get('''
    SELECT SUM(search_hits) AS all_search_hits, COUNT(single) AS all_value_count
    FROM  (SELECT search_hits, 'single' AS single FROM hot_keyword ) hot_keyword 
    GROUP BY single;
    ''')


@command
def get_all_search_keyword_product_hits_and_search_hits(count=to_integer):
    return db().list('''
        SELECT hk.*, COUNT(ph.*) AS product_hits 
          FROM (SELECT * FROM hot_keyword
            ORDER BY search_hits DESC
            LIMIT %(count)s) hk
            LEFT JOIN (
                SELECT * FROM product_search
             ) ph ON keywords@>ARRAY[hk.value] OR ph.tsv @@ PLAINTO_TSQUERY('zhparser_config', hk.value) OR ph.name ILIKE hk.value
             GROUP BY hk.value, hk.search_hits
             ORDER BY search_hits DESC
        ''', count=count)


@operator_route('GET', '/search/keyword-log-exporter')
def keywords_exporter_widget():
    statics = get_all_search_keyword_statics()
    return get_template('keyword-log-exporter.html').render(all_search_hits=statics.all_search_hits,
                                                            all_value_count=statics.all_value_count,
                                                            hot_keyword_expired_month=HOT_KEYWORD_EXPIRED_MONTH)


@operator_route('GET', '/search/export-keyword-log')
def export_sc_purchase_refunds_csv():
    count = get_http_argument('count', to_type=int)
    all_keywords = get_all_search_keyword_product_hits_and_search_hits(count)
    with tempfile.TemporaryFile(mode='wb+') as out_file:
        header = ['关键词', '搜索频次', '商品命中数']
        csv_writer = csv.writer(out_file)
        csv_writer.writerow([to_str(h) for h in header])
        for keyword in all_keywords:
            line = [keyword.value, keyword.search_hits, keyword.product_hits]
            csv_writer.writerow([to_str(field) if field is not None else b'' for field in line])
        out_file.seek(0)
        response = get_current_http_response()
        response.set_header('Content-Type', 'text/csv; charset=gb18030')
        filename = '搜索关键词记录.csv'
        response.set_header('Content-Disposition', 'attachment; filename={}'.format(quote_plus(filename)))
        response.write(out_file.read().decode('UTF-8').encode('gb18030'))
