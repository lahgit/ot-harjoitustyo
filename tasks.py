from invoke import task

@task
def test(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)

@task
def coverage_report(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)
    ctx.run("coverage html ",pty=True)

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)
