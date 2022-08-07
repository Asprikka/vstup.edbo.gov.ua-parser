class AppStatus:

    ADMITTED = 'допущено'
    REGISTERED = 'зареєстровано'
    SUBMITTED = 'заява надійшла з сайту'
    CANCELLED = 'скасовано (втрата пріор.)'
    UNKNOWN = None

    @staticmethod
    def get_app_status(str):
        status_list = [AppStatus.ADMITTED,
                       AppStatus.REGISTERED,
                       AppStatus.SUBMITTED,
                       AppStatus.CANCELLED]

        for status in status_list:
            if status in str:
                return status

        return AppStatus.UNKNOWN
