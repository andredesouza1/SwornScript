import unittest
from unittest.mock import patch, MagicMock
from pydantic import BaseModel, Field
from typing import List
import os
import sys

# Add the parent directory to the sys.path to allow imports from the main project
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from query_builder import create_structured_output, YesorNo, Sentiment, create_param_tuple

# Define a simple Pydantic model for testing
class TestModel(BaseModel):
    name: str = Field(description="The name of the person")
    age: int = Field(description="The age of the person")

class TestQueryBuilder(unittest.TestCase):

    @patch('query_builder.ChatOpenAI')
    @patch('query_builder.JsonOutputParser')
    @patch('query_builder.PromptTemplate')
    def test_create_structured_output(self, MockPromptTemplate, MockJsonOutputParser, MockChatOpenAI):
        # Mock the Langchain components
        mock_model = MockChatOpenAI.return_value
        mock_parser = MockJsonOutputParser.return_value
        mock_prompt = MockPromptTemplate.return_value

        # Mock the chain and its invoke method
        mock_chain = MagicMock()
        mock_prompt.__or__.return_value = mock_chain
        mock_chain.__or__.return_value = mock_chain

        # Define the expected output from the chain
        expected_output = {"name": "John Doe", "age": 30}
        mock_chain.invoke.return_value = expected_output

        # Input text for the function
        full_text = "The person's name is John Doe and he is 30 years old."

        # Call the function
        result = create_structured_output(full_text, TestModel)

        # Assertions
        self.assertIsInstance(result, TestModel)
        self.assertEqual(result.name, "John Doe")
        self.assertEqual(result.age, 30)

        # Verify that the mocked components were called correctly
        MockChatOpenAI.assert_called_once_with(temperature=0, model="gpt-4o-mini")
        MockJsonOutputParser.assert_called_once_with(pydantic_object=TestModel)
        mock_chain.invoke.assert_called_once_with({"document": full_text})

    def test_create_param_tuple(self):
        # Test case 1: Required string
        name, (field_type, field) = create_param_tuple("name", "str", "The name of the person", required=True)
        self.assertEqual(name, "name")
        self.assertEqual(field_type, str)
        self.assertEqual(field.description, "The name of the person")

        # Test case 2: Optional integer
        name, (field_type, field) = create_param_tuple("age", "int", "The age of the person", required=False)
        self.assertEqual(name, "age")
        self.assertIn(int, field_type.__args__) # Check for Optional[int]
        self.assertEqual(field.description, "The age of the person")
        self.assertEqual(field.default, None)

        # Test case 3: List of strings
        name, (field_type, field) = create_param_tuple("items", "list", "A list of items", required=True)
        self.assertEqual(name, "items")
        self.assertEqual(field_type, List[str])
        self.assertEqual(field.description, "A list of items")

        # Test case 4: Enum type
        name, (field_type, field) = create_param_tuple("sentiment", "Sentiment", "The sentiment", required=True)
        self.assertEqual(name, "sentiment")
        self.assertEqual(field_type, Sentiment)
        self.assertEqual(field.description, "The sentiment")

if __name__ == '__main__':
    unittest.main()
