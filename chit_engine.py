
import csv
from pathlib import Path

# Project ID: T081-PS-028
# Chit Fund Management System

BASE_DIR = Path(__file__).resolve().parent


class Member:
    def __init__(self, member_id, name, group_id):
        self.member_id = member_id
        self.name = name
        self.group_id = group_id
        self.total_paid = 0.0
        self.outstanding = 0.0
        self.has_won = False
        self.consecutive_defaults = 0
        self.is_defaulter = False


class ChitGroup:
    def __init__(self, group_id, chit_value, duration, random_seed):
        self.group_id = group_id
        self.chit_value = chit_value
        self.duration = duration
        self.random_seed = random_seed
        self.current_month = 1
        self.members = []


class ChitFundEngine:
    def __init__(self):
        self.groups = {}
        self.members = {}

    def load_groups(self):
        file_path = BASE_DIR / "groups.csv"

        with file_path.open(
            "r", newline="", encoding="utf-8"
        ) as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                group_id = row["group_id"].strip()

                if not group_id:
                    raise ValueError("Group ID cannot be empty.")

                if group_id in self.groups:
                    raise ValueError(
                        f"Duplicate group ID: {group_id}"
                    )

                chit_value = float(row["chit_value"])
                duration = int(row["duration"])
                random_seed = int(row["random_seed"])

                if chit_value <= 0 or duration <= 0:
                    raise ValueError(
                        "Chit value and duration must be positive."
                    )

                self.groups[group_id] = ChitGroup(
                    group_id,
                    chit_value,
                    duration,
                    random_seed
                )

    def load_members(self):
        file_path = BASE_DIR / "members.csv"

        with file_path.open(
            "r", newline="", encoding="utf-8"
        ) as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                member_id = row["member_id"].strip()
                name = row["name"].strip()
                group_id = row["group_id"].strip()

                if not member_id or not name:
                    raise ValueError(
                        "Member ID and name cannot be empty."
                    )

                if member_id in self.members:
                    raise ValueError(
                        f"Duplicate member ID: {member_id}"
                    )

                if group_id not in self.groups:
                    raise ValueError(
                        f"Group {group_id} does not exist."
                    )

                member = Member(member_id, name, group_id)

                self.members[member_id] = member
                self.groups[group_id].members.append(member)

    def show_report(self):
        print("\nCHIT FUND MANAGEMENT SYSTEM")
        print("Project ID: T081-PS-028")
        print("-" * 40)

        for group in self.groups.values():
            print(f"\nGroup ID: {group.group_id}")
            print(f"Chit Value: Rs. {group.chit_value:.2f}")
            print(f"Duration: {group.duration} months")
            print(f"Current Month: {group.current_month}")
            print(f"Number of Members: {len(group.members)}")

            print("\nMember Details:")

            for member in group.members:
                print(
                    f"{member.member_id} - {member.name} "
                    f"- Paid: Rs. {member.total_paid:.2f}"
                )

        print("\nProject setup completed successfully!")


def main():
    try:
        engine = ChitFundEngine()
        engine.load_groups()
        engine.load_members()
        engine.show_report()

    except FileNotFoundError as error:
        print("Error: Required CSV file not found.")
        print(error.filename)

    except (ValueError, KeyError) as error:
        print(f"Invalid input: {error}")

    except OSError as error:
        print(f"File error: {error}")


if __name__ == "__main__":
    main()
