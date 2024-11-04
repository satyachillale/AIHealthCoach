from django.contrib.auth.models import (
    User,
)  # Assumes you're using Django's default User model
from django.db import models


class Query(models.Model):
    query_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who made the query
    query = models.TextField()  # Stores the query text
    timestamp = models.DateTimeField(
        auto_now_add=True
    )  # Automatically sets the current timestamp

    def __str__(self):
        return f"Query {self.query_id} by User {self.user_id}"


class Agent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)


class Edge(models.Model):
    id = models.AutoField(primary_key=True)
    start = models.ForeignKey(
        Agent, on_delete=models.CASCADE, related_name="from_agent"
    )
    end = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name="to_agent")


class Graph(models.Model):
    id = models.AutoField(primary_key=True)
    nodes = models.ManyToManyField(Agent)
    edges = models.ManyToManyField(Edge)


class Workflow(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE)  # Related Query
    node_id = models.IntegerField()  # Node ID
    token_usage = models.IntegerField()  # Token usage for this node
    timestamp = models.DateTimeField(
        auto_now_add=True
    )  # Automatically sets the current timestamp
    graph = models.ForeignKey(Graph, on_delete=models.CASCADE)

    def __str__(self):
        return f"Workflow for Query {self.query.query_id} - Node {self.node_id}"
