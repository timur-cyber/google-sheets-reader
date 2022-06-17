from typing import List

from googleapiclient.discovery import build
from google.oauth2 import service_account

from exchange import make_exchange
from models import Base, Records, get_session
from sheets import SERVICE_ACCOUNT_FILE, SCOPES, SAMPLE_SPREADSHEET_ID


class MainClass:
    def get_sheets_data(self):
        """
        Метод для получения данных с таблицы Google Sheets при помощи Google API
        :return: List[List]
        """
        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='Лист1').execute()
        return result.get('values')

    def get_columns_w_ruble(self):
        """
        Добавление к таблице из Google Sheets колонки со значением в рублях
        :return: List[List]
        """
        columns = self.get_sheets_data()
        columns[0].insert(3, 'стоимость,₽')
        for column in columns[1:]:
            if len(column) < 4:
                columns.pop(columns.index(column))
                continue
            dollar = int(column[2])
            ruble = make_exchange(dollar)
            column.insert(3, ruble)
        return columns

    def update_table(self, columns: List[List]):
        """
        Обновление таблицы по данным из параметра
        :param columns: List[List]
        :return: None
        """
        Base.metadata.drop_all()
        Base.metadata.create_all()
        session = get_session()
        for column in columns[1:]:
            record = Records(
                num=column[0],
                order_num=column[1],
                price=column[2],
                price_rub=column[3],
                date=column[4]
            )
            session.add(record)
        session.commit()
