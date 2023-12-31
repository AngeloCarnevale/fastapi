from fastapi import APIRouter, Depends
from domain.entities.post import Post, PostDto
from domain.service.post import PostService

from port.factory.post import post_factory

router = APIRouter()

@router.get('/')
async def list_posts(service: PostService = Depends(post_factory)):
    return await service.list()

@router.post('/')
async def create_post(body: PostDto, service: PostService = Depends(post_factory)):
    post = Post(**body.model_dump())
    return await service.create(post=post)

@router.get('/{post_id}')
async def get_post(post_id: int, service: PostService = Depends(post_factory)):
    return await service.get(post_id)

@router.put('/{post_id}/publish')
async def publish_post(post_id: int, service: PostService = Depends(post_factory)):
    return await service.publish(post_id) 