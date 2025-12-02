"""
Unit tests for Knowledge Base
Tests course and staff retrieval, search functionality
"""

import unittest
from knowledge_base import KnowledgeBase

class TestKnowledgeBase(unittest.TestCase):
    
    def setUp(self):
        """Initialize knowledge base for each test"""
        self.kb = KnowledgeBase()
    
    def test_get_course_python(self):
        """Test retrieving Python course"""
        course = self.kb.get_course('python')
        self.assertIsNotNone(course)
        self.assertEqual(course['title'], 'Python Programming')
        self.assertEqual(course['instructor'], 'Dr. John Smith')
    
    def test_get_course_not_found(self):
        """Test retrieving non-existent course"""
        course = self.kb.get_course('nonexistent')
        self.assertIsNone(course)
    
    def test_get_all_courses(self):
        """Test retrieving all courses"""
        courses = self.kb.get_all_courses()
        self.assertEqual(len(courses), 4)
        self.assertIn('python', courses)
        self.assertIn('javascript', courses)
        self.assertIn('data_science', courses)
        self.assertIn('web_design', courses)
    
    def test_get_staff(self):
        """Test retrieving staff information"""
        staff = self.kb.get_staff('john_smith')
        self.assertIsNotNone(staff)
        self.assertEqual(staff['name'], 'Dr. John Smith')
        self.assertEqual(staff['position'], 'Senior Instructor')
    
    def test_get_staff_not_found(self):
        """Test retrieving non-existent staff"""
        staff = self.kb.get_staff('unknown')
        self.assertIsNone(staff)
    
    def test_get_all_staff(self):
        """Test retrieving all staff"""
        staff = self.kb.get_all_staff()
        self.assertEqual(len(staff), 3)
        self.assertIn('john_smith', staff)
        self.assertIn('sarah_johnson', staff)
        self.assertIn('emily_chen', staff)
    
    def test_search_courses_by_level(self):
        """Test searching courses by difficulty level"""
        beginner_courses = self.kb.search_courses_by_level('Beginner')
        self.assertEqual(len(beginner_courses), 2)  # Python and Web Design
        
        advanced_courses = self.kb.search_courses_by_level('Advanced')
        self.assertEqual(len(advanced_courses), 1)  # Data Science
    
    def test_search_courses_by_instructor(self):
        """Test searching courses by instructor"""
        courses = self.kb.search_courses_by_instructor('John Smith')
        self.assertGreater(len(courses), 0)
        for course in courses.values():
            self.assertIn('John Smith', course['instructor'])
    
    def test_course_attributes(self):
        """Test that courses have all required attributes"""
        course = self.kb.get_course('python')
        required_attrs = ['title', 'duration', 'level', 'instructor', 'description', 'schedule']
        for attr in required_attrs:
            self.assertIn(attr, course)
    
    def test_staff_attributes(self):
        """Test that staff have all required attributes"""
        staff = self.kb.get_staff('john_smith')
        required_attrs = ['name', 'position', 'department', 'email', 'office', 'office_hours']
        for attr in required_attrs:
            self.assertIn(attr, staff)
    
    def test_case_insensitive_search(self):
        """Test that searches are case-insensitive"""
        course_lower = self.kb.get_course('python')
        course_upper = self.kb.get_course('PYTHON')
        course_mixed = self.kb.get_course('PyThOn')
        
        self.assertEqual(course_lower, course_upper)
        self.assertEqual(course_lower, course_mixed)

if __name__ == '__main__':
    unittest.main()
