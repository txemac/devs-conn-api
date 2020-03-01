from typing import Dict
from typing import List
from typing import Union

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK

from app.utils import get_connections
from data import get_db
from data.api_clients import github_api_client
from data.api_clients import twitter_api_client
from data.models.realtime import Realtime
from data.schemas import RealtimePost

api_v1_connected = APIRouter()


@api_v1_connected.get('/realtime/{dev1}/{dev2}', status_code=HTTP_200_OK)
def get_real_time(
        *,
        db_session: Session = Depends(get_db),
        dev1: str,
        dev2: str,
) -> Dict[str, Union[bool, List[str]]]:
    github_user_1 = github_api_client.get_organisations(username=dev1)
    github_user_2 = github_api_client.get_organisations(username=dev2)
    twitter_user_1 = twitter_api_client.get_friends(username=dev1)
    twitter_user_2 = twitter_api_client.get_friends(username=dev2)

    # not valid user
    errors = [x for x in [github_user_1, github_user_2, twitter_user_1, twitter_user_2] if isinstance(x, str)]
    if errors:
        return dict(errors=errors)

    connected, organisations = get_connections(
        dev1=dev1,
        dev2=dev2,
        twitter_user_1=twitter_user_1,
        twitter_user_2=twitter_user_2,
        github_user_1=github_user_1,
        github_user_2=github_user_2,
    )

    # create response
    response = dict(connected=connected)
    if connected is True:
        response.update(organisations=organisations)

    # save
    Realtime.create(
        db_session=db_session,
        data=RealtimePost(
            user_1=dev1,
            user_2=dev2,
            connected=connected,
            organisations=organisations,
        )
    )

    return response
