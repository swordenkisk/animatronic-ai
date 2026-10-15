import random
import unittest

from showbot import classify, respond


class ShowbotTests(unittest.TestCase):
    def test_greeting_selects_greeting_cue(self):
        self.assertEqual(classify("Hey, how's it going?"), "greeting")

    def test_ai_question_selects_ai_cue(self):
        self.assertEqual(classify("What is AI?"), "ai")

    def test_unmatched_message_uses_fallback(self):
        self.assertEqual(classify("Tell me about the weather"), "fallback")

    def test_response_is_reproducible_with_seed(self):
        first = respond("How does it work?", random.Random(7))
        second = respond("How does it work?", random.Random(7))
        self.assertEqual(first, second)

    def test_goodbye_selects_farewell_cue(self):
        self.assertEqual(classify("Goodbye"), "farewell")


if __name__ == "__main__":
    unittest.main()
