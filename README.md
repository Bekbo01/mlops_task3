# MLOps Task 3

> This repository contains code for integration of Machine Learning Model and DevOps.

>I have created such a environment which launches Container (Operating System with required tools) for running the Machine Learning model. After running Container it will automatically start training and prediction of model using Jenkins and sends accuracy to developer.

# TASK :

1. Create container image that has Python3 and Keras or tensorflow installed  using Dockerfile.


2. Create a job chain of job1, job2, job3, job4 and job5 using build pipeline plugin in Jenkins.


3. Job1 : Pull the Github repo automatically when some developers push repo to Github.


4. Job2 : By looking at the code or program file, Jenkins should automatically start the respective container.


5. Job3 : Train your model and predict accuracy.


6. Job4 : If accuracy is less than 90% then tweak the machine learning model architecture and retrain it.


7. Job5: Notify that the best model is being created.


8. Create One extra job job6 for monitor. If container where app is running fails due to any reason then this job should automatically start the container again from where the last trained model left.

# Task 1 :
Create container image that has Python3 and Keras or tensorflow installed using Dockerfile.
- Copy the ***[Dockerfile](https://github.com/sagargarg27/mlops_task3/blob/master/Dockerfile)*** from this repository and paste it into a new directory.
- Go to that directory and run this command.
```
 docker build -t mytf:v1 .
 ```
 - Now we have an image named `mytf:v1`
 - Make sure you have internet connectivity while building this image.

 # Task 2 :
Create a job chain of job1, job2, job3, job4 and job5 using build pipeline plugin in Jenkins. 

I have created this pipeline :

![Build Pipeline](https://github.com/sagargarg27/mlops_task3/blob/master/Images/Build_pipeline.png)

# Job 1 :
Pull the Github repo automatically when some developers push repo to Github.

![Github](https://github.com/sagargarg27/mlops_task3/blob/master/Images/Github1.png)

![Github](https://github.com/sagargarg27/mlops_task3/blob/master/Images/github2.png)

# JOB 2 :
By looking at the code or program file, Jenkins should automatically start the respective container.

![Docker](https://github.com/sagargarg27/mlops_task3/blob/master/Images/Job2Docker.png)

# Job 3 :
Train your model and predict accuracy.

![Training Model](https://github.com/sagargarg27/mlops_task3/blob/master/Images/Job3Model.png)

# Job 4 :
If accuracy is less than 90% then tweak the machine learning model architecture and retrain it.

![Tweaking Model](https://github.com/sagargarg27/mlops_task3/blob/master/Images/Job4tweak.png)

# Job 5 :
Notify that the best model is being created.

![Notification](https://github.com/sagargarg27/mlops_task3/blob/master/Images/Job5mail.png)

# Job 6 :
If container where app is running fails due to any reason then this job should automatically start the container again from where the last trained model left.

![Monitor](https://github.com/sagargarg27/mlops_task3/blob/master/Images/Job6Monitor.png)

>Tools and Technologies used in this project:
- Docker : for creating and launching the image in container.
- Jenkins : for creating pipeline between the jobs.
- Git & Github : for continuous integeration and continuous delivery.
- Virtual Machine : for running my Rhel8.