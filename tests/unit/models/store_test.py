from models.store import StoreModel
from tests.base_test import BaseTest


class StoreTest(BaseTest):
    def test_create_store(self):
        store = StoreModel('test')


        self.assertListEqual(store.items.all(), [],
                            "The store's items length was not 0 even though no items were added.")

    def test_store_json(self):
        store = StoreModel('test')
        expected = {
            'id': None,
            'name': 'test',
            'items': []
        }

        self.assertDictEqual(store.json(), expected)
