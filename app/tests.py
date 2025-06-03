import math
import sqlite3
import unittest

from django.test import TestCase
from django.db import connection

from app.models import Note

# Create your tests here.


@unittest.skipUnless(connection.vendor == "sqlite", "This test is only for SQLite")
class NoteTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.notes = [
            Note(title=f"Test Note {i}", content="This is a test note.")
            for i in range(2**14)
        ]

    def test_note_creation(self):
        limit = connection.connection.getlimit(sqlite3.SQLITE_LIMIT_VARIABLE_NUMBER)
        num_fields = 2  # title and content
        batch_size = limit // num_fields
        with self.assertNumQueries(math.ceil(len(self.notes) / batch_size)):
            Note.objects.bulk_create(self.notes)
