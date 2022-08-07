class DataRow:

    def __init__(self, full_name, app_status, priority, exam_score):
        self.full_name = full_name
        self.app_status = app_status  # :AppStatus consts
        self.priority = priority
        self.exam_score = exam_score
