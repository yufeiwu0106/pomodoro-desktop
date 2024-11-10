from db import Database
from start_button import StartButton
import unittest
from unittest.mock import patch
from unittest.mock import Mock


class TestDatabase(unittest.TestCase):
    def test_class_variable(self):
        self.assertEqual(Database.DB_NAME, "pomodoro.db")

    @patch("db.sqlite3") # create a patch for sqlite3
    def test_init(self, mock_sqlite3):
        mock_conn = Mock() 
        mock_sqlite3.connect.return_value = mock_conn

        db = Database()   
        db.init()

        mock_sqlite3.connect.assert_called_once()
        mock_conn.execute.assert_called_once()
        mock_conn.close.assert_called_once()


class TestStartButton(unittest.TestCase):

    def test_set_paused(self):
        start_button = StartButton(1, 1, 1, Mock())

        self.assertFalse(start_button.paused)
        self.assertEqual(start_button.text, "Start")

        start_button.set_paused()

        self.assertTrue(start_button.paused)
        self.assertEqual(start_button.text, "Pause")



if __name__ == "__main__":
    unittest.main()
