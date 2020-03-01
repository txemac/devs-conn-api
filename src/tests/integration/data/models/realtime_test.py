from data.models.organisation import Organisation
from data.models.realtime import Realtime
from data.models.user import User
from data.schemas import RealtimePost


def test_create_creates(session):
    count_realtime_1 = session.query(Realtime).count()
    count_user_1 = session.query(User).count()
    count_organisations_1 = session.query(Organisation).count()
    data = RealtimePost(
        user_1='txemac',
        user_2='fever',
        connected=True,
        organisations=['new_1', 'new_2'],
    )
    Realtime.create(
        db_session=session,
        data=data
    )
    count_realtime_2 = session.query(Realtime).count()
    count_user_2 = session.query(User).count()
    count_organisations_2 = session.query(Organisation).count()
    assert count_realtime_1 + 1 == count_realtime_2
    assert count_user_1 + 2 == count_user_2
    assert count_organisations_1 + 2 == count_organisations_2


def test_create_get(session, new_user, new_organisation):
    count_realtime_1 = session.query(Realtime).count()
    count_user_1 = session.query(User).count()
    count_organisations_1 = session.query(Organisation).count()
    data = RealtimePost(
        user_1=new_user.name,
        user_2='fever',
        connected=True,
        organisations=[new_organisation.name],
    )
    Realtime.create(
        db_session=session,
        data=data
    )
    count_realtime_2 = session.query(Realtime).count()
    count_user_2 = session.query(User).count()
    count_organisations_2 = session.query(Organisation).count()
    assert count_realtime_1 + 1 == count_realtime_2
    assert count_user_1 + 1 == count_user_2
    assert count_organisations_1 == count_organisations_2
