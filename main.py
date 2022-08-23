from fastapi import FastAPI

import router.user
from db import models
from router import blog_get
from router import blog_post
from db.database import engine

app = FastAPI()
app.include_router(router.user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get('/')
def index():
    return 'Hello World'


models.Base.metadata.create_all(engine)