import unittest
import os
import logging
from unittest.mock import patch, MagicMock
from utils.logger import setup_logger

class TestLogger(unittest.TestCase):
    def setUp(self):
        """Set up test cases."""
        # Create a temporary log directory for testing
        self.test_log_dir = "test_logs"
        if not os.path.exists(self.test_log_dir):
            os.makedirs(self.test_log_dir)

    def tearDown(self):
        """Clean up after tests."""
        # Remove test log files and directory
        if os.path.exists(self.test_log_dir):
            for file in os.listdir(self.test_log_dir):
                os.remove(os.path.join(self.test_log_dir, file))
            os.rmdir(self.test_log_dir)

    def test_logger_setup(self):
        """Test logger setup and configuration."""
        # Act
        logger = setup_logger()

        # Assert
        self.assertEqual(logger.level, logging.DEBUG)
        # Verify we have 3 handlers (console, file, error file)
        self.assertEqual(len(logger.handlers), 3)
        
        # Check handlers configuration
        handlers = logger.handlers
        handler_levels = [h.level for h in handlers]
        # Should have one INFO handler (console) and one DEBUG handler (file)
        # and one ERROR handler (error file)
        self.assertIn(logging.INFO, handler_levels)
        self.assertIn(logging.DEBUG, handler_levels)
        self.assertIn(logging.ERROR, handler_levels)

    def test_log_file_creation(self):
        """Test that log files are created."""
        # Arrange & Act
        logger = setup_logger()
        test_message = "Test log message"
        logger.info(test_message)

        # Assert
        log_files = os.listdir("logs")
        self.assertTrue(any(file.startswith("app_") for file in log_files))
        self.assertTrue(any(file.startswith("error_") for file in log_files))

if __name__ == '__main__':
    unittest.main()
