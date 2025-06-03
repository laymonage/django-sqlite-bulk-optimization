from django.test import TestCase

from app.models import Note

# Create your tests here.


class NoteTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.notes = [
            Note(title=f"Test Note {i}", content="This is a test note.")
            for i in range(2**14)
        ]

    def test_note_creation(self):
        with self.assertNumQueries(2):
            Note.objects.bulk_create(self.notes)
