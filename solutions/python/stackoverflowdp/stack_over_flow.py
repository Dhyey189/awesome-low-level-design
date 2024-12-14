from threading import Lock
from typing import List
from user import User
from question import Question
from postable_entity import PostableEntity


class StackOverFlow:
	__lock = Lock()
	
	def __new__(cls):
		with cls.__lock:
			if cls.__instance in None:
				cls.__instance = super().__new__(cls)
				cls.__instance.users = []
				cls.__instance.questions = []

	@classmethod
	def get_instance(cls):
		return cls()

	def create_user(self):
		pass

	def post_question(self, auther: User, content: str):
		pass

	def post_answer(self, auther: User, question: Question, content: str):
		pass

	# def post_comment(self, auther: User, postable_entity: PostableEntity, content: str):
	# 	pass


