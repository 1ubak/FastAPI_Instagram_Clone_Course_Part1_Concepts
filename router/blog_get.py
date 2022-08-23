from fastapi import APIRouter, Depends
from os import stat
from typing import Optional
from fastapi import status, Response
from enum import Enum

from router.blog_post import dependencies_demo_function

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)



@router.get(
    "/all", 
    summary='Retrieve all blogs',
    description='This api call simulates fetching all blogs.',
    response_description='The list of available blogs'
    )
def get_all_blogs(page = 1, page_size = 10, tags = ['blog', 'comment'], depend_demo=Depends(dependencies_demo_function)):
    return {"message":f"All {page_size} blogs on page {page}","depend_demo":depend_demo}


@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    """
    test
    """
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error":"Not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message":f"Blog with id {id}"} 



@router.get('/{id}/comments/{comment_id}', tags = ['comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username : Optional[str] = None):
    """
    Simulates retrieving a comment of a blog

    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **valid** optional query parameter
    - **username** optional query parameter
    """
    return {"message":f"blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}"}


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@router.get('/type/{type}')
def blog_type(type: BlogType):
    return {"message":f"Blog type: {type}"}