# hacked-2020-demo

## 1. Create an AWS Account

Go to https://aws.amazon.com/free/

Fill out the following form with your information
<img width="448" alt="Screen Shot 2020-01-12 at 9 28 04 PM" src="https://user-images.githubusercontent.com/14353143/72233182-ec9db300-3582-11ea-9260-3355118772f6.png">


## 2. Create Security Groups

- Navigate to https://us-west-2.console.aws.amazon.com/ec2/v2/home?region=us-west-2#Home:

<img width="212" alt="Screen Shot 2020-01-17 at 5 06 44 PM" src="https://user-images.githubusercontent.com/14353143/72655194-a369ac80-3950-11ea-9c6f-9b7e34c02ff4.png">
Create Django App Security group. Note that we will allow SSH to connect and install and 8080 to host our django app
<img width="1008" alt="Screen Shot 2020-01-17 at 5 10 03 PM" src="https://user-images.githubusercontent.com/14353143/72655196-a369ac80-3950-11ea-88d7-cb6c9b83011c.png">
Create the Database Security Group. Note that we don't allow anyone to access the DB. We will fix this later
<img width="995" alt="Screen Shot 2020-01-17 at 5 11 33 PM" src="https://user-images.githubusercontent.com/14353143/72655197-a369ac80-3950-11ea-8915-424f67f4d043.png">


## 3. Create a PostGres Database 

- Navigate to https://us-west-2.console.aws.amazon.com/rds/home?region=us-west-2

<img width="778" alt="Screen Shot 2020-01-17 at 5 13 03 PM" src="https://user-images.githubusercontent.com/14353143/72655275-0a876100-3951-11ea-9e50-97de5f1c9b4c.png">
<img width="759" alt="Screen Shot 2020-01-17 at 5 13 28 PM" src="https://user-images.githubusercontent.com/14353143/72655276-0a876100-3951-11ea-95b5-6acf7d628c24.png">
<img width="583" alt="Screen Shot 2020-01-17 at 5 14 44 PM" src="https://user-images.githubusercontent.com/14353143/72655277-0a876100-3951-11ea-8e59-2c7d16a8bfe7.png">
<img width="749" alt="Screen Shot 2020-01-17 at 5 15 32 PM" src="https://user-images.githubusercontent.com/14353143/72655278-0b1ff780-3951-11ea-8c75-97dbd3f24ca7.png">
<img width="751" alt="Screen Shot 2020-01-17 at 5 17 20 PM" src="https://user-images.githubusercontent.com/14353143/72655345-6225cc80-3951-11ea-960a-72dac7ee54dc.png">

## 4. Create a EC2 Instance

- Navigate back to https://us-west-2.console.aws.amazon.com/ec2/v2/home?region=us-west-2#Home:

<img width="203" alt="Screen Shot 2020-01-17 at 5 48 10 PM" src="https://user-images.githubusercontent.com/14353143/72655409-baf56500-3951-11ea-98bc-d26fac3031d5.png">
<img width="458" alt="Screen Shot 2020-01-17 at 5 49 03 PM" src="https://user-images.githubusercontent.com/14353143/72655410-baf56500-3951-11ea-9ac4-51f214347083.png">
<img width="1642" alt="Screen Shot 2020-01-17 at 5 22 10 PM" src="https://user-images.githubusercontent.com/14353143/72655428-d1032580-3951-11ea-8f19-c74ff6d6882d.png">
<img width="1680" alt="Screen Shot 2020-01-17 at 5 22 40 PM" src="https://user-images.githubusercontent.com/14353143/72655430-d1032580-3951-11ea-8a18-b3032f68bcbb.png">
<img width="954" alt="Screen Shot 2020-01-17 at 5 23 16 PM" src="https://user-images.githubusercontent.com/14353143/72655431-d1032580-3951-11ea-9d44-ce87e3195577.png">
<img width="1577" alt="Screen Shot 2020-01-17 at 5 23 28 PM" src="https://user-images.githubusercontent.com/14353143/72655432-d1032580-3951-11ea-96d4-f92d24726e50.png">
<img width="1316" alt="Screen Shot 2020-01-17 at 5 23 43 PM" src="https://user-images.githubusercontent.com/14353143/72655433-d19bbc00-3951-11ea-97ff-8122dc60a4c2.png">
<img width="1650" alt="Screen Shot 2020-01-17 at 5 24 08 PM" src="https://user-images.githubusercontent.com/14353143/72655434-d19bbc00-3951-11ea-90bc-73439f33d019.png">
<img width="1665" alt="Screen Shot 2020-01-17 at 5 25 06 PM" src="https://user-images.githubusercontent.com/14353143/72655435-d19bbc00-3951-11ea-8e47-60553a25d1de.png">
<img width="685" alt="Screen Shot 2020-01-17 at 5 26 34 PM" src="https://user-images.githubusercontent.com/14353143/72655443-dfe9d800-3951-11ea-8c60-835c2e058258.png">
<img width="1265" alt="Screen Shot 2020-01-17 at 5 28 35 PM" src="https://user-images.githubusercontent.com/14353143/72655444-dfe9d800-3951-11ea-8f46-b8fc2e2c1b0a.png">
<img width="1160" alt="Screen Shot 2020-01-17 at 5 29 48 PM" src="https://user-images.githubusercontent.com/14353143/72655445-dfe9d800-3951-11ea-81b2-a7a9e380739f.png">


Once you have access to the server run these commands:
```shell
sudo yum update -y 
sudo yum install -y python3 git
git clone https://github.com/Gknoblau/hacked-2020-demo.git
cd hacked-2020-demo/
```

