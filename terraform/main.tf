
resource "aws_ecs_cluster" "main" {
  name = "main-cluster"
}

resource "aws_ecs_service" "fargate_service" {
  name            = "fargate_service"
  cluster         = aws_ecs_cluster.main.id
  launch_type     = "FARGATE"
  desired_count   = 2
  task_definition = aws_ecs_task_definition.main.arn
}
            

resource "aws_lambda_function" "health_plan_function" {
  function_name = "health_plan_function"
  role          = aws_iam_role.lambda_role.arn
  handler       = "index.handler"
  runtime       = "python3.8"
  source_code_hash = filebase64sha256("lambda_function.zip")
}
            

resource "aws_db_instance" "default" {
  allocated_storage    = 20
  storage_type         = "gp2"
  engine               = "postgres"
  engine_version       = "13.3"
  instance_class       = "db.t3.micro"
  name                 = "mydb"
  username             = "master"
  password             = "password"
  skip_final_snapshot  = true
}
            

resource "aws_s3_bucket" "uploads" {
  bucket = "myapp-uploads"
  acl    = "private"
}
            