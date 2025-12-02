import tkinter as tk
from tkinter import ttk, messagebox

class GPAConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("WIST Education - GPA Converter")
        self.root.geometry("900x750")  # Slightly increased height for the footer
        self.root.configure(bg='#2C5AA0')  # Blue background
        
        # Updated color scheme
        self.colors = {
            'primary': '#2C5AA0',      # Main blue
            'primary_light': '#C8BD4A', # Light blue
            'secondary': '#E6F0FF',    # Very light blue for input fields
            'accent': '#FFD700',       # Yellow for buttons
            'success': '#28A745',      # Green for results
            'warning': '#FFC107',      # Yellow
            'text': '#333333',         # Dark text
            'text_light': '#666666',   # Light text
            'background': '#2C5AA0',   # Blue background
            'card_bg': '#FFFFFF',      # White for cards
            'border': '#DDDDDD'        # Border color
        }
        
        # Create main container to organize layout
        self.main_container = tk.Frame(root, bg=self.colors['background'])
        self.main_container.pack(fill='both', expand=True)
        
        # Create tabs
        self.notebook = ttk.Notebook(self.main_container)
        self.notebook.pack(padx=10, pady=10, fill='both', expand=True)
        
        # Tab 1: Standard Calculation
        self.standard_frame = tk.Frame(self.notebook, bg=self.colors['card_bg'])
        self.notebook.add(self.standard_frame, text="Standard Calculation")
        
        # Tab 2: Precise Calculation with PUM
        self.advanced_frame = tk.Frame(self.notebook, bg=self.colors['card_bg'])
        self.notebook.add(self.advanced_frame, text="Precise Calculation (PUM)")
        
        # Initialize both tabs
        self.setup_standard_tab()
        self.setup_advanced_tab()
        
        # Add creator credit at the bottom
        creator_frame = tk.Frame(self.main_container, bg=self.colors['background'])
        creator_frame.pack(fill='x', pady=10)
        
        name_label = tk.Label(
            creator_frame,
            text="Made by students for students",
            font=('Arial', 11, 'bold'),
            bg=self.colors['background'],
            fg='white'
        )
        name_label.pack()
        
        students_label = tk.Label(
            creator_frame,
            text="Created by:[Me]",
            font=('Arial', 10, 'italic'),
            bg=self.colors['background'],
            fg='white'
        )
        students_label.pack()
        
    def setup_standard_tab(self):
        """Setup standard calculation tab"""
        # Main frame
        main_frame = tk.Frame(self.standard_frame, bg=self.colors['card_bg'])
        main_frame.pack(padx=20, pady=20, fill='both', expand=True)
        
        # Title
        title_label = tk.Label(main_frame, 
                               text="WIST Education - Standard GPA Calculation", 
                               font=('Arial', 16, 'bold'),
                               bg=self.colors['card_bg'],
                               fg=self.colors['primary'])
        title_label.pack(pady=(0, 20))
        
        # Description
        desc_label = tk.Label(main_frame, 
                              text="Enter your A-Level subjects and corresponding grades",
                              font=('Arial', 11),
                              bg=self.colors['card_bg'],
                              fg=self.colors['text'])
        desc_label.pack(pady=(0, 15))
        
        # Input frame with light blue background
        input_container = tk.Frame(main_frame, bg=self.colors['secondary'], 
                                 relief='ridge', bd=2)
        input_container.pack(pady=10, fill='x', padx=5)
        
        input_frame = tk.Frame(input_container, bg=self.colors['secondary'])
        input_frame.pack(padx=15, pady=15, fill='x')
        
        # Input section title
        input_title = tk.Label(input_frame, 
                 text="A-Level Subjects and Grades:", 
                 font=('Arial', 11, 'bold'),
                 bg=self.colors['secondary'],
                 fg=self.colors['text'])
        input_title.grid(row=0, column=0, columnspan=4, pady=8, sticky='w')
        
        # Column headers
        subject_header = tk.Label(input_frame, text="Subject", 
                                 font=('Arial', 10, 'bold'),
                                 bg=self.colors['secondary'],
                                 fg=self.colors['primary'])
        subject_header.grid(row=1, column=0, padx=5, pady=8, sticky='w')
        
        grade_header = tk.Label(input_frame, text="Grade", 
                               font=('Arial', 10, 'bold'),
                               bg=self.colors['secondary'],
                               fg=self.colors['primary'])
        grade_header.grid(row=1, column=1, padx=5, pady=8)
        
        # Dropdown lists for subjects and grades
        self.subjects = []
        self.grades = []
        
        # Predefined A-Level subjects
        self.subject_options = [
            "Mathematics", "Further Mathematics", "Physics", "Chemistry", "Biology",
            "Economics", "Business Studies", "Computer Science", "History", "Geography",
            "English Literature", "Psychology", "Art and Design", "Other", "Media Science",
            "Spanish", "Music", "Physical Education", "Other (custom)"
        ]
        
        self.grade_options = ["A*", "A", "B", "C", "D", "E"]
        
        # Add first input row
        self.add_subject_row_standard(input_frame, 2)
        
        # Control buttons
        button_frame = tk.Frame(input_frame, bg=self.colors['secondary'])
        button_frame.grid(row=10, column=0, columnspan=4, pady=20)
        
        add_btn = tk.Button(button_frame, text="+ Add Subject", 
                          command=lambda: self.add_subject_row_standard(input_frame, len(self.subjects)+2),
                          bg=self.colors['accent'],
                          fg='black',
                          font=('Arial', 10, 'bold'),
                          relief='raised',
                          bd=2,
                          padx=15,
                          pady=8)
        add_btn.pack(side='left', padx=8)
        
        calc_btn = tk.Button(button_frame, text="Calculate All GPA", 
                           command=self.calculate_all_standard,
                           bg=self.colors['accent'],
                           fg='black',
                           font=('Arial', 10, 'bold'),
                          relief='raised',
                          bd=2,
                          padx=15,
                          pady=8)
        calc_btn.pack(side='left', padx=8)
        
        clear_btn = tk.Button(button_frame, text="Clear All", 
                            command=self.clear_all_standard,
                            bg=self.colors['secondary'],
                            fg=self.colors['primary'],
                            font=('Arial', 10),
                            relief='raised',
                            bd=1,
                            padx=15,
                            pady=8)
        clear_btn.pack(side='left', padx=8)
        
        # Results frame
        self.result_frame_standard = tk.Frame(main_frame, bg=self.colors['secondary'],
                                            relief='ridge', bd=2)
        self.result_frame_standard.pack(pady=20, fill='x', padx=5)
        
        # Create result widgets for standard tab
        self.create_result_widgets_standard()
        
    def setup_advanced_tab(self):
        """Setup advanced calculation tab with PUM"""
        main_frame = tk.Frame(self.advanced_frame, bg=self.colors['card_bg'])
        main_frame.pack(padx=20, pady=20, fill='both', expand=True)
        
        # Title
        title_label = tk.Label(main_frame, 
                               text="WIST Education - Precise Calculation with PUM", 
                               font=('Arial', 16, 'bold'),
                               bg=self.colors['card_bg'],
                               fg=self.colors['primary'])
        title_label.pack(pady=(0, 20))
        
        # Description
        desc_text = "Percentage Uniform Mark (PUM) - more precise grading system.\nEnter PUM (0-100) for each subject."
        desc_label = tk.Label(main_frame, 
                              text=desc_text,
                              font=('Arial', 11),
                              bg=self.colors['card_bg'],
                              fg=self.colors['text'],
                              justify='left')
        desc_label.pack(pady=(0, 15))
        
        # Input frame for PUM
        input_container = tk.Frame(main_frame, bg=self.colors['secondary'], 
                                 relief='ridge', bd=2)
        input_container.pack(pady=10, fill='x', padx=5)
        
        input_frame = tk.Frame(input_container, bg=self.colors['secondary'])
        input_frame.pack(padx=15, pady=15, fill='x')
        
        # Title
        input_title = tk.Label(input_frame, 
                 text="Subjects, Grades and PUM:", 
                 font=('Arial', 11, 'bold'),
                 bg=self.colors['secondary'],
                 fg=self.colors['text'])
        input_title.grid(row=0, column=0, columnspan=5, pady=8, sticky='w')
        
        # Column headers
        subject_header = tk.Label(input_frame, text="Subject", 
                                 font=('Arial', 10, 'bold'),
                                 bg=self.colors['secondary'],
                                 fg=self.colors['primary'])
        subject_header.grid(row=1, column=0, padx=5, pady=8, sticky='w')
        
        grade_header = tk.Label(input_frame, text="Grade", 
                               font=('Arial', 10, 'bold'),
                               bg=self.colors['secondary'],
                               fg=self.colors['primary'])
        grade_header.grid(row=1, column=1, padx=5, pady=8)
        
        pum_header = tk.Label(input_frame, text="PUM (%)", 
                             font=('Arial', 10, 'bold'),
                             bg=self.colors['secondary'],
                             fg=self.colors['primary'])
        pum_header.grid(row=1, column=2, padx=5, pady=8)
        
        # Data for advanced tab
        self.advanced_subjects = []
        self.advanced_grades = []
        self.advanced_pums = []
        
        # Add first row
        self.add_subject_row_advanced(input_frame, 2)
        
        # Control buttons
        button_frame = tk.Frame(input_frame, bg=self.colors['secondary'])
        button_frame.grid(row=10, column=0, columnspan=5, pady=20)
        
        add_btn = tk.Button(button_frame, text="+ Add Subject", 
                          command=lambda: self.add_subject_row_advanced(input_frame, len(self.advanced_subjects)+2),
                          bg=self.colors['accent'],
                          fg='black',
                          font=('Arial', 10, 'bold'),
                          relief='raised',
                          bd=2,
                          padx=15,
                          pady=8)
        add_btn.pack(side='left', padx=8)
        
        calc_btn = tk.Button(button_frame, text="Calculate with PUM", 
                           command=self.calculate_all_advanced,
                           bg=self.colors['accent'],
                           fg='black',
                           font=('Arial', 10, 'bold'),
                          relief='raised',
                          bd=2,
                          padx=15,
                          pady=8)
        calc_btn.pack(side='left', padx=8)
        
        clear_btn = tk.Button(button_frame, text="Clear All", 
                            command=self.clear_all_advanced,
                            bg=self.colors['secondary'],
                            fg=self.colors['primary'],
                            font=('Arial', 10),
                            relief='raised',
                            bd=1,
                            padx=15,
                            pady=8)
        clear_btn.pack(side='left', padx=8)
        
        # Results frame
        self.result_frame_advanced = tk.Frame(main_frame, bg=self.colors['secondary'],
                                            relief='ridge', bd=2)
        self.result_frame_advanced.pack(pady=20, fill='x', padx=5)
        
        # Create result widgets for advanced tab
        self.create_result_widgets_advanced()
    
    def add_subject_row_standard(self, parent, row):
        """Add subject row for standard calculation"""
        # Create subject dropdown
        subject_var = tk.StringVar()
        subject_combo = ttk.Combobox(parent, textvariable=subject_var, 
                                   values=self.subject_options, width=22)
        subject_combo.set(self.subject_options[min(row-2, len(self.subject_options)-1)])
        subject_combo.grid(row=row, column=0, padx=8, pady=6)
        subject_combo.configure(background='white')
        
        # Create grade dropdown
        grade_var = tk.StringVar()
        grade_combo = ttk.Combobox(parent, textvariable=grade_var, 
                                 values=self.grade_options, width=8)
        grade_combo.set("A")
        grade_combo.grid(row=row, column=1, padx=8, pady=6)
        grade_combo.configure(background='white')
        
        self.subjects.append(subject_combo)
        self.grades.append(grade_combo)
        
        # Delete button for additional rows
        if row > 2:
            delete_btn = tk.Button(parent, text="×", width=3,
                                 bg=self.colors['secondary'],
                                 fg=self.colors['primary'],
                                 font=('Arial', 10, 'bold'),
                                 relief='flat',
                                 command=lambda r=row-2: self.remove_subject_row_standard(r))
            delete_btn.grid(row=row, column=2, padx=5)
    
    def add_subject_row_advanced(self, parent, row):
        """Add subject row for advanced calculation with PUM"""
        # Create subject dropdown
        subject_var = tk.StringVar()
        subject_combo = ttk.Combobox(parent, textvariable=subject_var, 
                                   values=self.subject_options, width=20)
        subject_combo.set(self.subject_options[min(row-2, len(self.subject_options)-1)])
        subject_combo.grid(row=row, column=0, padx=5, pady=6)
        subject_combo.configure(background='white')
        
        # Create grade dropdown
        grade_var = tk.StringVar()
        grade_combo = ttk.Combobox(parent, textvariable=grade_var, 
                                 values=self.grade_options, width=6)
        grade_combo.set("A")
        grade_combo.grid(row=row, column=1, padx=5, pady=6)
        grade_combo.configure(background='white')
        
        # Create PUM entry field
        pum_var = tk.StringVar()
        pum_entry = tk.Entry(parent, textvariable=pum_var, width=8,
                           bg='white', fg=self.colors['text'],
                           relief='sunken', bd=1)
        pum_entry.insert(0, "90")
        pum_entry.grid(row=row, column=2, padx=5, pady=6)
        
        self.advanced_subjects.append(subject_combo)
        self.advanced_grades.append(grade_combo)
        self.advanced_pums.append(pum_entry)
        
        # Delete button
        if row > 2:
            delete_btn = tk.Button(parent, text="×", width=3,
                                 bg=self.colors['secondary'],
                                 fg=self.colors['primary'],
                                 font=('Arial', 10, 'bold'),
                                 relief='flat',
                                 command=lambda r=row-2: self.remove_subject_row_advanced(r))
            delete_btn.grid(row=row, column=3, padx=5)
    
    def remove_subject_row_standard(self, index):
        """Remove subject row in standard tab"""
        if len(self.subjects) > 1:
            self.subjects[index].destroy()
            self.grades[index].destroy()
            self.subjects.pop(index)
            self.grades.pop(index)
    
    def remove_subject_row_advanced(self, index):
        """Remove subject row in advanced tab"""
        if len(self.advanced_subjects) > 1:
            self.advanced_subjects[index].destroy()
            self.advanced_grades[index].destroy()
            self.advanced_pums[index].destroy()
            self.advanced_subjects.pop(index)
            self.advanced_grades.pop(index)
            self.advanced_pums.pop(index)
    
    def calculate_all_standard(self):
        """Calculate all GPA systems for standard tab"""
        try:
            grades_list = []
            for grade_combo in self.grades:
                grade = grade_combo.get()
                if grade in self.grade_options:
                    grades_list.append(grade)
            
            if not grades_list:
                messagebox.showwarning("Warning", "Please select at least one grade")
                return
            
            american_gpa = self.calculate_american_gpa(grades_list)
            european_gpa = self.calculate_european_gpa(grades_list)
            german_gpa = self.calculate_german_gpa(grades_list)
            ucas_points = self.calculate_ucas_points(grades_list)
            
            self.american_var_standard.set(f"{american_gpa:.2f}")
            self.european_var_standard.set(f"{european_gpa:.2f}")
            self.german_var_standard.set(f"{german_gpa:.2f}")
            self.ucas_var_standard.set(f"{ucas_points}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Calculation error: {str(e)}")
    
    def calculate_all_advanced(self):
        """Calculate GPA using PUM scores"""
        try:
            grades_list = []
            pums_list = []
            
            for i in range(len(self.advanced_grades)):
                grade = self.advanced_grades[i].get()
                pum_text = self.advanced_pums[i].get()
                
                if grade in self.grade_options and pum_text:
                    try:
                        pum = float(pum_text)
                        if 0 <= pum <= 100:
                            grades_list.append(grade)
                            pums_list.append(pum)
                        else:
                            messagebox.showwarning("Error", "PUM must be between 0 and 100")
                            return
                    except ValueError:
                        messagebox.showwarning("Error", "PUM must be a number")
                        return
            
            if not grades_list:
                messagebox.showwarning("Warning", "Please enter at least one subject with PUM score")
                return
            
            # Calculate with PUM
            american_gpa = self.calculate_american_gpa_pum(pums_list)
            european_gpa = self.calculate_european_gpa_pum(pums_list)
            german_gpa = self.calculate_german_gpa_pum(pums_list)
            ucas_points = self.calculate_ucas_points(grades_list)
            
            self.american_var_advanced.set(f"{american_gpa:.2f}")
            self.european_var_advanced.set(f"{european_gpa:.2f}")
            self.german_var_advanced.set(f"{german_gpa:.2f}")
            self.ucas_var_advanced.set(f"{ucas_points}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Calculation error: {str(e)}")
    
    def calculate_american_gpa(self, grades):
        """Calculate American GPA (4.0 scale)"""
        grade_points = {
            "A*": 4.0, "A": 4.0, "B": 3.3, 
            "C": 2.65, "D": 2.0, "E": 1.0
        }
        
        total = sum(grade_points[grade] for grade in grades)
        return total / len(grades)
    
    def calculate_european_gpa(self, grades):
        """Calculate European GPA (100 scale)"""
        grade_points = {
            "A*": 100, "A": 85, "B": 75, 
            "C": 65, "D": 55, "E": 45
        }
        
        total = sum(grade_points[grade] for grade in grades)
        return total / len(grades)
    
    def calculate_german_gpa(self, grades):
        """Calculate German GPA (Bavarian formula)"""
        grade_points = {
            "A*": 1.0, "A": 1.0, "B": 1.5, 
            "C": 2.0, "D": 2.5, "E": 3.0
        }
        
        total = sum(grade_points[grade] for grade in grades)
        german_gpa = total / len(grades)
        return round(german_gpa, 1)
    
    def calculate_ucas_points(self, grades):
        """Calculate UCAS Tariff points"""
        ucas_points_map = {
            "A*": 56, "A": 48, "B": 40, 
            "C": 32, "D": 24, "E": 16
        }
        
        return sum(ucas_points_map[grade] for grade in grades)
    
    # Methods for PUM-based calculation
    def calculate_american_gpa_pum(self, pums):
        """Calculate American GPA based on PUM"""
        total = sum((pum / 100) * 4.0 for pum in pums)
        return total / len(pums)
    
    def calculate_european_gpa_pum(self, pums):
        """Calculate European GPA based on PUM"""
        return sum(pums) / len(pums)
    
    def calculate_german_gpa_pum(self, pums):
        """Calculate German GPA based on PUM using Bavarian formula"""
        # Bavarian formula: 1 + 3*(100 - PUM)/100
        total = sum(1 + 3 * (100 - pum) / 100 for pum in pums)
        german_gpa = total / len(pums)
        return round(german_gpa, 1)
    
    def create_result_widgets_standard(self):
        """Create result display widgets for standard tab"""
        result_inner = tk.Frame(self.result_frame_standard, bg=self.colors['secondary'])
        result_inner.pack(padx=20, pady=20, fill='x')
        
        # Results title
        result_title = tk.Label(result_inner, text="Results:", 
                               font=('Arial', 12, 'bold'),
                               bg=self.colors['secondary'],
                               fg=self.colors['primary'])
        result_title.grid(row=0, column=0, columnspan=2, sticky='w', pady=(0, 15))
        
        # American GPA
        american_label = tk.Label(result_inner, text="American GPA (4.0 scale):", 
                                 font=('Arial', 11, 'bold'),
                                 bg=self.colors['secondary'],
                                 fg=self.colors['text'])
        american_label.grid(row=1, column=0, sticky='w', pady=8)
        
        self.american_var_standard = tk.StringVar(value="0.00")
        american_value = tk.Label(result_inner, textvariable=self.american_var_standard, 
                                 font=('Arial', 11, 'bold'),
                                 bg=self.colors['secondary'],
                                 fg=self.colors['success'])
        american_value.grid(row=1, column=1, padx=20, pady=8)
        
        # European GPA
        european_label = tk.Label(result_inner, text="European GPA (100 scale):", 
                                 font=('Arial', 11, 'bold'),
                                 bg=self.colors['secondary'],
                                 fg=self.colors['text'])
        european_label.grid(row=2, column=0, sticky='w', pady=8)
        
        self.european_var_standard = tk.StringVar(value="0.00")
        european_value = tk.Label(result_inner, textvariable=self.european_var_standard, 
                                 font=('Arial', 11, 'bold'),
                                 bg=self.colors['secondary'],
                                 fg=self.colors['success'])
        european_value.grid(row=2, column=1, padx=20, pady=8)
        
        # German GPA
        german_label = tk.Label(result_inner, text="German GPA (Bavarian Formula):", 
                               font=('Arial', 11, 'bold'),
                               bg=self.colors['secondary'],
                               fg=self.colors['text'])
        german_label.grid(row=3, column=0, sticky='w', pady=8)
        
        self.german_var_standard = tk.StringVar(value="0.00")
        german_value = tk.Label(result_inner, textvariable=self.german_var_standard, 
                               font=('Arial', 11, 'bold'),
                               bg=self.colors['secondary'],
                               fg=self.colors['success'])
        german_value.grid(row=3, column=1, padx=20, pady=8)
        
        # UCAS Points
        ucas_label = tk.Label(result_inner, text="UCAS Tariff Points:", 
                             font=('Arial', 11, 'bold'),
                             bg=self.colors['secondary'],
                             fg=self.colors['text'])
        ucas_label.grid(row=4, column=0, sticky='w', pady=8)
        
        self.ucas_var_standard = tk.StringVar(value="0")
        ucas_value = tk.Label(result_inner, textvariable=self.ucas_var_standard, 
                             font=('Arial', 11, 'bold'),
                             bg=self.colors['secondary'],
                             fg=self.colors['success'])
        ucas_value.grid(row=4, column=1, padx=20, pady=8)
    
    def create_result_widgets_advanced(self):
        """Create result display widgets for advanced tab"""
        result_inner = tk.Frame(self.result_frame_advanced, bg=self.colors['secondary'])
        result_inner.pack(padx=20, pady=20, fill='x')
        
        # Results title
        result_title = tk.Label(result_inner, text="Results (PUM-based):", 
                               font=('Arial', 12, 'bold'),
                               bg=self.colors['secondary'],
                               fg=self.colors['primary'])
        result_title.grid(row=0, column=0, columnspan=2, sticky='w', pady=(0, 15))
        
        # American GPA
        american_label = tk.Label(result_inner, text="American GPA (4.0 scale):", 
                                 font=('Arial', 11, 'bold'),
                                 bg=self.colors['secondary'],
                                 fg=self.colors['text'])
        american_label.grid(row=1, column=0, sticky='w', pady=8)
        
        self.american_var_advanced = tk.StringVar(value="0.00")
        american_value = tk.Label(result_inner, textvariable=self.american_var_advanced, 
                                 font=('Arial', 11, 'bold'),
                                 bg=self.colors['secondary'],
                                 fg=self.colors['success'])
        american_value.grid(row=1, column=1, padx=20, pady=8)
        
        # European GPA
        european_label = tk.Label(result_inner, text="European GPA (100 scale):", 
                                 font=('Arial', 11, 'bold'),
                                 bg=self.colors['secondary'],
                                 fg=self.colors['text'])
        european_label.grid(row=2, column=0, sticky='w', pady=8)
        
        self.european_var_advanced = tk.StringVar(value="0.00")
        european_value = tk.Label(result_inner, textvariable=self.european_var_advanced, 
                                 font=('Arial', 11, 'bold'),
                                 bg=self.colors['secondary'],
                                 fg=self.colors['success'])
        european_value.grid(row=2, column=1, padx=20, pady=8)
        
        # German GPA
        german_label = tk.Label(result_inner, text="German GPA (Bavarian Formula):", 
                               font=('Arial', 11, 'bold'),
                               bg=self.colors['secondary'],
                               fg=self.colors['text'])
        german_label.grid(row=3, column=0, sticky='w', pady=8)
        
        self.german_var_advanced = tk.StringVar(value="0.00")
        german_value = tk.Label(result_inner, textvariable=self.german_var_advanced, 
                               font=('Arial', 11, 'bold'),
                               bg=self.colors['secondary'],
                               fg=self.colors['success'])
        german_value.grid(row=3, column=1, padx=20, pady=8)
        
        # UCAS Points
        ucas_label = tk.Label(result_inner, text="UCAS Tariff Points:", 
                             font=('Arial', 11, 'bold'),
                             bg=self.colors['secondary'],
                             fg=self.colors['text'])
        ucas_label.grid(row=4, column=0, sticky='w', pady=8)
        
        self.ucas_var_advanced = tk.StringVar(value="0")
        ucas_value = tk.Label(result_inner, textvariable=self.ucas_var_advanced, 
                             font=('Arial', 11, 'bold'),
                             bg=self.colors['secondary'],
                             fg=self.colors['success'])
        ucas_value.grid(row=4, column=1, padx=20, pady=8)
    
    def clear_all_standard(self):
        """Clear all fields in standard tab"""
        for i in range(len(self.subjects)):
            if i == 0:
                self.subjects[i].set(self.subject_options[0])
                self.grades[i].set("A")
            else:
                self.subjects[i].destroy()
                self.grades[i].destroy()
        
        self.subjects = self.subjects[:1]
        self.grades = self.grades[:1]
        
        self.american_var_standard.set("0.00")
        self.european_var_standard.set("0.00")
        self.german_var_standard.set("0.00")
        self.ucas_var_standard.set("0")
    
    def clear_all_advanced(self):
        """Clear all fields in advanced tab"""
        for i in range(len(self.advanced_subjects)):
            if i == 0:
                self.advanced_subjects[i].set(self.subject_options[0])
                self.advanced_grades[i].set("A")
                self.advanced_pums[i].delete(0, tk.END)
                self.advanced_pums[i].insert(0, "90")
            else:
                self.advanced_subjects[i].destroy()
                self.advanced_grades[i].destroy()
                self.advanced_pums[i].destroy()
        
        self.advanced_subjects = self.advanced_subjects[:1]
        self.advanced_grades = self.advanced_grades[:1]
        self.advanced_pums = self.advanced_pums[:1]
        
        self.american_var_advanced.set("0.00")
        self.european_var_advanced.set("0.00")
        self.german_var_advanced.set("0.00")
        self.ucas_var_advanced.set("0")

def main():
    root = tk.Tk()
    app = GPAConverter(root)
    root.mainloop()

if __name__ == "__main__":

    main()
