from locust import HttpLocust, Locust, TaskSet, task, between
from assertpy import assert_that

class SimpleHTTPMethods(TaskSet):  #TaskSet: Class defining a set of tasks that a Locust user will execute.
    @task
    def simpleGet(self):
        response = self.client.get("/posts")
        assert_that(response.status_code).is_between(200,299)

    @task
    def simplePost(self):
        response = self.client.post("/posts", {"username":"testuser", "password":"secret"})
        assert_that(response.status_code).is_between(200,299)
 

    @task
    def simplePut(self):
        response = self.client.put("/posts/1", {"username":"testuser", "password":"secret"})
        assert_that(response.status_code).is_between(200,299)

    @task
    def simpleDelete(self):
        response = self.client.delete("/posts/1")
        assert_that(response.status_code).is_between(200,299)




class User(HttpLocust):
    task_set = SimpleHTTPMethods
    wait_time = between(5, 15)
