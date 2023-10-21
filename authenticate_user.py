import terry

USERNAME = "test_user"
auth_url = terry.generate_widget_url(USERNAME)
print(auth_url)