class User:
    def __init__(self, name, email, password, job_title):
        self.user_name = name
        self.user_email = email
        self.user_pass = password
        self.user_job = job_title

    def change_password(self, new_pass):
        self.user_pass = new_pass

    def change_job_title(self, new_title):
        self.user_job = new_title

    def get_user_info(self):
        print(f"User {self.user_name} currently work as a {self.user_job}. You can contact at {self.user_email}")
