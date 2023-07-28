from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from models.user_model import UserModel
from core.deps import get_session


# #Bypass warning SQLModel select
# from sqlmodel.sql.expression import Select, SelectOfScalar

# SelectOfScalar.inherit_cache = True # type: ignore
# Select.inherit_cache = True # type: ignore
# #Fim Bypass

router = APIRouter()

# POST user
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserModel)
async def post_user(user: UserModel, db: AsyncSession = Depends(get_session)):
    new_user = UserModel(nome=user.nome, email=user.email, senha=user.senha)
    
    db.add(new_user)
    await db.commit()
    
    return new_user


# GET user
@router.get('/', response_model=List[UserModel])
async def get_users(db: AsyncSession = Depends(get_session)):
    
    async with db as session:
        query = select(UserModel)
        result = await session.execute(query)
        users: List[UserModel] = result.scalars().all()
        
        return users
    
    
@router.get('/{user_id}', response_model=UserModel, status_code=status.HTTP_200_OK)
async def get_user(user_id: int, db: AsyncSession = Depends(get_session)):
    
    async with db as session:
        query = select(UserModel).filter(UserModel.id == user_id)
        result = await session.execute(query)
        user: UserModel = result.scalar_one_or_none()
        
        if user:
            return user
        else:
            raise HTTPException(detail='User not found', status_code=status.HTTP_404_NOT_FOUND)
        

@router.put('/{user_id}', status_code=status.HTTP_202_ACCEPTED, response_model=UserModel)
async def put_user(user_id: int, user: UserModel, db:AsyncSession = Depends(get_session)):
    
    async with db as session:
        query = select(UserModel).filter(UserModel.id == user_id)
        result = await session.execute(query)
        user_up: UserModel = result.scalar_one_or_none()

        if user_up:
            user_up.nome = user.nome
            user_up.email = user.email
            user_up.senha = user.senha
            
            await session.commit()
            
            return user_up
        else:
            raise HTTPException(detail='User not found', status_code=status.HTTP_404_NOT_FOUND)
        

# DELETE user
@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_session)):
    
    async with db as session:
        query = select(UserModel).filter(UserModel.id == user_id)
        result = await session.execute(query)
        user_del: UserModel = result.scalar_one_or_none()

        if user_del:
            await session.delete(user_del)
            
            await session.commit()
        
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='User not found', status_code=status.HTTP_404_NOT_FOUND)