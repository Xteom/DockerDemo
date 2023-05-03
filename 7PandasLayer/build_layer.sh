IMAGE=pandas_layer

docker build -t $IMAGE .
CONTAINER=$(docker run -d $IMAGE false)
docker cp $CONTAINER:/opt layer
docker rm $CONTAINER

touch layer/.slsignore
cat > layer/.slsignore << EOF 
**/*.a
**/*.la
share/**
include/**
bin/**
EOF

cp *.py layer/python/.
cp google_credentials_n.json layer/python/.
