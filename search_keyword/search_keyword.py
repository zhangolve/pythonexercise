# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function, division
from veil.profile.web import *


operator_route = route_for('operator')


@operator_route('GET', '/search')
def search_section():
    return get_template('search-section.html').render()



