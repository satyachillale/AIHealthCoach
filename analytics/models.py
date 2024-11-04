from django.db import models
from django.contrib.auth.models import User  # Assumes you're using Django's default User model

class Query(models.Model):
    query_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who made the query
    query = models.TextField()  # Stores the query text
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically sets the current timestamp

    def __str__(self):
        return f"Query {self.query_id} by User {self.user_id}"

class Workflow(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE)  # Related Query
    node_id = models.IntegerField()  # Node ID
    token_usage = models.IntegerField()  # Token usage for this node
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically sets the current timestamp

    def __str__(self):
        return f"Workflow for Query {self.query.query_id} - Node {self.node_id}"
