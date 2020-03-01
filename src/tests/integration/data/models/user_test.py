from data.models.user import User
from data.schemas import UserPost


def test_create(session, data_user):
    count1 = session.query(User).count()
    data = UserPost(name=data_user['name'])
    User.create(
        db_session=session,
        data=data
    )
    count2 = session.query(User).count()
    assert count1 + 1 == count2


def test_get_or_create_by_name_get(session, new_user):
    count1 = session.query(User).count()
    User.get_or_create_by_name(
        db_session=session,
        name=new_user.name,
    )
    count2 = session.query(User).count()
    assert count1 == count2


def test_get_or_create_by_name_create(session):
    count1 = session.query(User).count()
    User.get_or_create_by_name(
        db_session=session,
        name='not_exists',
    )
    count2 = session.query(User).count()
    assert count1 + 1 == count2
