# tasks.py

from invoke import task

@task
def test(c):
    """
    Ejecuta las pruebas unitarias
    """
    c.run("pytest test/test_profile.py")
