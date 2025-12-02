# GPA Converter

A professional desktop application for converting A-Level grades to multiple international grading systems (American, European, German, and UCAS), built with Python and Tkinter.

---

## ✨ Features

- **Dual Calculation Modes**:
  - **Standard Calculation**: Convert letter grades (A*, A, B, etc.) to GPA systems
  - **Precise Calculation (PUM)**: Use Percentage Uniform Marks (0-100) for more accurate conversions
- **Multiple Grading Systems**:
  - American GPA (4.0 scale)
  - European GPA (100 scale)
  - German GPA (Bavarian formula)
  - UCAS Tariff points
- **User-Friendly Interface**:
  - Clean, modern UI with professional color scheme
  - Tabbed interface for easy navigation
  - Dynamic subject addition/removal
  - Real-time calculation results
- **Professional Design**:
  - Consistent blue/yellow color palette
  - Clearly labeled input/output sections
  - Responsive layout

---

## 🛠️ Installation & Requirements

### Prerequisites
- Python 3.7 or higher
- Tkinter (usually included with Python)

### Installation
1. Clone the repository or download the `Conversator.py` file
2. Ensure Python is installed on your system
3. Run the application:



# Mark-equivalent-Edu-proj-
Grading Systems Explained
System	Scale	Description
American GPA	0.0 - 4.0	Standard U.S. university grading
European GPA	0 - 100	Common European percentage-based system
German GPA	1.0 - 6.0	Bavarian formula (1.0 = best, 6.0 = worst)
UCAS Points	0 - 168	UK university admissions tariff

<img width="812" height="465" alt="image" src="https://github.com/user-attachments/assets/75c6fdc7-c2fb-40ef-9f38-ac263b7300c3" />

A-Level Grade	American GPA	European GPA	German GPA	UCAS Points
A*	            4.0          	100          	1.0        	56
A	              4.0	          85	          1.0	        48
B	              3.3         	75          	1.5        	40
C             	2.65        	65          	2.0       	32
D	              2.0         	55          	2.5        	24
E	              1.0         	45           	3.0       	16
📖 How to Use
Standard Calculation Tab
Select a subject from the dropdown menu

Choose the corresponding grade (A*, A, B, C, D, E)

Click "+ Add Subject" to add more subjects

Click "Calculate All GPA" to see conversions

Results appear instantly in four different systems

Precise Calculation (PUM) Tab
Select subject and grade as above

Enter the Percentage Uniform Mark (0-100) for finer granularity

Add multiple subjects as needed

Click "Calculate with PUM" for precision conversions

Controls
+ Add Subject: Add another subject row

× Button: Remove specific subject row (available after first row)

Clear All: Reset all inputs and results

Calculate: Perform conversions for all systems
 🎨 UI Components
Color Scheme
Primary: #2C5AA0 (Blue)

Secondary: #E6F0FF (Light blue)

Accent: #FFD700 (Yellow for buttons)

Success: #28A745 (Green for results)

Background: #2C5AA0 (Blue)

Card Background: #FFFFFF (White)

Layout Sections
Header: Application title and description

Input Area: Subject selection with dropdowns and PUM entry

Control Panel: Action buttons (Add, Calculate, Clear)

Results Panel: Four GPA system displays

Footer: Creator credits
 
 🧩Code Structure
The application follows an object-oriented design:

GPAConverter Class: Main application class

__init__(): Initializes UI and tabs

setup_standard_tab(): Configures standard calculation interface

setup_advanced_tab(): Configures PUM-based calculation interface

Calculation methods for each grading system

UI management methods for dynamic rows

Key Methods
calculate_american_gpa(): Converts to 4.0 scale

calculate_european_gpa(): Converts to 100-point scale

calculate_german_gpa(): Applies Bavarian formula

calculate_ucas_points(): Calculates UCAS tariff

PUM variants for precision calculations
