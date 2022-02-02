import logging
import requests


class RestBookServiceClient:

    ROOT_PATH = "/v1/books"
    ENDPOINTS = {
        "ids": ROOT_PATH + "/ids",
        "info": ROOT_PATH + "/info",
        "latest": ROOT_PATH + "/latest",
        "manipulation": ROOT_PATH + "/manipulation"
        }
    DICT_NO_BOOKS = {'message': 'There is no such book | books.'}

    def __init__(self, scheme="http", host="127.0.0.1", port="5000"):
        self.url = "{0}://{1}:{2}".format(scheme, host, port)
        self.log = logging.getLogger(f"{self.__class__.__name__}")

    def create_book(self, body):
        self.log.debug(f"Attempt to POST book: {body}"
                       f"to {self.url+RestBookServiceClient.ENDPOINTS['manipulation']} endpoint.")
        resp = requests.post(self.url+RestBookServiceClient.ENDPOINTS["manipulation"],
                             json=body,
                             timeout=5)
        return resp

    def update_book(self, body, book_id):
        self.log.debug(f"Attempt to UPDATE book: {body}"
                       f"and URL is {self.url+RestBookServiceClient.ENDPOINTS['manipulation']}")
        resp = requests.put(self.url+RestBookServiceClient.ENDPOINTS["manipulation"],
                            json=body,
                            params=({"id": book_id}),
                            timeout=5)
        return resp

    def remove_book(self, book_id):
        self.log.debug(f"Attempt to DELETE 1 book by specified 'id' param: {book_id}")
        resp = requests.delete(self.url+RestBookServiceClient.ENDPOINTS['manipulation'],
                               params=({"id": book_id}), timeout=5)
        return resp

    def search_book_info(self, book_id):
        self.log.debug(f"Attempt to GET /info of the book by specified 'id' param: {book_id}")
        resp = requests.get(self.url+RestBookServiceClient.ENDPOINTS['info'],
                            params=({"id": book_id}), timeout=5)
        return resp

    def search_books(self, limit=100000000):
        self.log.debug(f"Attempt to GET /latest created books (or all) sliced by 'limit' param. Current: {limit}")
        resp = requests.get(self.url+RestBookServiceClient.ENDPOINTS['latest'],
                            params=({"limit": limit}), timeout=5)
        return resp

    def search_all_books_by_type(self, book_type):
        self.log.debug(f"Attempt to GET /ids (full information of the books) by type. Current: {book_type}")
        resp = requests.get(self.url+RestBookServiceClient.ENDPOINTS['ids'],
                            params=({"ids": book_type}), timeout=5)
        return resp

    @staticmethod
    def validate_book_was_created(response, test_data):
        assert response.status_code == 200, f"Book was NOT created with data {test_data}, {response.status_code}"