from bs4 import BeautifulSoup

import re


class Faculty:

    def __init__(self, name, offer_code):
        self.name = name  # довільне найменування
        self.offer_code = offer_code

        self.free_education_places_count = 0
        self.applicants_count = 0
        self.admitted_applicants_count = 0
        self.free_education_applicants = 0


    def get_link(self):
        return f'https://vstup.edbo.gov.ua/offer/{self.offer_code}/'


    def set_post_data(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        fepc_sel = '#offer > div.offer > div.offer-info > div.offer-info-left > dl.row.offer-max-order > dd'
        fepc_tag = soup.select_one(fepc_sel).decode_contents()
        self.free_education_places_count = int(re.sub(r"\s+", "", fepc_tag))

        ac_sel = '#offer > div.offer > div.offer-requests-stats.offer-requests-stats-c > div' \
                 ' > div.col-md-4.col-sm-12.stats-field.stats-field-t > div.value'
        ac_tag = soup.select_one(ac_sel).decode_contents()
        self.applicants_count = int(re.sub(r"\s+", "", ac_tag))

        aac_sel = '#offer > div.offer > div.offer-requests-stats.offer-requests-stats-c > div' \
                  ' > div.col-md-4.col-sm-12.stats-field.stats-field-a > div.value'
        aac_tag = soup.select_one(aac_sel).decode_contents()
        self.admitted_applicants_count = int(re.sub(r"\s+", "", aac_tag))

        fea_sel = '#offer > div.offer > div.offer-requests-stats.offer-requests-stats-c > div' \
                  ' > div.col-md-4.col-sm-12.stats-field.stats-field-b > div.value'
        fea_tag = soup.select_one(fea_sel).decode_contents()
        self.free_education_applicants = int(re.sub(r"\s+", "", fea_tag))
