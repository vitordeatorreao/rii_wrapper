"""Tests the regular expression wrapper"""

import unittest

from wrapper import RegexWrapper

class TestRegexWrapper(unittest.TestCase):
    """Tests the RegexWrapper class"""

    def test_fill_template(self):
        """Tests the fill_template method from the RegexWrapper class"""
        wrapper = RegexWrapper({
            "Brand": r"(fiat|gm|chevrolet|wv|volkswagen|ford)",
            "Model": r"^(\w+)[^\w]?([a-zA-Z]\w*)?[^\w]?([a-zA-Z]\w*)?[^\w]",
            "Motor": r"[^\w\.\,](\d\.\d)[^\w\.\,]",
            "Year": r"[^\w\.\,](\d{2,4})[^\w\.\,]",
            "Color": r"(branc\w?|prata|pret\w?|cinza|vermelh\w?|marrom|verde)",
            "Complete": r"comp\w+",
        })
        result = wrapper.fill_template("S10 2.8 03 branco, diesel, completo.")
        # assert that a not found regex will still be reproduced in the result
        self.assertTrue("Brand" in result)
        self.assertEqual("", result["Brand"]) # with an empty string
        # assert model is in the result and is correct
        self.assertTrue("Model" in result)
        self.assertEqual("S10", result["Model"])
        # assert motor is in the result and is correct
        self.assertTrue("Motor" in result)
        self.assertEqual("2.8", result["Motor"])
        # same for year
        self.assertTrue("Year" in result)
        self.assertEqual("03", result["Year"])
        # and color
        self.assertTrue("Color" in result)
        self.assertEqual("branco", result["Color"])
        # since "Complete" has no groups, it must come simply as "Complete"
        self.assertTrue("Complete" in result)
        self.assertEqual("Complete", result["Complete"])

        # test for another query string
        result = wrapper.fill_template(
            "ONIX LT 1.4 14 manual, flex, vermelha. R$ 38.990,00")
        self.assertTrue("Brand" in result)
        self.assertEqual("", result["Brand"])
        self.assertTrue("Model" in result)
        # if there is more than one group in the regex, they are joined by blank
        self.assertEqual("ONIX LT", result["Model"])
        self.assertTrue("Motor" in result)
        self.assertEqual("1.4", result["Motor"])
        self.assertTrue("Year" in result)
        self.assertEqual("14", result["Year"])
        self.assertTrue("Color" in result)
        self.assertEqual("vermelha", result["Color"])

        # test for another (this one has 3 names in the model)
        result = wrapper.fill_template("GOL L CL 1.6 89 alcool R$ 7.900,00")
        self.assertTrue("Brand" in result)
        self.assertEqual("", result["Brand"])
        self.assertTrue("Model" in result)
        # if there is more than one group in the regex, they are joined by blank
        self.assertEqual("GOL L CL", result["Model"])
        self.assertTrue("Motor" in result)
        self.assertEqual("1.6", result["Motor"])
        self.assertTrue("Year" in result)
        self.assertEqual("89", result["Year"])
        self.assertTrue("Color" in result)
        self.assertEqual("", result["Color"])
