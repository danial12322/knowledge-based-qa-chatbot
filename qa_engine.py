"""
QA Engine Module
Implements rule-based question answering with natural language processing
"""

import re
from typing import Dict, List, Tuple, Optional
from knowledge_base import KnowledgeBase

class QAEngine:
    """
    Question Answering Engine with rule-based responses
    """
    
    def __init__(self, knowledge_base: KnowledgeBase):
        self.kb = knowledge_base
        self.response_templates = {
            "course_info": "The {course} course is taught by {instructor} and runs for {duration}. {description}",
            "course_schedule": "The {course} course is scheduled for {schedule}.",
            "staff_info": "{name} is a {position} in the {department} department. Email: {email}. Office: {office}.",
            "staff_hours": "{name} has office hours at {office_hours}.",
            "not_found": "I don't have information about that. Please try asking about courses or staff."
        }
    
    def extract_keywords(self, query: str) -> List[str]:
        """
        Extract keywords from user query
        """
        # Convert to lowercase and split
        words = query.lower().split()
        # Remove common stop words
        stop_words = {'what', 'is', 'the', 'a', 'an', 'about', 'tell', 'me', 'who', 'when', 'where', 'how'}
        return [w for w in words if w not in stop_words and len(w) > 2]
    
    def identify_intent(self, query: str) -> str:
        """
        Identify the intent of the user query
        """
        query_lower = query.lower()
        
        if re.search(r'course|class|learn|study|take', query_lower):
            return 'course_query'
        elif re.search(r'staff|instructor|professor|teacher|contact', query_lower):
            return 'staff_query'
        elif re.search(r'schedule|time|when|day', query_lower):
            return 'schedule_query'
        elif re.search(r'office hour|meeting|availability', query_lower):
            return 'office_hours_query'
        elif re.search(r'enroll|enlist|register|prerequisite|level|beginner|advanced', query_lower):
            return 'faq_query'
        else:
            return 'general_query'
    
    def find_course_match(self, keywords: List[str]) -> Optional[str]:
        """
        Find matching course based on keywords
        """
        courses = self.kb.get_all_courses()
        for keyword in keywords:
            for course_name, course_info in courses.items():
                if keyword in course_name or keyword in course_info['title'].lower():
                    return course_name
        return None
    
    def find_staff_match(self, keywords: List[str]) -> Optional[str]:
        """
        Find matching staff member based on keywords
        """
        staff = self.kb.get_all_staff()
        for keyword in keywords:
            for staff_id, staff_info in staff.items():
                if keyword in staff_id or keyword in staff_info['name'].lower():
                    return staff_id
        return None
    
    def answer_course_query(self, course_name: str) -> str:
        """
        Generate answer for course-related queries
        """
        course = self.kb.get_course(course_name)
        if not course:
            return self.response_templates['not_found']
        
        return self.response_templates['course_info'].format(
            course=course['title'],
            instructor=course['instructor'],
            duration=course['duration'],
            description=course['description']
        )
    
    def answer_staff_query(self, staff_id: str) -> str:
        """
        Generate answer for staff-related queries
        """
        staff = self.kb.get_staff(staff_id)
        if not staff:
            return self.response_templates['not_found']
        
        return self.response_templates['staff_info'].format(
            name=staff['name'],
            position=staff['position'],
            department=staff['department'],
            email=staff['email'],
            office=staff['office']
        )
    
    def process_query(self, query: str) -> str:
        """
        Main method to process user query and generate response
        """
        if not query or len(query.strip()) == 0:
            return "Please ask me a question about courses or staff."
        
        intent = self.identify_intent(query)
        keywords = self.extract_keywords(query)
        
        if intent == 'course_query':
            course_match = self.find_course_match(keywords)
            if course_match:
                return self.answer_course_query(course_match)
        
        elif intent == 'staff_query':
            staff_match = self.find_staff_match(keywords)
            if staff_match:
                return self.answer_staff_query(staff_match)
        
        elif intent == 'schedule_query':
            course_match = self.find_course_match(keywords)
            if course_match:
                course = self.kb.get_course(course_match)
                return self.response_templates['course_schedule'].format(
                    course=course['title'],
                    schedule=course['schedule']
                )
        
        elif intent == 'office_hours_query':
            staff_match = self.find_staff_match(keywords)
            if staff_match:
                staff = self.kb.get_staff(staff_match)
                return self.response_templates['staff_hours'].format(
                    name=staff['name'],
                    office_hours=staff['office_hours']
                )
        
        return self.response_templates['not_found']
