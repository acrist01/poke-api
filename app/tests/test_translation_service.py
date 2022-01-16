import unittest
from unittest.mock import MagicMock, patch
from Services.TranslationService import TranslationService
from Wrappers.HttpClient import HttpClient

http_client = HttpClient()

class TestTranslationService(unittest.TestCase):

    def test_translate_with_exception(self):
        
        http_client.post = MagicMock(return_value=Exception())
        translator = TranslationService('any', 'any', http_client)
        result = translator.translate('text', 'yoda')
        self.assertEqual('text', result)

    def test_translate_with_valid_return(self):

        http_client.post = MagicMock(return_value={'contents': {'translated' : 'translated_text'}})
        translator = TranslationService('any', 'any', http_client)
        result = translator.translate('text', 'yoda')
        self.assertEqual('translated_text', result)
