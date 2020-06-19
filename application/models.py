from application import db



class Topics(db.Model):
      id = db.Column(db.Integer, primary_key=True, autoincrement=True)
      topic_title = db.Column(db.String(500), nullable=False, unique=True)
      topic_desc = db.Column(db.String(500), nullable=False, unique=True)


      def __repr__(self):
        return ''.join([
            'Topic ID: ', self.id, ' ','\r\n',
            'Title: ', self.topic_title, '\r\n',
            'Description:', self.topic_desc, '\r\n'
            ])


class Podcast(db.Model):
      id = db.Column(db.Integer, primary_key=True, autoincrement=True)
      podcast_title = db.Column(db.String(500), nullable=False, unique=True)
      podcast_detail = db.Column(db.String(500),nullable=False, unique=True)
      episode = db.relationship('Topics',
            secondary = 'episode',
            cascade = 'delete',
            backref = db.backref('episode'),
            lazy = 'dynamic')
      
      def __repr__(self):
          return ''.join([
              'Podcast ID: ', self.id, ' ','\r\n',
              'Title: ', self.podcast_title, '\r\n',
              'Detail: ', self.podcast_detail, '\r\n'
              ])


episode = db.Table('episode', db.Model.metadata,
    db.Column('podcast_id', db.Integer, db.ForeignKey('podcast.id')),
    db.Column('topic_id', db.Integer, db.ForeignKey('topics.id'))

  )


