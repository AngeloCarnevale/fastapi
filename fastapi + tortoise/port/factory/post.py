from adapter.post import PostTortoiseAdapter
from adapter.schemas.post import PostModel
from domain.service.post import PostService


# Factory é a instânciação de todos os ciclos/processos
def post_factory():
    adapter = PostTortoiseAdapter(model=PostModel)
    service = PostService(adapter=adapter)
    return service
