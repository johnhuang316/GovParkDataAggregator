from api import taipeiapi, taoyuanapi, iapi


def get_api(api_name) -> iapi.IApi:
    match api_name:
        case "Taipei":
            api = taipeiapi.TaipeiApi()
        case "Taoyuan":
            api = taoyuanapi.TaoyuanApi()
        case _:
            raise ValueError("no api")
    return api
