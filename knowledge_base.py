"""
Knowledge Base Module for QA Chatbot
Contains domain-specific information for courses and staff
"""

class KnowledgeBase:
    """
    Manages the knowledge base with course and staff information
    """
    
    def __init__(self):
        self.courses = {
            "python": {
                "title": "Python Programming",
                "duration": "8 weeks",
                "level": "Beginner",
                "instructor": "Dr. John Smith",
                "description": "Learn Python fundamentals including variables, loops, functions, and OOP",
                "schedule": "Monday and Wednesday, 2:00 PM - 3:30 PM"
            },
            "javascript": {
                "title": "JavaScript Web Development",
                "duration": "10 weeks",
                "level": "Intermediate",
                "instructor": "Prof. Sarah Johnson",
                "description": "Master JavaScript for frontend and backend web development",
                "schedule": "Tuesday and Thursday, 3:00 PM - 4:30 PM"
            },
            "data_science": {
                "title": "Data Science and Machine Learning",
                "duration": "12 weeks",
                "level": "Advanced",
                "instructor": "Dr. Emily Chen",
                "description": "Comprehensive course on data analysis, visualization, and ML algorithms",
                "schedule": "Saturday, 10:00 AM - 12:00 PM"
            },
            "web_design": {
                "title": "Web Design Fundamentals",
                "duration": "6 weeks",
                "level": "Beginner",
                "instructor": "Alex Martinez",
                "description": "Learn HTML, CSS, and responsive design principles",
                "schedule": "Friday, 4:00 PM - 5:30 PM"
            }
        }
        
        self.staff = {
            "john_smith": {
                "name": "Dr. John Smith",
                "position": "Senior Instructor",
                "department": "Computer Science",
                "email": "john.smith@academy.edu",
                "office": "Building A, Room 205",
                "office_hours": "Monday and Wednesday, 4:00 PM - 5:00 PM"
            },
            "sarah_johnson": {
                "name": "Prof. Sarah Johnson",
                "position": "Instructor",
                "department": "Web Technologies",
                "email": "sarah.johnson@academy.edu",
                "office": "Building B, Room 101",
                "office_hours": "Tuesday and Thursday, 5:00 PM - 6:00 PM"
            },
            "emily_chen": {
                "name": "Dr. Emily Chen",
                "position": "Lead Instructor",
                "department": "Data Science",
                "email": "emily.chen@academy.edu",
                "office": "Building C, Room 310",
                "office_hours": "Saturday, 1:00 PM - 2:00 PM"
            }
        }
        
        self.faq = {
            "enrollment": "How do I enroll in a course?",
            "enrollment_ans": "Visit the registration portal on our website and fill out the enrollment form.",
            "prerequisite": "Are there prerequisites for courses?",
            "prerequisite_ans": "Beginner courses have no prerequisites. Intermediate and Advanced courses require prior knowledge.",
            "certificate": "Do I get a certificate after completion?",
            "certificate_ans": "Yes, you receive a certificate of completion after successfully finishing the course.",
            "refund": "What is the refund policy?",
            "refund_ans": "We offer a 7-day refund policy from the enrollment date."
        }
    
    def get_course(self, course_name):
        """
        Retrieve course information by name
        """
        return self.courses.get(course_name.lower())
    
    def get_all_courses(self):
        """
        Get all available courses
        """
        return self.courses
    
    def get_staff(self, staff_name):
        """
        Retrieve staff information by name
        """
        return self.staff.get(staff_name.lower())
    
    def get_all_staff(self):
        """
        Get all staff information
        """
        return self.staff
    
    def search_courses_by_level(self, level):
        """
        Search courses by difficulty level
        """
        return {name: course for name, course in self.courses.items() 
                if course["level"].lower() == level.lower()}
    
    def search_courses_by_instructor(self, instructor_name):
        """
        Search courses taught by a specific instructor
        """
        return {name: course for name, course in self.courses.items() 
                if instructor_name.lower() in course["instructor"].lower()}
