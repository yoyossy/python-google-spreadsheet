from unittest import TestCase

from nose.tools import assert_equals, assert_true

from google_spreadsheet.api import SpreadsheetAPI
from test_settings import (GOOGLE_SPREADSHEET_USER,
                           GOOGLE_SPREADSHEET_PASSWORD,
                           GOOGLE_SPREADSHEET_SOURCE,
                           GOOGLE_SPREADSHEET_KEY,
                           GOOGLE_WORKSHEET_KEY)


class TestSpreadsheetAPI(TestCase):
    """Test Google Spreadsheet API

    Test Class for Google Spreadsheet API wrapper.
    """
    def setUp(self):
        """Set Up.

        Initialize the Amazon API wrapper. The following values:

        * GOOGLE_SPREADSHEET_USER
        * GOOGLE_SPREADSHEET_PASSWORD
        * GOOGLE_SPREADSHEET_SOURCE
        * GOOGLE_SPREADSHEET_KEY
        * GOOGLE_WORKSHEET_KEY

        Are imported from a custom file named: 'test_settings.py'
        """
        self.spreadsheet = SpreadsheetAPI(GOOGLE_SPREADSHEET_USER,
            GOOGLE_SPREADSHEET_PASSWORD, GOOGLE_SPREADSHEET_SOURCE)

    def test_list_spreadsheets(self):
        """Test List Spreadsheets.

        Tests the list spreadsheets method by calling it and testing that at
        least one result was returned.
        """
        sheets = self.spreadsheet.list_spreadsheets()
        assert_true(len(sheets))

    def test_list_worksheets(self):
        """Test List Worksheets.

        Tests the list worksheets method by calling it and testing that at
        least one result was returned.
        """
        sheets = self.spreadsheet.list_worksheets(GOOGLE_SPREADSHEET_KEY)
        assert_true(len(sheets))

    def test_get_worksheet(self):
        """Test Get  Worksheet.

        Tests the get worksheet method by calling it and testing that a
        result was returned.
        """
        sheet = self.spreadsheet.get_worksheet(GOOGLE_SPREADSHEET_KEY,
            GOOGLE_WORKSHEET_KEY)
        assert_true(sheet)


class TestWorksheet(TestCase):
    """Test Worksheet Class

    Test Class for Worksheet.
    """
    def setUp(self):
        """Set Up.

        Initialize the Amazon API wrapper. The following values:

        * GOOGLE_SPREADSHEET_USER
        * GOOGLE_SPREADSHEET_PASSWORD
        * GOOGLE_SPREADSHEET_SOURCE
        * GOOGLE_SPREADSHEET_KEY
        * GOOGLE_WORKSHEET_KEY

        Are imported from a custom file named: 'test_settings.py'
        """
        self.spreadsheet = SpreadsheetAPI(GOOGLE_SPREADSHEET_USER,
            GOOGLE_SPREADSHEET_PASSWORD, GOOGLE_SPREADSHEET_SOURCE)
        self.sheet = self.spreadsheet.get_worksheet(GOOGLE_SPREADSHEET_KEY,
            GOOGLE_WORKSHEET_KEY)

    def test_get_rows(self):
        """Test Get Rows.
        """
        rows = self.sheet.get_rows()
        assert_true(len(rows))

    def test_update_row(self):
        """Test Update Rows.

        First gets all rows, than updates lest row.
        """
        rows = self.sheet.get_rows()
        row_index = len(rows) - 1
        new_row = rows[0]
        row = self.sheet.update_row(row_index, new_row)
        assert_equals(row, new_row)

    def test_insert_delete_row(self):
        """Test Insert and Delete Row.

        First gets all rows, than inserts a new row, finally deletes the new
        row.
        """
        rows = self.sheet.get_rows()
        num_rows = len(rows)
        new_row = rows[0]
        self.sheet.insert_row(new_row)
        insert_rows = self.sheet.get_rows()
        assert_equals(len(insert_rows), num_rows + 1)
        self.sheet.delete_row(num_rows)
        delete_rows = self.sheet.get_rows()
        assert_equals(len(delete_rows), num_rows)
        assert_equals(delete_rows[-1], rows[-1])
