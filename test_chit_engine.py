import unittest
from chit_engine import Member, ChitFundEngine


class TestChitFundSystem(unittest.TestCase):

    def test_member_creation(self):
        member = Member("M001", "Member1", "G001")

        self.assertEqual(member.member_id, "M001")
        self.assertEqual(member.name, "Member1")
        self.assertFalse(member.has_won)

    def test_payment_recorded(self):
        engine = ChitFundEngine()
        member = Member("M001", "Member1", "G001")
        engine.members["M001"] = member

        engine.record_payment("M001", 5000)

        self.assertEqual(member.total_paid, 5000)

    def test_invalid_payment(self):
        engine = ChitFundEngine()
        member = Member("M001", "Member1", "G001")
        engine.members["M001"] = member

        engine.record_payment("M001", 0)

        self.assertEqual(member.total_paid, 0)

    def test_load_groups(self):
        engine = ChitFundEngine()
        engine.load_groups()

        self.assertIn("G001", engine.groups)
        self.assertEqual(engine.groups["G001"].chit_value, 100000)
        self.assertEqual(engine.groups["G001"].duration, 12)

    def test_load_members(self):
        engine = ChitFundEngine()
        engine.load_groups()
        engine.load_members()

        self.assertEqual(len(engine.members), 4)
        self.assertIn("M001", engine.members)


if __name__ == "__main__":
    unittest.main()