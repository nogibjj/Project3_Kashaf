from step3 import connect_db
from step3 import create_df
from step3 import q_test


def test(cursor=connect_db()):
    q_test = "SELECT count(Country_Region) FROM aqi_country where aqi_2019 != '-';"
    qtest1 = create_df(cursor.execute(q_test).fetchall(), cursor)
    print(qtest1)

def test_add():
    assert test() == q_test()