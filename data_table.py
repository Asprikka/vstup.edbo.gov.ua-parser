from faculty import Faculty
from bs4 import BeautifulSoup
import re

from data_row import DataRow
from app_status import AppStatus


class DataTable:

    @staticmethod
    def extract_data_rows(html):
        data_rows = []

        soup = BeautifulSoup(html, 'html.parser')

        full_name_list = DataTable.get_data_row_property(soup, 'fio')
        app_status_list = DataTable.get_data_row_property(soup, 'status')
        priority_list = DataTable.get_data_row_property(soup, 'priority')
        exam_score_list = DataTable.get_data_row_property(soup, 'kv')

        rows_count = len(full_name_list)
        for i in range(rows_count):
            full_name = full_name_list[i].decode_contents().replace('\n', '').replace('\t', '')
            app_status = AppStatus.get_app_status(app_status_list[i].decode_contents())
            priority = re.sub(r"\s+", "", priority_list[i].decode_contents())
            exam_score = float(re.sub(r"\s+", "", exam_score_list[i].decode_contents()).replace(',', '.'))

            data_rows.append(DataRow(full_name, app_status, priority, exam_score))

        return DataTable.sort_by_exam_score(data_rows)


    @staticmethod
    def sort_by_exam_score(data_rows):
        return sorted(data_rows, key=lambda r: r.exam_score, reverse=True)


    @staticmethod
    def get_data_row_property(soup, name):
        return soup.select(f'div#offer-requests-body>div>div.offer-request-{name}>div')


    def __init__(self, faculty, html):
        faculty.set_post_data(html)
        self.faculty: Faculty = faculty
        self.data_rows = DataTable.extract_data_rows(html)


    def show_info(self):
        fac_info_text = f'\n\n\n{self.faculty.name} - {self.faculty.get_link()}\n\n' \
                        f'Обсяг бюджетних місць -- {self.faculty.free_education_places_count}\n' \
                        f'Подано заяв ------------ {self.faculty.applicants_count}\n' \
                        f'Допущено до конкурсу: -- {self.faculty.admitted_applicants_count}\n' \
                        f'Заяв на бюджет: -------- {self.faculty.free_education_applicants}\n'

        print(fac_info_text)

        print_counter = 0
        for i in range(len(self.data_rows)):
            row: DataRow = self.data_rows[i]

            if not DataTable.apply_show_info_filters(row):
                continue

            print_counter += 1
            print(f'{print_counter}.\t{row.exam_score:.1f} ({row.priority}) - {row.full_name}')


    @staticmethod
    def apply_show_info_filters(row):

        app_status_sel = row.app_status == AppStatus.ADMITTED or \
                         row.app_status == AppStatus.REGISTERED or \
                         row.app_status == AppStatus.SUBMITTED
        priority_sel = row.priority in ['1', '2']
        min_exam_score = 194

        return app_status_sel and priority_sel and row.exam_score >= min_exam_score
