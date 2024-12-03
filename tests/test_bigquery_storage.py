import unittest
from unittest.mock import Mock, patch
from datetime import datetime
from datastorage import BigQueryStorage, TableSchema
from dto.parkingdata import ParkingData, ParkingLot

class TestBigQueryStorage(unittest.TestCase):
    def setUp(self):
        """Set up test cases."""
        self.mock_client = Mock()
        with patch('google.cloud.bigquery.Client') as mock_client:
            self.storage = BigQueryStorage()
            self.storage.client = mock_client()

    def test_create_table(self):
        """Test table creation."""
        # Arrange
        mock_table_schema = Mock(spec=TableSchema)
        mock_table_schema.table_name = "test_table"
        mock_table_schema.get_create_table_schema.return_value = [
            {"name": "id", "type": "STRING"}
        ]

        # Act
        self.storage.create_table(mock_table_schema)

        # Assert
        self.storage.client.create_table.assert_called_once()

    def test_insert_data(self):
        """Test data insertion."""
        # Arrange
        test_data = [
            ParkingLot(
                official_id="123",
                name="Test Parking",
                description="Test Description",
                county="Test County",
                district="Test District",
                address="Test Address",
                total_parking_spaces=100,
                total_motorcycle_spaces=50,
                total_charging_stations=2
            )
        ]
        self.storage.client.insert_rows_json.return_value = []  # No errors

        # Act
        self.storage.insert_data("test_table", test_data)

        # Assert
        self.storage.client.insert_rows_json.assert_called_once()

    def test_insert_data_with_error(self):
        """Test data insertion with error."""
        # Arrange
        test_data = [
            ParkingLot(
                official_id="123",
                name="Test Parking",
                description="Test Description",
                county="Test County",
                district="Test District",
                address="Test Address",
                total_parking_spaces=100,
                total_motorcycle_spaces=50,
                total_charging_stations=2
            )
        ]
        self.storage.client.insert_rows_json.return_value = ["Error"]

        # Act & Assert
        with self.assertRaises(Exception):
            self.storage.insert_data("test_table", test_data)

    def test_remove_table(self):
        """Test table removal."""
        # Arrange
        table_name = "test_table"

        # Act
        self.storage.remove_table(table_name)

        # Assert
        self.storage.client.delete_table.assert_called_once()

if __name__ == '__main__':
    unittest.main()
