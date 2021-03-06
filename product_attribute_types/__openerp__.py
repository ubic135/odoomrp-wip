
# -*- encoding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    "name": "Product attribute types",
    "version": "1.0",
    "depends": [
        "product",
    ],
    "author": "OdooMRP team",
    "contributors": [
        "Mikel Arregi <mikelarregi@avanzosc.es>",
        "Oihane Crucelaegui <oihanecrucelaegi@avanzosc.es>",
    ],
    "category": "Product Management",
    "website": "http://www.odoomrp.com",
    "description": """
This module provide :
    New features in product attributes:
        * Mandatory fields
        * Default attribute value
        * Range based type of attribute
        * ...
    """,
    'data': [
        "views/product_view.xml",
    ],
    'installable': True,
}
