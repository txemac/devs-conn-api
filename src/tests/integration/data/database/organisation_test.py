from data.database.organisation import Organisation
from data.schemas import OrganisationPost


def test_create(session, data_organisation):
    count1 = session.query(Organisation).count()
    data = OrganisationPost(name=data_organisation['name'])
    Organisation.create(
        db_session=session,
        data=data
    )
    count2 = session.query(Organisation).count()
    assert count1 + 1 == count2


def test_get_or_create_by_name_get(session, new_organisation):
    count1 = session.query(Organisation).count()
    Organisation.get_or_create_by_name(
        db_session=session,
        name=new_organisation.name,
    )
    count2 = session.query(Organisation).count()
    assert count1 == count2


def test_get_or_create_by_name_create(session):
    count1 = session.query(Organisation).count()
    Organisation.get_or_create_by_name(
        db_session=session,
        name='not_exists',
    )
    count2 = session.query(Organisation).count()
    assert count1 + 1 == count2


def test_get_ids_from_names(session, new_organisation):
    assert Organisation.get_ids_from_names(db_session=session, names=[new_organisation.name]) == [new_organisation.id]


def test_get_names_from_ids(session, new_organisation):
    assert Organisation.get_names_from_ids(db_session=session, ids=[new_organisation.id]) == [new_organisation.name]
