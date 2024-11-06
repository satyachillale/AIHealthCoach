from django.contrib.auth.models import (
    User,
)  # Assumes you're using Django's default User model
from django.db import models

from agents.models import UserData


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
    hash = models.CharField(max_length=64, unique=True)


class Query(models.Model):
    id = models.AutoField(primary_key=True)
    # userdata = models.OneToOneField(UserData, on_delete=models.CASCADE)
    query_text = models.TextField()  # Stores the query text
    timestamp = models.DateTimeField(
        auto_now_add=True
    )  # Automatically sets the current timestamp
    graph = models.ForeignKey(Graph, on_delete=models.CASCADE, null=True)


class AgentQuery(models.Model):
    queryId = models.ForeignKey(
        Query, on_delete=models.CASCADE, primary_key=False
    )  # Related Query
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)  # Node ID
    token_usage = models.IntegerField()  # Token usage for this node
    startTimestamp = models.DateTimeField()
    endTimestamp = models.DateTimeField()

    def __str__(self):
        return f"Workflow for Query {self.query.query_id} - Node {self.node_id}"
