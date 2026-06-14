"""initial

Revision ID: 0001
Revises:
Create Date: 2026-06-07
"""

from alembic import op
import sqlalchemy as sa


revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        "users",
        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True
        ),
        sa.Column(
            "username",
            sa.String(100),
            nullable=False,
            unique=True
        ),
        sa.Column(
            "password_hash",
            sa.String(255),
            nullable=False
        ),
        sa.Column(
            "role",
            sa.Enum(
                "ADMIN",
                "EMPLOYEE",
                name="userrole"
            ),
            nullable=False
        )
    )

    op.create_table(
        "rooms",
        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True
        ),
        sa.Column(
            "name",
            sa.String(100),
            nullable=False,
            unique=True
        ),
        sa.Column(
            "description",
            sa.String(500)
        )
    )

    op.create_table(
        "time_slots",
        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True
        ),
        sa.Column(
            "room_id",
            sa.Integer(),
            sa.ForeignKey("rooms.id"),
            nullable=False
        ),
        sa.Column(
            "start_time",
            sa.Time(),
            nullable=False
        ),
        sa.Column(
            "end_time",
            sa.Time(),
            nullable=False
        )
    )

    op.create_table(
        "bookings",
        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True
        ),
        sa.Column(
            "room_id",
            sa.Integer(),
            sa.ForeignKey("rooms.id")
        ),
        sa.Column(
            "slot_id",
            sa.Integer(),
            sa.ForeignKey("time_slots.id")
        ),
        sa.Column(
            "user_id",
            sa.Integer(),
            sa.ForeignKey("users.id")
        ),
        sa.Column(
            "booking_date",
            sa.Date(),
            nullable=False
        ),
        sa.Column(
            "created_at",
            sa.DateTime()
        ),
        sa.UniqueConstraint(
            "room_id",
            "slot_id",
            "booking_date",
            name="uq_room_slot_date"
        )
    )


def downgrade():

    op.drop_table("bookings")
    op.drop_table("time_slots")
    op.drop_table("rooms")
    op.drop_table("users")