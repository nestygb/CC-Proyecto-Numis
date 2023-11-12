# tasks.py
import sys
sys.path.append('src')
from invoke import task

@task
def test(c):
    """
    Ejecuta las pruebas unitarias
    """
    c.run("pytest test/test.py")
