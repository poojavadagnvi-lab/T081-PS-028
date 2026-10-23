T081-PS-028 — Chit Fund Management System

1. Project Overview

The Chit Fund Management System is a command-file-driven application designed to manage the monthly activities of a chit fund group.

The system aims to automate member payment tracking, late payment penalties, auction processing, prize distribution, dividend calculations, defaulter management, and final settlement.

2. Project Objectives

- Maintain chit group and member information.
- Track monthly payments and outstanding balances.
- Calculate late payment penalties according to the business rules.
- Identify eligible bidders.
- Process auctions and select winners.
- Calculate prize money, foreman commission, and member dividends.
- Track payment defaults and member substitutions.
- Generate monthly statements and final reports.

3. Technologies Used

- Python 3
- CSV files
- Git
- GitHub
- Visual Studio Code

4. Project Structure

T081-PS-028/
├── DESIGN.md
├── chit_engine.py
├── groups.csv
├── members.csv
├── commands.csv
└── README.md

5. File Description

- DESIGN.md: Describes the system design, modules, workflow, and business rules.
- chit_engine.py: Contains the Python implementation of the system.
- groups.csv: Stores chit group configuration.
- members.csv: Stores member information.
- commands.csv: Stores sample monthly commands for processing.
- README.md: Provides project information and setup instructions.

6. Prerequisites

- Python 3 installed on the computer.
- Visual Studio Code or another Python-compatible editor.

No external Python packages are required for the current starter implementation because it uses Python's built-in modules.

7. Setup Instructions

1. Create or open the "T081-PS-028" project folder in Visual Studio Code.
2. Place all project files in the same folder.
3. Ensure that "groups.csv" and "members.csv" contain valid data.
4. Open the terminal in Visual Studio Code.
5. Run the application using the command below.

python chit_engine.py

On systems where Python is invoked as "python3", use:

python3 chit_engine.py

8. Input Data

groups.csv

Contains the group ID, total chit value, duration in months, and random seed.

members.csv

Contains each member's unique ID, name, and associated group ID.

commands.csv

Contains sample monthly actions intended for future command-processing functionality.

9. Current Implementation Status

The initial version establishes the basic data structures for members and chit groups. It loads group and member information from CSV files, validates basic input data, and displays a summary report.

Payment collection, late penalties, auction processing, dividend distribution, default management, command-file execution, and final settlement require further implementation and testing.

10. Testing

The initial version can be tested by:

1. Running the Python program.
2. Verifying that the group information is displayed.
3. Checking that all member records are loaded.
4. Testing error handling for missing files and invalid data.

Further tests will be added as the remaining business rules are implemented.

11. Expected Outcome

The completed system is intended to provide a structured way to manage chit fund operations, maintain member records, apply business rules consistently, and generate monthly and final financial reports.

12. Future Enhancements

- Complete command-file processing.
- Automated payment and penalty calculations.
- Auction and dividend processing.
- Defaulter and guarantor management.
- Monthly and final settlement reports.
- Automated testing of all official business rules.

13. Project Status

Current phase: Week 1 — Initial project setup and design.

The implementation will be developed incrementally according to the official project requirements.