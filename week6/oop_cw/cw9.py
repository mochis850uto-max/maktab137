class User:
    def __init__(self, user_name: str, email: str, privilegs: list, comments: list):
        self.user_name = user_name
        self.email = email
        self.privilegs = privilegs
        self.comments = comments
    
    def show_info(self):
        print(f"User : {self.user_name}\nEmail : {self.email}")
    def login(self):
        print(f"{self.user_name} has logged in")

class AdminUser(User):
    def __init__(self, user_name, email, privilegs, comments):
        super().__init__(user_name , email, privilegs, comments)
        self.privilegs = privilegs
    def ban_user(self, user):
        print(f"Admin {self.user_name} has banned user {user}.")
    
    def show_privilegs(self):
        print(self.privilegs)

class  NormalUser(User):
    def __init__(self,user_name, email, privilegs, comments):
        super().__init__(user_name, email, privilegs, comments)
        self.comments = comments

    def post_comment(self):
        # for txt in self.comments:
        txt = input("please leave a comment: ")
        self.comments.append(txt)
        print(f"{self.user_name} posted a new comment :\n{txt}")
    def show_comments(self):
        print(self.comments)

user = User("john", "smartjo12@gmail.com", [5, 3, 10, 2], ["well done", "good job man", "yes you got it"])
admin_User = AdminUser("noa", "notanother2@gmail.com", [5, 4, 8, 2], ["good", "nice"])
normal_user = NormalUser("johanson", "smjijio12@gmail.com", [2,5], ["very good", "good job", "yes"])
user.show_info()
user.login()
admin_User.ban_user("johnii")
admin_User.show_privilegs()
normal_user.post_comment()
normal_user.show_comments()