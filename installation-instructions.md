# Installation Instructions

## Workplace Setup

### Install Python

Download and install Python from [here](https://www.python.org/downloads/)

Downloading the installer should automatically install Python and PIP



### Install EB CLI  

Run the following command to install AWS EB CLI

`pip install awsebcli --upgrade --user`

Add `%USERPROFILE%\AppData\roaming\Python\Python%VERSION%\scripts` to your PATH

Confirm installation with `eb --version`

**References**
- [Install EB CLI on Windows](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-windows.html)



### Install Discord

Use the following command to install Discord using pip

`pip install -U discord.py`



### Setup AWS Console

Login to the AWS Console with the unique user sign in link

The console link should be in the following format: `https://<unique-number>.signin.aws.amazon.com/console`

On initial setup, use the preconfigured password and username to log in

Ex:

`Username: faeribot-user-charlotte`

`Password: I am smoww and tewwibwe`

Once logged in, it will prompt you to change your password

Please change your password and take note of the new credentials

Access to the AWS Console should now be available



### Setup Elastic Beanstalk Workplace

Run the following command to setup

`eb init -i`

It will require AWS account access setup. Supply the respective Access Key ID and Access Key Secret when asked

When asked for the region, select `(1) us-east-1 (West Virginia)`

When asked for the application, select `(1) faeriebot`

When asked for CodeCommit, select `(n) no`

To confirm the correct application and environment, run `eb list`

The environment `faeriebot-dev` should be selected

Elasic Beanstalk should be completely setup on the account



### Deploying using Elastic Beanstalk

Make sure that the environment is set to `faeriebot-dev` by running the command `eb list`

Make sure all necessary changes to be added in the application are pushed to the repository

To deploy, run the command `eb deploy`

The command will deploy the newly updated files to the selected environment
