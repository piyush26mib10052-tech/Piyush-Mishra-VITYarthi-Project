# Vityarthi Hospital Management System

## Overview
A menu-driven, command-line Hospital Management System written in Python. It lets hospital staff register patients, look up and update their records, book appointments, generate bills, and discharge patients, all from one simple text menu.

Patient, appointment and billing data is stored in memory (Python lists and dictionaries) while the program runs.

## Features
- **Patient registration**: add a patient with ID, name, age, gender, phone, address, blood group and disease. Duplicate IDs are rejected.
- **View patient details**: list all registered patients.
- **Search patient**: find a patient by ID and see name, age, blood group and status.
- **Update patient**: change a patient's name, age and disease.
- **Book appointment**: schedule an appointment with a doctor for a registered patient.
- **Billing**: calculate a total from doctor fee, medicine cost and room rent.
- **Discharge**: mark a patient as discharged.
- **Input validation**: age and bill amounts only accept whole numbers.

## Technologies / Tools Used
- Python 3
- Python standard library only (`time` module), so no extra installs are needed

## Steps to Install & Run
1. Install Python 3 from https://www.python.org/downloads/ (skip if already installed).
2. Download or clone this repository:
   ```
   git clone https://github.com/piyush26mib10052-tech/Piyush-Mishra-VITYarthi-Project.git
   cd Piyush-Mishra-VITYarthi-Project
   ```
3. Run the program:
   ```
   python hospital_management.py
   ```
   (On some systems use `python3` instead of `python`.)
4. Choose an option from the menu by typing its number (1-8).

## Instructions for Testing
Manual test cases you can run from the menu:

| # | Test | Steps | Expected result |
|---|------|-------|-----------------|
| 1 | Add patient | Option 1, enter valid details | "Patient Saved!!!" |
| 2 | Duplicate ID | Option 1 again with the same ID | "This patient already exists!" |
| 3 | Invalid age | Option 1, enter `abc` as age | Asks again for a valid whole number |
| 4 | View all | Option 2 | Registered patients are listed |
| 5 | Search (found) | Option 3 with an existing ID | Patient details shown |
| 6 | Search (not found) | Option 3 with an unknown ID | "Sorry,No Patient Found With This ID" |
| 7 | Update | Option 4 with an existing ID | "Details Updated." |
| 8 | Appointment | Option 5 with an existing ID | "Appointment Booked!" |
| 9 | Appointment (unregistered) | Option 5 with an unknown ID | "REGISTER PATIENT FIRST!" |
| 10 | Billing | Option 6, enter fees | Total bill is displayed |
| 11 | Discharge | Option 7, then search the same ID | Status shows DISCHARGED |
| 12 | Exit | Option 8 | Program exits |

## Limitations
Data is not saved to a file or database, so all records are lost when the program exits.

## Author
Piyush Mishra, Registration No. MIB10052
GitHub: [piyush26mib10052-tech](https://github.com/piyush26mib10052-tech)
