# © 2018-Today Aktiv Software (http://www.aktivsoftware.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': "Status Bar Clock",
    'summary': """
        Clock will be displayed""",
    'description': """
        Clock will be displayed in status bar.
    """,
    'author': "Aktiv Software",
    'website': "http://www.aktivsoftware.com",
    'category': 'Extra Tools',
    'license': 'AGPL-3',
    'version': '11.0.1.0.0',
    'depends': ['base_setup'],
    'data': [
        'views/res_company_view.xml',
        'views/status_bar_clock_view.xml',
        'static/src/xml/web_view.xml'
    ],
    'images': [
        'static/description/banner.jpg',
    ],
}
