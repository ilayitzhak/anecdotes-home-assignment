# anecdotes-home assignment
 
Anecdotes develop and maintain hundreds of plugins, but in this exercise you will develop a
simple plugin that might exist on our platform. You will collect 3 pieces of evidence from
dummyjson, which simulates a REST API service.

Your plugin should:
1. Implement a connectivity test - Every evidence collection starts with a connectivity test.
In this case we’ll just use it to authenticate with your selected user by calling the login
endpoint. If you want to make sure that your connectivity test works well, you can
provide valid and non-valid credentials.
2. Evidence collection:
    - E1 - Collect the authenticated user details (the user you picked to use).
    - E2 - Collect a list of 60 posts in the system.
    - E3 - Collect a list of 60 posts, including each post’s comments.

#Prerequisites
1. Learn the https://dummyjson.com/docs APIs.
2. Pick a user to use from https://dummyjson.com/users and use its username and
password.

#Outcome
Create a new Github repository where you will implement your plugin code. The code’s entry
point should be the file main.py and it should be invoked by calling python main.py.

#Further considerations
- Consider how the structure of the code can be used with other APIs?
- The code should be as generic as possible as we might want to add new evidence to
this plugin or write new plugins in the future.
- Think about error handling as the API might return different other status codes than 200
OK.
