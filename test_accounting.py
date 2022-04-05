import copy
import unittest
import accounting


class AccountingTest(unittest.TestCase):
    def test_check_document_existance(self):
        existing_document_number = "11-2"
        self.assertTrue(accounting.check_document_existance(existing_document_number))

        non_existing_document_number = "34"
        self.assertFalse(accounting.check_document_existance(non_existing_document_number))

    def test_get_all_doc_owners_names(self):
        self.assertEqual(
            accounting.get_all_doc_owners_names(),
            {"Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"}
        )

    def test_delete_doc(self):
        documents = copy.deepcopy(accounting.documents)
        directories = copy.deepcopy(accounting.directories)
        non_existent = "123"
        self.assertIsNone(
            accounting.delete_doc(non_existent)
        )
        self.assertEqual(documents, accounting.documents)
        self.assertEqual(directories, accounting.directories)

        existent = "11-2"
        doc_number, deleted = accounting.delete_doc(existent)
        self.assertEqual(doc_number, existent)
        self.assertTrue(deleted)
        self.assertNotEqual(documents, accounting.documents)
        self.assertNotEqual(directories, accounting.directories)

    def test_add_new_shelf(self):
        directories = copy.deepcopy(accounting.directories)
        existent = "2"
        shelf_number, added = accounting.add_new_shelf(existent)
        self.assertEqual(shelf_number, existent)
        self.assertFalse(added)
        self.assertEqual(directories, accounting.directories)

        non_existent = "5"
        shelf_number, added = accounting.add_new_shelf(non_existent)
        self.assertEqual(shelf_number, non_existent)
        self.assertTrue(added)
        self.assertNotEqual(directories, accounting.directories)
