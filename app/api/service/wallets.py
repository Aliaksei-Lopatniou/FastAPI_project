from fastapi import HTTPException
from app.schemas import CreateWalletRequest
from app.repositoriy import wallets as wallets_repository
from app.database import SessionLocal


def get_balance(wallet_name: str | None=None):
    db = SessionLocal()
    try:
        if wallet_name is None:
            wallets = wallets_repository.get_all_wallets(db)
            return { 'Total_balance' : sum([w.balance for w in wallets])}
        if not wallets_repository.is_wallet_exist(db, wallet_name):
            return HTTPException(status_code=404, detail=f"wallet not found ")
        wallet = wallets_repository.get_wallet_balance_by_name(db, wallet_name)
        return { 'wallet' :wallet.name, 'balance' :wallet.balance}

    finally:
        db.close()


def create_wallet(wallet : CreateWalletRequest):
    db = SessionLocal()
    try:
        if  wallets_repository.is_wallet_exist(db, wallet.wallet_name):
            raise HTTPException(status_code=400, detail=f"wallet  already exists ")
        wallet = wallets_repository.create_wallet(db, wallet.wallet_name, wallet.initial_balance)
        return {
                'message': f"wallet '{wallet.name}' created",
                'wallet' :wallet.name,
                'balance' :wallet.balance
            }

    finally:
        db.close()

