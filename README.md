# πΌπ±π²π·π²π·π° πΌπ½πͺπ» πͺπππͺπ»π­πΌπ

![Screen Shot 2022-06-15 at 03 51 10](https://user-images.githubusercontent.com/62022158/173713727-c52ec9d5-2035-4895-973a-a5344a4c1ac9.png)

![Screen Shot 2022-06-15 at 03 51 20](https://user-images.githubusercontent.com/62022158/173713784-98fabd72-2585-454d-9306-a9027aa45b4f.png)

![Screen Shot 2022-06-15 at 03 53 48](https://user-images.githubusercontent.com/62022158/173713845-1a040558-3dc1-4a6b-8f42-ef879ba01410.png)

The πΌπ±π²π·π²π·π° πΌπ½πͺπ» πͺπππͺπ»π­πΌπ is an application will allow a user to post a project he/she has created and get it reviewed by his/her peers.

# DescriptionπΈ

The First impression which makes this web application stand out from the rest is this the motto: ππ’π¦π«π€ β­π―π’ππ±π¦π³π’ πͺππ¨π’ π¦π± π¬π― ππ―π’ππ¨, πΆπ¬π²π― π­π¬π°π±π° π ππ« π°π’π©π© π¦π‘π’ππ°
πΌπ±π²π·π²π·π° πΌπ½πͺπ» πͺπππͺπ»π­πΌπ users are able to create account upload their best projects with their unique ideas and showoff their skills.

# Behaviour Driven Developmentπ

<p>

- A user can View posted projects and their details
- A user can upload pictures to the application.
- As user can see their profile with all their pictures.
- A user can Search for projects.
</p>

# INSTALLATION PROCESS β¨

To use the application you should have python3 and django latest version installed in your machine.

- Create and activate the vitual Environment and install the from requirements.txt
  `$ python3 -m virtualenv virtual`
  `$ source virtual/bin/activate`
  `$ pip install -r requirements.txt`

> It will install everything from the requirements file after configuring launch and enjoy.

- Setting up environment variables

Create an `.env` and add the following.

```
SECRET_KEY='<Secret_key>'
DBNAME='<DbName>'
USER='<Username>'
PASSWORD='<password>'
DEBUG=True
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='.localhost','.herokuapp.com','127.0.0.1'
DISABLE_COLLECTSTATIC=1

```

- Start the Server to run the app
- `$ python3 manage.py runserver`

- Open [localhost:8000](#)

---

# TECHNOLOGIES USED β¨

I have used:

   <li>Python3</li>
   <li>Django</li>
   <li>Html</li>
   <li>Css</li>
  <li>PostgreSql</li>

# Improvement plans ποΈ

> <li> Users are able to rate/review projects from their fellow peers.</li>

> <li>Users View projects overall score due to rate/review functionality.</li>

# AUTHORS NAMEπ¦

> jimmy-oss

# BUGSπ’

> No bugs so far

# THE LICENSEπ¨πΎββοΈ

The website is under Mit license.
