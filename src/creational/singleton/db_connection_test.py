import unittest
from unittest.mock import MagicMock, patch
from src.creational.singleton.db_connection import DatabaseConnection


class TestDatabaseConnection(unittest.TestCase):

    def setUp(self):
        self.db_connection = DatabaseConnection()
        self.db_connection._connection = MagicMock()

    def test_execute_query_with_connection(self):
        query = "SELECT * FROM users"
        self.db_connection._connection.execute.return_value = MagicMock()

        self.db_connection.execute_query(query)

        self.db_connection._connection.execute.assert_called_once_with(query)
        self.db_connection._connection.commit.assert_called_once()

    @patch('src.creational.singleton.db_connection.sqlite3')
    def test_execute_query_without_connection(self, mock_sqlite3):
        mock_sqlite3.connect.side_effect = Exception("No connection")
        query = "SELECT * FROM users"

        with self.assertRaises(Exception) as context:
            self.db_connection.execute_query(query)

        self.assertEqual('No connection', str(context.exception))


if __name__ == '__main__':
    unittest.main()
