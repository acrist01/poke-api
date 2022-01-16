import unittest
from unittest.mock import MagicMock, patch
from Services.TranslationService import TranslationService
from Services.PokemonService import PokemonService
from Wrappers.HttpClient import HttpClient

http_client = HttpClient()
translation_service = TranslationService('any', 'any', http_client)

class TestPokemonService(unittest.TestCase):

    def test_get_pokemon_details_should_return_not_found(self):
        
        http_client.get = MagicMock(return_value=Exception)
        poke_service = PokemonService(http_client, translation_service, 'any')
        result = poke_service.get_pokemon_details('any', True)
        expected = {'status': 404, 'message': 'Pokemon not found'}
        self.assertEqual(expected, result)

    def test_get_pokemon_details_should_return_translated_to_yoda_description(self):
        
        poke_api_return_mock = {
            'habitat': {'name': 'cave'},
            'is_legendary': False,
            'flavor_text_entries': 'any at this point',
            'name': 'Pikachu'
        }

        http_client.get = MagicMock(return_value=poke_api_return_mock)
        translation_service.translate = MagicMock(return_value='translated into yoda description')

        poke_service = PokemonService(http_client, translation_service, 'any')
        poke_service.get_description = MagicMock(return_value='pokemon description')

        result = poke_service.get_pokemon_details('any', True)
        expected = {'description': 'translated into yoda description', 'habitat': 'cave', 'isLegendary': False, 'name': 'Pikachu' }
        self.assertEqual(expected, result)

    def test_get_pokemon_details_should_return_translated_to_yoda_description2(self):
        
        poke_api_return_mock = {
            'habitat': {'name': 'forrest'},
            'is_legendary': True,
            'flavor_text_entries': 'any at this point',
            'name': 'Pikachu'
        }

        http_client.get = MagicMock(return_value=poke_api_return_mock)
        translation_service.translate = MagicMock(return_value='translated into yoda description')

        poke_service = PokemonService(http_client, translation_service, 'any')
        poke_service.get_description = MagicMock(return_value='pokemon description')

        result = poke_service.get_pokemon_details('any', True)
        expected = {'description': 'translated into yoda description', 'habitat': 'forrest', 'isLegendary': True, 'name': 'Pikachu' }
        self.assertEqual(expected, result)

    def test_get_pokemon_details_should_return_translated_into_shakespeare_description(self):
        
        poke_api_return_mock = {
            'habitat': {'name': 'forrest'},
            'is_legendary': False,
            'flavor_text_entries': 'any at this point',
            'name': 'Pikachu'
        }

        http_client.get = MagicMock(return_value=poke_api_return_mock)
        translation_service.translate = MagicMock(return_value='translated into shakespeare description')

        poke_service = PokemonService(http_client, translation_service, 'any')
        poke_service.get_description = MagicMock(return_value='pokemon description')

        result = poke_service.get_pokemon_details('any', True)
        expected = {'description': 'translated into shakespeare description', 'habitat': 'forrest', 'isLegendary': False, 'name': 'Pikachu' }
        self.assertEqual(expected, result)

    def test_get_pokemon_details_should_return_non_translated_description(self):
        
        poke_api_return_mock = {
            'habitat': {'name': 'forrest'},
            'is_legendary': False,
            'flavor_text_entries': 'any at this point',
            'name': 'Pikachu'
        }

        http_client.get = MagicMock(return_value=poke_api_return_mock)

        poke_service = PokemonService(http_client, translation_service, 'any')
        poke_service.get_description = MagicMock(return_value='pokemon description')

        result = poke_service.get_pokemon_details('any', False)
        expected = {'description': 'pokemon description', 'habitat': 'forrest', 'isLegendary': False, 'name': 'Pikachu' }
        self.assertEqual(expected, result)

    def test_get_description_should_return_the_first_english_flavor_text(self):
        
        mock_entries = [
            {
                'language': {'name': 'fr'},
                'flavor_text': 'description du pokemon'
            },
            {
                'language': {'name': 'en'},
                'flavor_text': 'pokemon description'
            }
        ]

        poke_service = PokemonService(http_client, translation_service, 'any')
        result = poke_service.get_description(mock_entries)
        expected = 'pokemon description'
        self.assertEqual(expected, result)

    def test_get_description_should_remove_special_chars_and_trailing_spaces(self):
        
        mock_entries = [
            {
                'language': {'name': 'en'},
                'flavor_text': ' pokemon\fdescription\n '
            }
        ]

        poke_service = PokemonService(http_client, translation_service, 'any')
        result = poke_service.get_description(mock_entries)
        expected = 'pokemon description'
        self.assertEqual(expected, result)


