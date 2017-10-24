# -*- coding: utf-8 -*-
"""Tests the utils module"""

import unittest

from wrapper.utils import remove_diacritics

class TestRemoveDiacritics(unittest.TestCase):
    """Tests the remove_diacritics function"""

    def test_remove_diacritics(self):
        """Tests the remove diacritics function"""
        before = u"Automático"
        after_ = remove_diacritics(before)
        self.assertEqual("Automatico", after_)

        before = u"álcool"
        after_ = remove_diacritics(before)
        self.assertEqual("alcool", after_)

        before = u"direção hidráulica"
        after_ = remove_diacritics(before)
        self.assertEqual("direcao hidraulica", after_)
