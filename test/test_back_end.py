import unittest

from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Topics, Podcast
from os import getenv


class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app


    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()



        update=Topics(topic_title='Test Title', topic_desc='Test Description01')
        db.session.add(update)
        db.session.commit
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):
    def test_homepage_view(self):

        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_topics_view(self):
        response = self.client.get(url_for('topics'))
        self.assertEqual(response.status_code, 200)

    def test_podcast_view(self):
        response = self.client.get(url_for('podcast'))
        self.assertEqual(response.status_code, 200)

    def test_schedule_view(self):
        response = self.client.get(url_for('schedule'))
        self.assertEqual(response.status_code, 200)
        



class TestTopics(TestBase):
    def test_add_new_topic(self):
        with self.client:
            response = self.client.post(
                    '/topics',
                    data=dict(
                        title='Test Title',
                        desc='Test Description'
                    ),
                    follow_redirects=True
            )
            self.assertIn(b'Test Title', response.data)





class TestPodcast(TestBase):
    def test_add_new_podcast(self):
        with self.client:
            response = self.client.post(
                    '/podcast',
                    data=dict(
                        title='Test Title',
                        detail='Test Detail'
                    ),
                    follow_redirects=True
            )
            self.assertIn(b'Test Title', response.data)




class Testupdatetopic(TestBase):
    def test_add_update_topic(self):
        with self.client:
            response = self.client.post(
                    '/updatetopics/1',
                    data=dict(
                        title='Test Title',
                        desc='Test Description01'
                    ),
                    follow_redirects=True
            )
            self.assertIn(b'Test Title', response.data)

