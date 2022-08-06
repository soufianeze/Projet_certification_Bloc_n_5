import mlflow.sagemaker as mfs
experiment_id = '1'
run_id = '7b9e401c818a46fd878c709fc0915fbe'
region = 'us-east-1'
aws_id = '271704954066'
arn = 'arn:aws:iam::271704954066:role/awssagemakerfordeploy'
app_name = 'model-application'
run_id = "7b9e401c818a46fd878c709fc0915fbe"
model_uri = "runs:/" + run_id + "/randomf"
tag_id = '1.18.0'
image_url = aws_id + '.dkr.ecr.' + region + '.amazonaws.com/mlflow-pyfunc:' + tag_id

mfs.deploy(app_name=app_name, 
           model_uri=model_uri, 
           region_name=region, 
           mode="create",
           execution_role_arn=arn,
           image_url=image_url)