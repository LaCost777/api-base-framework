import json
import logging
import pytest
import random
import string

from datetime import date
from clients.restcl import RestBookServiceClient

from hamcrest import assert_that, equal_to, has_length

XFAIL = pytest.mark.xfail


class TestBookCreationPositive:

    def setup_class(self):
        self.LOG = logging.getLogger(f"{self.__class__.__name__}")
        self.B00K_SERVICE = RestBookServiceClient()

    def teardown_class(self):
        print("teardown_class called once for the class")

    def setup_method(self):
        """ Ensure there is 0 books in Service, if not - remove all book(s). Unfortunately, the dependency on
         DELETE /manipulations exists. No DB Service."""
        self.EXISTING_BOOKS_RESP = json.loads(self.B00K_SERVICE.search_books().text)
        if self.EXISTING_BOOKS_RESP == self.B00K_SERVICE.DICT_NO_BOOKS:
            pass
        else:
            [self.B00K_SERVICE.remove_book(i['id']) for i in self.EXISTING_BOOKS_RESP]

        # Double check.
        self.EXISTING_BOOKS_RESP = json.loads(self.B00K_SERVICE.search_books().text)
        assert self.EXISTING_BOOKS_RESP == self.B00K_SERVICE.DICT_NO_BOOKS
        self.LOG.debug("Service is Empty. There is No Book. setup_class called once for the class")

    def teardown_method(self):
        print("  teardown_method called for every method")

    @pytest.mark.parametrize("test_book_type", ("Drama", "Science", "Satire",
                                                pytest.param("Action and Adventure", marks=XFAIL(reason="JIRA-1001")),
                                                "Romance"))
    def test_create_book_type_(self, test_book_type):
        book_body = {"title": "TestAutoSmartQA", "type": test_book_type, "creation_date": f"{date.today().isoformat()}"}
        response = self.B00K_SERVICE.create_book(book_body)

        self.B00K_SERVICE.validate_book_was_created(response, test_book_type)
        book_id = json.loads(response.text)["id"]

        # GET created book, by id.
        resp = self.B00K_SERVICE.search_book_info(book_id=book_id)

        # Validate book type.
        assert json.loads(response.text)["type"] == test_book_type

    @pytest.mark.parametrize("date_format", (pytest.param(None, marks=XFAIL(reason="JIRA-1002")),
                                             f"{date.today().isoformat()}",))
    def test_create_book_with_valid_creation_date_(self, date_format):
        # Create a book.
        book_body = {"title": "TestAutoSmartQA", "type": "Drama", "creation_date": f"{date_format}"}
        response = self.B00K_SERVICE.create_book(book_body)

        self.B00K_SERVICE.validate_book_was_created(response, date_format)
        book_id = json.loads(response.text)["id"]
        # GET created book, by id.
        resp = self.B00K_SERVICE.search_book_info(book_id=book_id)

        # Validate created_date.
        assert json.loads(resp.text)["creation_date"] == date_format

    def test_create_book_with_missing_creation_date_field(self):
        # Create a book.
        book_body = {"title": "TestAutoSmartQA", "type": "Drama"}
        response = self.B00K_SERVICE.create_book(book_body)
        self.B00K_SERVICE.validate_book_was_created(response, book_body)
        book_id = json.loads(response.text)["id"]

        # GET created book, by id.
        resp = self.B00K_SERVICE.search_book_info(book_id=book_id)

        # Validate created_date.
        assert json.loads(resp.text)["creation_date"] is None

    # weak test data just to save time.
    @pytest.mark.parametrize("test_book_title",
                             ("",
                              "".join(random.choices(string.ascii_uppercase + string.digits, k=156)),
                              "".join(random.choices(string.ascii_uppercase + string.digits, k=255)),
                              "".join(random.choices(string.ascii_uppercase + " ", k=25)),
                              ),
                             ids=("empty string '' ", "random_string_156", "random_string_max_length", "with spaces",))
    def test_create_book_valid_title(self, test_book_title):
        book_body = {"title": test_book_title, "type": "Drama", "creation_date": f"{date.today().isoformat()}"}
        response = self.B00K_SERVICE.create_book(book_body)

        self.B00K_SERVICE.validate_book_was_created(response, test_book_title)
        book_id = json.loads(response.text)["id"]

        # GET created book, by id.
        resp = self.B00K_SERVICE.search_book_info(book_id=book_id)

        # Validate title.
        assert_that(json.loads(response.text)["title"], equal_to(test_book_title),
                    "POSTed title is NOT same in GET request.")