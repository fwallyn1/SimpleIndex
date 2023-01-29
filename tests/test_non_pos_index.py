import unittest
from index.non_pos_index import NonPosIndex

class TestNonPosIndex(unittest.TestCase):
    def test_tokenize(self):
        #GIVEN
        title = "Un titre comme les autres !"
        index = NonPosIndex()

        #WHEN
        tokens = index.tokenize(title)

        #THEN
        self.assertEqual(tokens, ['un','titre','comme','les', 'autres'])

    def test_index(self):
        #GIVEN
        urls = ["https://fr.wikipedia.org/wiki/Karine_Lacombe","https://fr.wikipedia.org/wiki/Nuit_de_Cristal"]
        index = NonPosIndex(urls)
        res = {
            "karine": [{0:1}],
            "—":[{0:1},{1:1}],
            "wikipédia":[{0:1},{1:1}],
            "lacombe" : [{0:1}],
            "nuit" : [{1:1}],
            "de" : [{1:1}],
            "cristal" : [{1:1}]
        }
        #WHEN
        index.create_inverse_index()
        reverse_index = index.get_inverse_index()
        print(index)
        #THEN
        self.assertDictEqual(res,reverse_index)