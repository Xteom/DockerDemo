
# A continuación deberia de seguir el deploy de docker
# Set variables
img_name=pandas_header
aws_region=us-west-2
aws_account_id=401913772240

#Update and build docker image
docker build -t $img_name .
docker tag $img_name $aws_account_id.dkr.ecr.$aws_region.amazonaws.com/$img_name
aws ecr get-login-password --region $aws_region | docker login --username AWS --password-stdin $aws_account_id.dkr.ecr.$aws_region.amazonaws.com

# We push our image
docker push $aws_account_id.dkr.ecr.$aws_region.amazonaws.com/$img_name

