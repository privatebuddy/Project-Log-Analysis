# Project-Log-Analysis
Project Log Analysis for Study Udacity 

Develop by Sasin Siriskaowkul

# Dependencies 
- PostgreSQL version 10.5
- Python version 2.7

# Resource 
1. Database Link
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

# Setup
1. Install Virtual Machine if you are running non linux base computer
  1.1 Install Virtual Box : https://www.virtualbox.org/wiki/Downloads
  1.2 Install Vagrant : https://www.vagrantup.com/downloads.html
  1.3 Download VM Configuration : https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip
2. Install PostgreSQL 
  2.1 via Homebrew if you are macOS, Ubontu
  2.2 install on vm
3. run code by 'python LogAnalysis.py' on terminal 

# Design

1. Question 1 : What are the most popular three articles of all time?
   In the log table, they are data provide about the article URL path which is in format of ("/article/article-slug") so the program is designed to count all of the path columns and then join articles table on slug which is combined with "/article" to be the resulting program expect. Then on the Python part, the program is using replace string to format the data to be easier to read in the console.
   
2. Question 2 : Who are the most popular article authors of all time? 
  In the author's table that has the name of each author that write an article on the website. First, the program is joining the authors with articles using authors primary key (id), and foreign key on the article (author) then join it with log table on a path which is contain article slug of each author. Then on the Python part, the program is using replace string to format the data to be easier to read in the console.
  
3. Quesgtion 3 : On which days did more than 1% of requests lead to errors?
  For this question, Program is solved by two query which is one for good connection (200 OK) and bad connection (404 NOT FOUND) which is collected in the status column on the log table. By using a select status column with the result in good or bad into two arrays. Then on the Python part, the program is a loop on each of the data set to find which date contain more than 1% error.
