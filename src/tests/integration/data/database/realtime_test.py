from data.database.organisation import Organisation
from data.database.realtime import Realtime
from data.database.user import User
from data.schemas import RealtimePost


def test_create_creates(session):
    count_realtime_1 = session.query(Realtime).count()
    count_user_1 = session.query(User).count()
    count_organisations_1 = session.query(Organisation).count()
    data = RealtimePost(
        user_1='txemac',
        user_2='jobandtalent',
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

    realtime = session.query(Realtime).order_by(Realtime.id.desc()).first()
    assert realtime.user_1_id == User.get_or_create_by_name(db_session=session, name=data.user_1).id
    assert realtime.user_2_id == User.get_or_create_by_name(db_session=session, name=data.user_2).id
    assert realtime.connected == data.connected
    assert list(map(int, realtime.organisations)) == Organisation.get_ids_from_names(db_session=session,
                                                                                     names=data.organisations)


def test_create_get(session, new_user, new_organisation):
    count_realtime_1 = session.query(Realtime).count()
    count_user_1 = session.query(User).count()
    count_organisations_1 = session.query(Organisation).count()
    data = RealtimePost(
        user_1=new_user.name,
        user_2='jobandtalent',
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

    realtime = session.query(Realtime).order_by(Realtime.id.desc()).first()
    assert realtime.user_1_id == User.get_or_create_by_name(db_session=session, name=data.user_1).id
    assert realtime.user_2_id == User.get_or_create_by_name(db_session=session, name=data.user_2).id
    assert realtime.connected == data.connected
    assert list(map(int, realtime.organisations)) == Organisation.get_ids_from_names(db_session=session,
                                                                                     names=data.organisations)


def test_create_false(session, new_user):
    count_realtime_1 = session.query(Realtime).count()
    count_user_1 = session.query(User).count()
    count_organisations_1 = session.query(Organisation).count()
    data = RealtimePost(
        user_1=new_user.name,
        user_2='jobandtalent',
        connected=False,
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

    realtime = session.query(Realtime).order_by(Realtime.id.desc()).first()
    assert realtime.user_1_id == User.get_or_create_by_name(db_session=session, name=data.user_1).id
    assert realtime.user_2_id == User.get_or_create_by_name(db_session=session, name=data.user_2).id
    assert realtime.connected == data.connected
    assert realtime.organisations is None
