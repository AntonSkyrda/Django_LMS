from invoke import task


@task
def build(c):
    c.run("docker-compose up --build -d")


@task
def logs(c):
    c.run("docker-compose logs -f")


@task
def migrate(c):
    c.run("docker exec django_app python manage.py migrate")


@task
def collectstatic(c):
    c.run("docker exec django_app python manage.py collectstatic --noinput")


@task
def createsuperuser(c):
    c.run("docker exec -it django_app python manage.py createsuperuser")


@task
def restart(c):
    c.run("docker-compose restart")
