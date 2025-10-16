class User:
    def __init__(self, user_name: str, email: str):
        self.user_name = user_name
        self.email = email
    def show_info(self):
        print(f"User : {self.user_name}\nEmail : {self.email}")
    def login(self):
        print(f"{self.user_name} has logged in")

class AdminUser(User):
    def __init__(self, user_name, email, privilegs):
        super().__init__(user_name, email)
        self.privilegs = privilegs
    def ban_user(self, user):
        print(f"Admin {self.user_name} has banned user {user}.")
    
    def show_privilegs(self):
        print(self.privilegs)

class  NormalUser(User):
    def __init__(self,user_name, email, comments):
        super().__init__(user_name, email)
        self.comments = comments

    def post_comment(self):
        
        txt = input("please leave a comment: ")
        self.comments.append(txt)
        print(f"{self.user_name} posted a new comment :\n{txt}")
    def show_comments(self):
        print(self.comments)

user = User("John", "smartjo12@gmail.com") 
admin_User = AdminUser("Noa", "notanother2@gmail.com", [5, 4, 8, 2])  
normal_user = NormalUser("Johanson", "smjijio12@gmail.com", ["very good", "good job", "yes"])  
user.show_info()
user.login()
admin_User.ban_user("Peter")
admin_User.show_privilegs()
normal_user.post_comment()
normal_user.show_comments()