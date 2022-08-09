from user import User
from post import Post

app_user_one = User("Arif", "mdah@gmail.com", "pwd1", "software engineer")
app_user_one.get_user_info()
# app_user_one.change_job_title("DevOps")
# app_user_one.get_user_info()

app_user_two = User("Totul", "totul@gmail.com", "tot2", "DevOps trainer")
app_user_two.get_user_info()


createPost = Post("Arif", "Python BLog", "Python is a very popular language")
createPost.get_post_info()