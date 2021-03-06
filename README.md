<br />
<p align="center">
  <a href="#list-of-labs">
    <img src="/images/aws-labs-logo.png" alt="Logo" width="664" height="377">
  </a>

  <h3 align="center">100 days in Cloud</h3>

  <p align="center">
    One lab a day with AWS cloud services. 
    <br />
    <br />
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#AWS-learning-options">AWS learning options</a></li>
        <li><a href="#recommended-prerequisites">Recommended prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#list-of-labs">List of labs</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<img src="/images/AmazonWebservices_Logo.png" alt="Logo" width="200" height="100">
Idea is to cover as many AWS architectures and services as possible in different labs, some in Management Console, some through AWS CLI. AWS features over 200 services so there’s lots to lab on. Great deal of labs is me working on my website, other comes from labs providers.

### Built With

* [AWS CLI](https://aws.amazon.com/cli/)
* [Python](https://aws.amazon.com/developer/language/python/)
* [AWS CloudFormation Templates](https://aws.amazon.com/cloudformation/resources/templates/)
* [AWS SAM](https://aws.amazon.com/serverless/sam/)
* [Terraform](https://www.terraform.io/)



<!-- GETTING STARTED -->
## Getting Started

To get started with AWS you'll either create a new [Free Tier](https://aws.amazon.com/free/) account or start
one of the paid services that offer labs and sandboxes. You’ll find some examples in <a href="#AWS learning options">Paid AWS learning options</a> section.
The advantage of the paid services is that you’ll get the labs with clear instructions, in some cases guidance and a sandbox, that is provided AWS account where you can deploy services without worrying about additional costs.


### Paid AWS learning options

Here’s a list of services used as a source of labs:
* [A Cloud Guru](https://acloudguru.com/browse-training?type=lab) - paid with some free options
* [WhizLabs](https://play.whizlabs.com/) - paid with some free options
* [Udemy course Ultimate AWS Certified Developer Associate 2021](https://www.udemy.com/course/aws-certified-developer-associate-dva-c01/?src=sac&kw=Ultimate+AWS+Certified+Developer+Associate+2021) - paid

And some free ones:
* [AWS Hands-On repository](https://aws.amazon.com/getting-started/hands-on/) - free
* ['Be a better dev' YouTube channel](https://www.youtube.com/c/BeABetterDev) - free
* [Cloud Academy](https://cloudacademy.com/library/)

### Recommended prerequisites

1. Install [Visual Studio Code](https://code.visualstudio.com/download) for writing JSON,YAML files or Lambda functions
2. Install AWS Command Line Interface [from here](https://awscli.amazonaws.com/AWSCLIV2.msi) for command line labs
   * verify the installation by running this command in Command Prompt or Terminal:
    ```sh
   aws --version
   ```
   * configure you're AWS CLI with your credentials, here's more [info](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
    ```sh
   aws configure
   ```

## List of labs

List of Labs in the repository (will be growing as time passes towards the end of 2021) in countdown order:
* [Day 100 - Using EC2 Roles and Instance Profiles in AWS](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/100%20-%20Using%20EC2%20Roles%20and%20Instance%20Profiles%20in%20AWS)
* [Day 99 - Deploy an Amazon RDS Multi-AZ and Read Replica in AWS](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/99%20-%20Deploy%20an%20Amazon%20RDS%20Multi-AZ%20and%20Read%20Replica%20in%20AWS)
* [Day 98 - AWS IoT - ESP32-CAM and Rekognition](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/98%20-%20AWS%20IoT%20-%20ESP32-CAM%20and%20Rekognition)
* [Day 97 - Build a real time data streaming system with Amazon Kinesis Data Streams](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/97%20-%20Build%20a%20real%20time%20data%20streaming%20system%20with%20Amazon%20Kinesis%20Data%20Streams)
* [Day 96 - Running Lambda on a Schedule](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/96%20-%20Running%20Lambda%20on%20a%20Schedule)
* [Day 95 - CloudWatch event for RDS backup to DynamoDB](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/95%20-%20CloudWatch%20event%20for%20RDS%20backup%20to%20DynamoDB)
* [96 - Running Lambda on a Schedule](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/96%20-%20Running%20Lambda%20on%20a%20Schedule)
* [95 - CloudWatch event for RDS backup to DynamoDB](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/95%20-%20CloudWatch%20event%20for%20RDS%20backup%20to%20DynamoDB)
* [94-React-App-On-S3-and-CloudFront](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/94-React-App-On-S3-and-CloudFront)
* [93-Docker-Flask-App-with-Aurora](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/93-Docker-Flask-App-with-Aurora)
* [92-Moving Route 53 DNS to Lightsail](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/92-Moving%20Route%2053%20DNS%20to%20Lightsail)
* [91-Create-VPC-EC2-for-website-with-CLI](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/91-Create-VPC-EC2-for-website-with-CLI)
* [90-CloudFront-for-dynamic-websites](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/90-CloudFront-for-dynamic-websites)
* [89-API-Gateway-with-parameters](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/89-API-Gateway-with-parameters)
* [88-DynamoDB-Stream-using-Lambda](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/88-DynamoDB-Stream-using-Lambda)
* [87-Create-API-based-visitors-counter](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/87-Create-API-based-visitors-counter)
* [86-JavaScript-Visitors-Counter-with-API](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/86-JavaScript-Visitors-Counter-with-API)
* [85-CICD-Deploy-App-CodePipeline-CodeBuild](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/85-CICD-Deploy-App-CodePipeline-CodeBuild)
* [84-Static-Website-with-CloudFront-Distribution](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/84-Static-Website-with-CloudFront-Distribution)
* [83-Provisioning-EC2-with-CloudFormation](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/83-Provisioning-EC2-with-CloudFormation)
* [82-Lambda-triggered-from-SQS](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/82-Lambda-triggered-from-SQS)
* [81-SAM-with-CodeDeploy](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/81-SAM-with-CodeDeploy)
* [80-Amazon-Rekognition-CDK-deployed](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/80-Amazon-Rekognition-CDK-deployed)
* [79-Create&Deploy-App-CodeDeploy-CodePipeline](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/79-Create%26Deploy-App-CodeDeploy-CodePipeline)
* [78-Deploy-App-on-ECS-using-CodeDeploy](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/78-Deploy-App-on-ECS-using-CodeDeploy)
* [77-Install-Python-Modules-Using-Cloud9](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/77-Install-Python-Modules-Using-Cloud9)
* [76-ENI-Multiple-IPs-on-EC2](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/76-ENI-Multiple-IPs-on-EC2)
* [75-Launch-Windows-EC2-and-connect-using-RDC](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/75-Launch-Windows-EC2-and-connect-using-RDC)
* [74-Blue-Green-Deployments-with-Elastic-Beanstalk](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/74-Blue-Green-Deployments-with-Elastic-Beanstalk)
* [73-Host-Static-S3-website-with-CloudFront](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/73-Host-Static-S3-website-with-CloudFront)
* [72-Terraform-launch-NGINX-on-EC2](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/72-Terraform-launch-NGINX-on-EC2)
* [71-Amazon-Lex-create-a-bot](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/71-Amazon-Lex-create-a-bot)
* [70-SAM-Iac-Website-with-CloudFront-1](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/70-SAM-Iac-Website-with-CloudFront-1)
* [69-Highly-Available-Web-App-and-Bastion-Host-on-EC2](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/69-Highly-Available-Web-App-and-Bastion-Host-on-EC2)
* [68-Storing-ELB-Access-Logs-in-S3-bucket](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/68-Storing-ELB-Access-Logs-in-S3-bucket)
* [67-SAM-IaC-Website-with-CloudFront-2](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/67-SAM-IaC-Website-with-CloudFront-2)
* [66-Data-in-S3-for-Analytics-in-Athena](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/66-Data-in-S3-for-Analytics-in-Athena)
* [65-S3-triggering-Lambda-on-events](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/65-S3-triggering-Lambda-on-events)
* [64-Amazon-EC2-ASG-and-ALB](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/64-Amazon-EC2-ASG-and-ALB)
* [63-Mounting-EFS-to-EC2](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/63-Mounting-EFS-to-EC2)
* [62-Create-EC2-using-Snapshot-and-AMI](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/62-Create-EC2-using-Snapshot-and-AMI)
* [61-DynamoDB-and-Lambda](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/61-DynamoDB-and-Lambda)
* [60-Elastic-Beanstalk-and-CodePipeline](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/60-Elastic-Beanstalk-and-CodePipeline)
* [59-Auto-Scaling-Group-with-Load-Balancer](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/59-Auto-Scaling-Group-with-Load-Balancer)
* [58-Create-VPC-with-IGW-and-Route-Table](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/58-Create-VPC-with-IGW-and-Route-Table)
* [57-Securing-VPC-using-Private&Public-subnets](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/57-Securing-VPC-using-Private%26Public-subnets)
* [56-High-Availability-VPC](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/56-High-Availability-VPC)
* [55-Roles-and-Groups-using-IAM](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/55-Roles-and-Groups-using-IAM)
* [54-ELB-Network-Load-Balancer-Challenge](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/54-ELB-Network-Load-Balancer-Challenge)
* [53-Docker-on-Linux](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/53-Docker-on-Linux)
* [52-Create-RDS-DB-connect-using-Systems-Manager](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/52-Create-RDS-DB-connect-using-Systems-Manager)
* [51-EC2-Auto-Scaling-Challenge](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/51-EC2-Auto-Scaling-Challenge)
* [50-Scheduling-Lambda-using-EventBridge](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/50-Scheduling-Lambda-using-EventBridge)
* [49-React-App-on-Amplify](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/49-React-App-on-Amplify)
* [48-Terraform-Nginx-webserver-VPC-subnets](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/48-Terraform-Nginx-webserver-VPC-subnets)
* [47-Terraform-Advanced-VPC-ALB-EC2](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/47-Terraform-Advanced-VPC-ALB-EC2)
* [46-ALB-with-ASG-in-EC2](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/46-ALB-with-ASG-in-EC2)
* [45-Terraform-Modules-WebApp-API-VPC-ALB-EC2](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/45-Terraform-Modules-WebApp-API-VPC-ALB-EC2)
* [44-AWS-Config-Rules](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/44-AWS-Config-Rules)
* [43-Terraform-remote-and-lock-S3-DynamoDB-Challange](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/43-Terraform-remote-and-lock-S3-DynamoDB-Challange)
* [42-CloudTrail-Events-with-CloudWatch](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/42-CloudTrail-Events-with-CloudWatch)
* [41-CloudSearch-App](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/41-CloudSearch-App)
* [40-SageMaker-Notebooks-Machine-Learning](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/40-SageMaker-Notebooks-Machine-Learning)
* [39-SQS Queue Creation Challenge](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/39-SQS%20Queue%20Creation%20Challenge)
* [38-Solutions-Architect-Associate-Certification-Challenge](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/38-Solutions-Architect-Associate-Certification-Challenge)
* [37-ENI-Multiple-IPs-on-EC2](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/37-ENI-Multiple-IPs-on-EC2)
* [36-EBS-Challenge](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/36-EBS-Challenge)
* [35-VPC-Challenge](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/35-VPC-Challenge)
* [34-Automating-EBS-snapshots-with-Lambda](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/34-Automating-EBS-snapshots-with-Lambda)
* [33-Encrypt-RDS-DB-Instance](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/33-Encrypt-RDS-DB-Instance)
* [32-DynamoDB-triggers-with-Lambda](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/32-DynamoDB-triggers-with-Lambda)
* [31-RDS-DB-Challange](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/31-RDS-DB-Challange)
* [30-SNS-Image-Resizing-Challenge](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/30-SNS-Image-Resizing-Challenge)
* [29-Using-EC2-Spot-Instances](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/29-Using-EC2-Spot-Instances)
* [28-Manage-Message-Queues-Using-SQS](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/28-Manage-Message-Queues-Using-SQS)
* [27-Fan-Out-Orders-using-SNS-and-SQS](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/27-Fan-Out-Orders-using-SNS-and-SQS)
* [26-Create-VPC-with-CloudFormation](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/26-Create-VPC-with-CloudFormation)
* [25-Layered-Security-in-VPC](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/25-Layered-Security-in-VPC)
* [24-Lambda-Custom-Runtimes-to-Run-Bash-Commands](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/24-Lambda-Custom-Runtimes-to-Run-Bash-Commands)
* [23-Manage-Authentication-with-Cognito](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/23-Manage-Authentication-with-Cognito)
* [22-Directory-Service-working-with-Simple-AD](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/22-Directory-Service-working-with-Simple-AD)
* [21-Deploy-Highly-Available-Website-with-Terraform](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/21-Deploy-Highly-Available-Website-with-Terraform)
* [20-React-Voting-App-on-EC2](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/20-React-Voting-App-on-EC2)
* [19-Real-time-data-streaming-with-Kinesis-Data-Stream-and-Agent](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/19-Real-time-data-streaming-with-Kinesis-Data-Stream-and-Agent)
* [18-Export-RDS-DB-Snapshot-to-S3](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/18-Export-RDS-DB-Snapshot-to-S3)
* [17-Serverless-Container-App-On-Fargate](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/17-Serverless-Container-App-On-Fargate)
* [16-Monitoring-EC2-with-CloudWatch](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/16-Monitoring-EC2-with-CloudWatch)
* [15-Deploy-Wordpress-using-CloudFormation](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/15-Deploy-Wordpress-using-CloudFormation)
* [14-DynamoDB-Global-Secondary-Index](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/14-DynamoDB-Global-Secondary-Index)
* [13-Query-RDS-DB-with-Lambda](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/13-Query-RDS-DB-with-Lambda)
* [12-Predicting-Time-Series-Data-With-Forecast](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/12-Predicting-Time-Series-Data-With-Forecast)
* [11-Deploy-DocumentDB-cluster](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/11-Deploy-DocumentDB-cluster)
* [10-Aggregating-Data-with-Managed-Streaming-for-Apache-Kafka](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/10-Aggregating-Data-with-Managed-Streaming-for-Apache-Kafka)
* [09-Application-Load-Balander-for-ECS](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/09-Application-Load-Balander-for-ECS)
* [08-Deploy-WordPress-on-EKS-Kubernetes-Cluster](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/08-Deploy-WordPress-on-EKS-Kubernetes-Cluster)
* [07-S3-Events-With_lambda](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/07-S3-Events-With_lambda)
* [06-S3-Object-Lambda](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/06-S3-Object-Lambda)
* [05-Accessing-DynamoDB-using-API-Gateway](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/05-Accessing-DynamoDB-using-API-Gateway)
* [04-Deploy-Scalability-using-CloudFormation](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/04-Deploy-Scalability-using-CloudFormation)
* [03-Storing-and-Rotating-RDS-Credentials-in-Secrets-Manager](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/03-Storing-and-Rotating-RDS-Credentials-in-Secrets-Manager)
* [02-Running-queries-using-Redshift](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/02-Running-queries-using-Redshift)
* [01-Deploy-Infrastructure-with-Terraform](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/01-Deploy-Infrastructure-with-Terraform)
* [00-CloudFormation-Stack-Update](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/00-CloudFormation-Stack-Update)






## License

Distributed under the MIT License.



<!-- CONTACT -->
## Contact

[My blog](cloudofthings.net)

[Cloud Resume Challenge](profile.cloudofthings.net)

Leszek Ucinski [![LinkedIn][linkedin-shield]][linkedin-url]

Project Link: [https://github.com/CloudedThings/100-Days-in-Cloud](https://github.com/CloudedThings/100-Days-in-Cloud)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [A Cloud Guru](https://acloudguru.com/)
* [Whizlabs](https://www.whizlabs.com/)
* [Udemy](https://www.udemy.com/)
* [Be A Better Dev](https://www.youtube.com/c/BeABetterDev)
* [AWS](https://aws.amazon.com/training/self-paced-labs/)

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/leszekucinski/
