from fastapi import  HTTPException
from app.schemas import OperationRequest
from app.repositoriy import wallets as wallets_repository
from app.database import SessionLocal


def add_income(operation: OperationRequest):
    db = SessionLocal()
    try:
        if not wallets_repository.is_wallet_exist(db, operation.wallet_name):
            raise HTTPException(status_code=400, detail=f"wallet '{operation.wallet_name}' not exists ")
        wallet = wallets_repository.add_income(db, operation.wallet_name, operation.amount)

        return {'message': f"wallet '{operation.wallet_name}' add {operation.amount} ",
                'wallet' :operation.wallet_name,
                'balance' :wallet}
    finally:
        db.close()


def add_expensive(operation: OperationRequest):
    db = SessionLocal()
    try:
        if not wallets_repository.is_wallet_exist(db, operation.wallet_name):
            raise HTTPException(status_code=400,
                                detail=f"wallet '{operation.wallet_name}' not exists ")
        wallet = wallets_repository.get_wallet_balance_by_name(db, operation.wallet_name)
        if operation.amount > wallet.balance:
            raise HTTPException(status_code=400,detail='not money')
        wallet = wallets_repository.add_expense(db, operation.wallet_name, operation.amount)

        return {'message': f"wallet '{operation.wallet_name}' exp {operation.amount} ",
                'wallet': operation.wallet_name,
                'balance': wallet.balance}
    finally:
        db.close()
