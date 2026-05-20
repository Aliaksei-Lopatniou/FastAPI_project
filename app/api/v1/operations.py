from fastapi import APIRouter
from app.api.service import  operations as operations_service
from app.schemas import OperationRequest

router = APIRouter()


@router.post('/operations/income')
def add_income(operation: OperationRequest):
    return operations_service.add_income(operation)


@router.post('/operations/expense')
def add_expensive(operation: OperationRequest):
    return operations_service.add_expensive(operation)