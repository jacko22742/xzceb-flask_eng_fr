"""Importing MyMemoryTranslator from deep_translator"""
from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    """translate_english_to_french translate an english text to french language"""
    french_text= MyMemoryTranslator(source="en-GB", target="fr-FR").translate(text=english_text)
    return french_text


def french_to_english(french_text):
    """translate_french_to_english translate an french text to english language"""
    english_text= MyMemoryTranslator(source="fr-FR", target="en-GB").translate(text=french_text)
    return english_text
