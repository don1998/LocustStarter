from locust import HttpLocust, Locust, TaskSet, task, between
from assertpy import assert_that

class SimpleHTTPMethods(TaskSet):  #TaskSet: Class defining a set of tasks that a Locust user will execute.
    @task
    def simpleGet(self):
        response = self.client.get("/")
        assert_that(response.status_code).is_equal_to(200)
        print("Response: ", response)
        
    @task
    def simplePost(self):
        response = self.client.post("/posts", {"username":"testuser", "password":"secret"})
        assert_that(response.status_code).is_equal_to(200)
        print("Response: ", response)

    @task
    def simplePut(self):
        response = self.client.post("/posts", {"username":"testuser", "password":"secret"})
        assert_that(response.status_code).is_equal_to(200)
        print("Response: ", response)



class User(HttpLocust):
    task_set = SimpleHTTPMethods
    wait_time = between(5, 15)
