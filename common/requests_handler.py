import requests


def visit(url,
          params=None,
          data=None,
          json=None,
          headers=None,
          method='get',
          **kwargs
):
    """访问接口，返回字典 res.hson()"""
    res = requests.request(
        method.lower(),
        url,
        params=params,
        data=data,
        headers=headers,
        json=json,
        **kwargs
)

    try:
        return res.json()
    except Exception as e:
        return None

if __name__ == '__main__':
    pass