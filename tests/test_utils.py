import unittest
from unittest.mock import patch, MagicMock
import os
import sys

# Add the parent directory to the sys.path to allow imports from the main project
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import rewrite_document, extract_type_info, get_empty_fields, read_single_pdf

class TestUtils(unittest.TestCase):

    @patch('utils.ChatOpenAI')
    @patch('utils.ChatPromptTemplate')
    @patch('utils.StrOutputParser')
    def test_rewrite_document(self, MockStrOutputParser, MockChatPromptTemplate, MockChatOpenAI):
        # Mock the Langchain components
        mock_model = MockChatOpenAI.return_value
        mock_parser = MockStrOutputParser.return_value
        mock_prompt = MockChatPromptTemplate.from_messages.return_value

        # Mock the chain and its invoke method
        mock_chain = MagicMock()
        mock_prompt.__or__.return_value = mock_chain
        mock_chain.__or__.return_value = mock_chain

        # Define the expected output from the chain
        expected_output = "This is the rewritten document."
        mock_chain.invoke.return_value = expected_output

        # Input for the function
        full_text = "This is the original document."
        info_to_add = {"new_info": "This is new information."}

        # Call the function
        result = rewrite_document(full_text, info_to_add)

        # Assertions
        self.assertEqual(result, expected_output)

        # Verify that the mocked components were called correctly
        MockChatOpenAI.assert_called_once_with(temperature=0, model="gpt-4o-mini")
        mock_chain.invoke.assert_called_once_with({
            "full_text": full_text,
            "info_to_add": str(info_to_add)
        })

    def test_extract_type_info(self):
        self.assertEqual(extract_type_info("<class 'str'>"), "str")
        self.assertEqual(extract_type_info("typing.Optional[str]"), "str")
        self.assertEqual(extract_type_info("int"), "int")

    def test_get_empty_fields(self):
        self.assertEqual(get_empty_fields({"a": "", "b": [], "c": False, "d": 0}), ["a", "b", "c", "d"])
        self.assertEqual(get_empty_fields({"a": "hello", "b": [1], "c": True, "d": 1}), [])

if __name__ == '__main__':
    unittest.main()
