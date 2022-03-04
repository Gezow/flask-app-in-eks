# DevOps - PingPong

### LOCAL IMAGE RUN:

##### Docker:

    docker image build -t devops-pingpong .
    
    docker run -p 8080:8080 -d devops-pingpong

##### Docker Compose:

    docker-compose up

### BUILD EKS CLUSTER:

    eksctl create cluster -f eksctl-cluster.yaml

#### ADD IMAGE TO AWS ECR

    aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com
    
    aws ecr create-repository --repository-name <hello-world> --image-scanning-configuration scanOnPush=true --region <region>
    
    docker image build -t devops-pingpong .
    
    docker tag <docker-image-id> <aws_account_id>.dkr.ecr.<region>.amazonaws.com/<my-repository:tag>
    
    docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/<my-repository:tag>


#### INSTALL APP TO CLUSTER

    kubectl create namespace pingpong-namespace
    
    kubectl create -f pingpong-deployment.yaml 
    
    kubectl create -f pingpong-webapp-service.yaml 