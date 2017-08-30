from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
_table_name_data = "movie"

class bogo_movie(Base):
    __tablename__ = _table_name_data

    id              = Column(Integer, primary_key=True, autoincrement=True)    # ID (primary)
    views           = Column(Integer)           # 조회수
    comment_number  = Column(Integer)           # 댓글 갯수
    title           = Column(String(256))       # 제목
    url             = Column(String(256))       # URL
    link_1          = Column(String(256))       # Downloadable Link1
    link_2          = Column(String(256))       # Downloadable Link2
    link_3          = Column(String(256))       # Downloadable Link3

    def __init__(self, views, comment_number, title, url, link_1, link_2, link_3):
        self.views = views
        self.comment_number = comment_number
        self.title = title
        self.url = url
        self.link_1 = link_1
        self.link_2 = link_2
        self.link_3 = link_3

    def __repr__(self):
        item = {"id": self.id, "views": self.views, "comment_number": self.comment_number, "title": self.title}
        return "\tid : {id}\n\tviews = {views}\n\tcomment_number={comment_number}\n\ttitle={title}".format_map(item)

def check_database(engine):
    if not engine.dialect.has_table(engine, _table_name_data):
        print(bogo_movie.__table__) # show schema
        bogo_movie.metadata.create_all(bind=engine)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("sqlite:///sqlalchemy.sqlite", echo=True, convert_unicode=True)
    check_database(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # 조회수, 댓글 갯수, 제목, URL, Downloadable Link1, Downloadable Link2, Downloadable Link3
    new_movie = bogo_movie(5, 7, "title", "http://naver.com", "Link1", "Link2", "Link3")

    session.add(new_movie)
    session.commit()

    #item_code = session.query(megabox_movie).filter_by().first()

    session.close()
