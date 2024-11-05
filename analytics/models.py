from django.db import models
from agents.models import UserData

class Query(models.Model):
    queryId = models.OneToOneField(UserData, on_delete=models.CASCADE, primary_key=True)
    query = models.TextField()  # Stores the query text
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically sets the current timestamp


# class Workflow(models.Model):
#     query = models.ForeignKey(Query, on_delete=models.CASCADE)  # Related Query
#     node_id = models.IntegerField()  # Node ID
#     token_usage = models.IntegerField()  # Token usage for this node
#     timestamp = models.DateTimeField(auto_now_add=True)  # Automatically sets the current timestamp

#     def __str__(self):
#         return f"Workflow for Query {self.query.query_id} - Node {self.node_id}"
