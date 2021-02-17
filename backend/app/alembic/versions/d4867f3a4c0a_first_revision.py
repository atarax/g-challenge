"""First revision

Revision ID: d4867f3a4c0a
Revises:
Create Date: 2019-04-17 13:53:32.978401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d4867f3a4c0a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "brand",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False, unique=True),
        sa.PrimaryKeyConstraint("id")
    )

    op.create_table(
        "product_category",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False, unique=True),
        sa.PrimaryKeyConstraint("id")
    )

    op.create_table(
        "store",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("code", sa.String(), nullable=False, unique=True),
        sa.PrimaryKeyConstraint("id")
    )

    op.create_table(
        "product",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False, unique=True),
        sa.Column("brand_id", sa.Integer(), nullable=False),
        sa.Column("category_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["brand_id"], ["brand.id"],),
        sa.ForeignKeyConstraint(["category_id"], ["product_category.id"],),
        sa.PrimaryKeyConstraint("id")
    )

    op.create_table(
        "stock_levels",
        sa.Column("product_id", sa.Integer(), nullable=False),
        sa.Column("store_id", sa.Integer(), nullable=False),
        sa.Column("amount", sa.Integer(), nullable=False),
        sa.UniqueConstraint('product_id', 'store_id', name='uq_product_store'),
        sa.ForeignKeyConstraint(["product_id"], ["product.id"],),
        sa.ForeignKeyConstraint(["store_id"], ["store.id"],),
    )

def downgrade():
    op.drop_table("brand")
    op.drop_table("product_category")
    op.drop_table("store")
    op.drop_table("product")
    op.drop_table("stock_levels")
