from unittest import TestCase

from decorator.registration import (
    registered,
    subject_1,
    subject_2,
    subject_3,
)


class DecorateTestCase(TestCase):

    def test_subject_1_is_decorated(self):
        status = getattr(subject_1, 'status', None)
        self.assertIsNotNone(status, 'subject_1 should have status attribute.')

    def test_subject_1_is_registered(self):
        self.assertIn(subject_1, registered)

    def test_subject_1_is_active(self):
        status = getattr(subject_1, 'status')
        self.assertEqual(status, 'active', 'subject_1 should be active.')

    def test_subject_2_is_decorated(self):
        status = getattr(subject_2, 'status', None)
        self.assertIsNotNone(status, 'subject_2 should have status attribute.')

    def test_subject_2_is_registered(self):
        self.assertNotIn(subject_2, registered)

    def test_subject_2_is_active(self):
        status = getattr(subject_2, 'status')
        self.assertEqual(status, 'inactive', 'subject_3 should be inactive.')

    def test_subject_3_is_decorated(self):
        status = getattr(subject_3, 'status', None)
        self.assertIsNotNone(status, 'subject_3 should have status attribute.')

    def test_subject_3_is_registered(self):
        self.assertIn(subject_3, registered)

    def test_subject_3_is_active(self):
        status = getattr(subject_3, 'status')
        self.assertEqual(status, 'active', 'subject_3 should be inactive.')

    def test_all_active_subjects_registered(self):
        self.assertIn(subject_1, registered, 'subject_1 should be in registered.')
        self.assertIn(subject_3, registered, 'subject_3 should be in registered.')

    def test_all_inactive_subjects_unregistered(self):
        self.assertNotIn(subject_2, registered, 'subject_2 should not be in registered.')
