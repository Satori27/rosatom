"""Add admin and create roles

Revision ID: 923633ef5d2e
Revises: fd6608c6a775
Create Date: 2024-11-04 18:16:31.982699

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from app.users.auth import get_password_hash
from app.config import ADMIN_EMAIL, ADMIN_LOGIN, ADMIN_PASSWORD
from passlib.hash import bcrypt



# revision identifiers, used by Alembic.
revision: str = '923633ef5d2e'
down_revision: Union[str, None] = 'fd6608c6a775'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    hashed_password = get_password_hash(ADMIN_PASSWORD)

    op.execute(
        f"""
        INSERT INTO users (name, hashed_password, email, roles)
        VALUES ('{ADMIN_LOGIN}', '{hashed_password}', '{ADMIN_EMAIL}', 'admin');
        """
    )


def downgrade() -> None:
    op.execute(
        f"""
        DELETE FROM users WHERE username = {ADMIN_LOGIN};
        """
    )
