#!/usr/bin/python3

import unittest
from model.review import Review
from persistence.review_repository import ReviewRepository


class TestReviewRepository(unittest.TestCase):

    def setUp(self):
        self.repository = ReviewRepository()

    def test_save_review(self):
        review = Review("Sayyara Alaks", "Amazing product!")
        self.repository.save(review)
        self.assertIn(review.review_id, self.repository.reviews)

    def test_save_review_with_existing_id(self):
        review = Review("Kenan", "best review")
        review.review_id = 5
        self.repository.save(review)
        self.assertEqual(self.repository.reviews[5].author, "Kenan")

    def test_get_review(self):
        review = Review("Farid", "Nice plase and services")
        self.repository.save(review)
        retrieved_review = self.repository.get(review.review_id)
        self.assertEqual(retrieved_review.author, "Farid")

    def test_get_review_non_existing_id(self):
        retrieved_review = self.repository.get(100)
        self.assertIsNone(retrieved_review)

    def test_get_all_reviews(self):
        review1 = Review("Aygun", "smart review")
        review2 = Review("Ahmed", "not bad")
        self.repository.save(review1)
        self.repository.save(review2)
        all_reviews = self.repository.get_all()
        self.assertEqual(len(all_reviews), 2)

    def test_update_review(self):
        review = Review("Alekper", "Delices")
        self.repository.save(review)
        update_data = {"author": "Alekper Updated",
                       "content": "Super delices!"}
        self.repository.update(review.review_id, update_data)
        updated_review = self.repository.get(review.review_id)
        self.assertEqual(updated_review.author, "Alekper Updated")
        self.assertEqual(updated_review.content, "Super delices!")

    def test_update_non_existing_review(self):
        update_data = {"author": "Zuzu",
                       "content": "This dont work"}
        result = self.repository.update(100, update_data)
        self.assertFalse(result)

    def test_delete_review(self):
        review = Review("Isa", "Bad place")
        self.repository.save(review)
        self.repository.delete(review.review_id)
        deleted_review = self.repository.get(review.review_id)
        self.assertIsNone(deleted_review)

    def test_delete_non_existing_review(self):
        result = self.repository.delete(100)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
