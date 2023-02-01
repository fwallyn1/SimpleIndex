import unittest
from index.pos_index import PosIndex

class TestPosIndex(unittest.TestCase):
    def test_index(self):
        #GIVEN
        urls = ["https://fr.wikipedia.org/wiki/Karine_Lacombe","https://fr.wikipedia.org/wiki/Nuit_de_Cristal"]
        index = PosIndex(urls)
        res = {
            "karine": [{0: {"count": 1, "position": [0]}}], 
            "lacombe": [{0: {"count": 1, "position": [1]}}],
            "—": [{0: {"count": 1, "position": [2]}}, {1: {"count": 1, "position": [3]}}],
            "wikipédia": [{0: {"count": 1, "position": [3]}}, {1: {"count": 1, "position": [4]}}],
            "nuit": [{1: {"count": 1, "position": [0]}}], 
            "de": [{1: {"count": 1, "position": [1]}}], 
            "cristal": [{1: {"count": 1, "position": [2]}}]
        }
        #WHEN
        index.create_inverse_index()
        reverse_index = index.get_inverse_index()
        print(index)
        #THEN
        self.assertDictEqual(res,reverse_index)