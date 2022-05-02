# Roadmap

## Version 1.0

Still on the making

### What this application is supposed to do on V1.0

- Browse blue collar jobs and apply to them
- Post jobs as an employer
- Register as an employer or as a job candidate
- Upload your cv
- Send your preffered cv to the company that holds the job post

### Stuff already done or fixed

- Add a candidate file uploads model
- Add user authentication classes 
- Add separate api viewsets for uploading files and changing password
- Change file upload api view to viewset 
- Add a company model and django app functionality
- Add separate api viewsets for checking files uploaded per candidate
- Add permission classes --> Added a user is loggen in class, for checking if the user in the session is the owner of the profile



### Stuff I will be working on

- Fixing
- Testing
- Work on the jopost api
- Make post job api functionality
- A custom search tool for candidates and jobposts
- An api call that lets you choose the file you're going to submit to the jobpost

### Stuff to be considered in the future
- Having multiple candidate profiles per user, like accomodating the profile to the job-post
- A spanish and english version of the profile

### Stuff I need to fix

- I should be able to change the account profile data without changing the password
- The media folder should not contain its own folder name, like media/media/uploaded
- I should include tests

