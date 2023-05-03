FROM public.ecr.aws/lambda/python:3.8 AS ECR

# Copy function code and models into our /var/task
# Optimal Attempt
COPY requirements.txt ${LAMBDA_TASK_ROOT}/ 

# Use gcc and install dependencies
# Install other non python dependencies
# RUN rm -rf /var/cache/yum & yum install -y cmake python37-devel gcc gcc-c++ make mesa-libGL ffmpeg python3-opencv ffmpeg-devel

RUN python3 -m pip install -r requirements.txt --target ${LAMBDA_TASK_ROOT}

COPY ./ ${LAMBDA_TASK_ROOT}/

RUN yum clean all & rm -rf /var/cache/yum