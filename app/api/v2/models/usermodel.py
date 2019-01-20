# """User class"""


# from manage import connection


# class User:
#     """User class defining methods related to the class"""

#     def __init__(self, email, username, password, role='attendant'):

#         self.email = email
#         self.username = username
#         self.password = password
#         self.role = role

#     def save_user(self):
#         """ save a new user """
#         with connection() as conn:
#             with conn.cursor() as cursor:
#                 cursor.execute("INSERT INTO users (email,username,\
#                                                    password,role,\
#                                                    registered_on)\
#                                 VALUES(%s,%s,%s,%s,%s) \
#                                 RETURNING username", (self.email,
#                                                       self.username,
#                                                       self.password,
#                                                       self.role,
#                                                       self.registered_on))
#                 user = cursor.fetchone()
#                 return dict(username=user)
